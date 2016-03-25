"""
High level api for manipulating project file/symbols index.

Indexing is the process of scanning a project directory recursively to build
an index of all the project files and their symbols.

To add your own index (e.g. to perform indexing on libraries), implement
:class:`hackedit.api.plugins.WorkspacePlugin` and call `perform_indexation` to
perform indexation when you plugin is activated.

To add you own symbol parser (e.g. to parse the symbols of an unsupported
mime types), just implement a :class:`hackedit.api.plugins.SymbolParserPlugin`,
define the mimetypes you support and implement the parse method.
"""
import os
import logging
import sqlite3

from hackedit.app.index import db
from hackedit.app.settings import indexing_enabled


class File:
    """
    Represents a file entry in the index database.
    """
    def __init__(self, item):
        self.name = item[db.COL_FILE_NAME]
        self.id = item[db.COL_FILE_ID]
        self.path = item[db.COL_FILE_PATH]
        self.time_stamp = item[db.COL_FILE_TIME_STAMP]
        self.project_id = item[db.COL_FILE_PROJECT_ID]

    def __repr__(self):
        return 'File(name=%r, id=%r, path=%r, time_stamp=%r)' % (
            self.name, self.id, self.path, self.time_stamp)


class Symbol:
    """
    Represents a symbol entry in the index database.
    """
    def __init__(self, item):
        self.name = item[db.COL_SYMBOL_NAME]
        self.id = int(item[db.COL_SYMBOL_ID])
        self.line = int(item[db.COL_SYMBOL_LINE])
        self.column = int(item[db.COL_SYMBOL_COLUMN])
        self.icon_theme = item[db.COL_SYMBOL_ICON_THEME]
        self.icon_path = item[db.COL_SYMBOL_ICON_PATH]
        self.file_id = int(item[db.COL_SYMBOL_FILE_ID])
        self.project_id = item[db.COL_FILE_PROJECT_ID]
        parent_id = item[db.COL_SYMBOL_PARENT_SYMBOL_ID]
        if not parent_id or parent_id == 'null':
            self.parent_symbol_id = None
        else:
            self.parent_symbol_id = int(parent_id)

    def __repr__(self):
        return 'Symbol(name=%r, id=%r, line=%r, column=%r)' % (
            self.name, self.id, self.line, self.column)


class Project:
    """
    Represents a project entry in the index database.
    """
    def __init__(self, item):
        self.name = item[db.COL_PROJECT_NAME]
        self.id = item[db.COL_PROJECT_ID]
        self.path = item[db.COL_PROJECT_PATH]

    def __repr__(self):
        return 'Project(name=%r, id=%r, path=%r)' % (
            self.name, self.id, self.path)


def _logger():
    return logging.getLogger(__name__)


def create_database():
    """
    Creates the index database if does not already exists.

    :return: Whether the operation succeeded or not.
    """
    try:
        with db.DbHelper():
            pass
    except (OSError, sqlite3.OperationalError):
        _logger().exception("failed to create index database...")
        return False
    else:
        return True


def get_all_projects():
    """
    Gets the list of indexed project paths.

    :return: list of paths
    """
    projects = []
    with db.DbHelper() as dbh:
        for item in dbh.get_projects():
            p = Project(item)
            projects.append(p)
    return sorted(projects, key=lambda x: x.name)


def get_project_ids(projects):
    """
    Gets the id of the specified projects.

    :param projects: list of project paths
    :return: list of id
    """
    project_ids = []
    if indexing_enabled():
        for proj in projects:
            with db.DbHelper() as dbh:
                p = dbh.get_project(proj)
                if p:
                    project_ids.append(p[db.COL_PROJECT_ID])
    return project_ids


def get_file(file_path):
    """
    Gets a file from the database
    :param file_path: path of the File entry to retrieve.

    :returns: File
    """
    with db.DbHelper() as dbh:
        row = dbh.get_file_by_path(file_path)
        if row:
            return File(row)
    return None


def get_files(name_filter='', projects=None):
    """
    Generator that yields all the File entries found in the index database.

    Client can restrict the search to the specified project paths.

    An optional name filter can be used to filter files by names.

    :param name_filter: Optional file name filter.
    :param projects: List of projects to search into. If None, all files from
    all indexed projects will be used.
    :return: A generator that yields class:`File`.
    """
    if not indexing_enabled():
        return
    project_ids = None
    if projects:
        project_ids = get_project_ids(projects)
    with db.DbHelper() as dbh:
        for itm in dbh.get_files(project_ids=project_ids,
                                 name_filter=name_filter):
            yield File(itm)


def get_symbols(name_filter='', projects=None, file=None):
    """
    Generator that yields all the Symbol entries found in the index database.

    Client can restrict search to the specified projects or the specified file.

    An optional name filter can be used to filter symbols by names.

    .. note:: You cannot specify both file and project filters.
        It's either one or the other (or none at all).

    :param name_filter: Optional symbol name filter
    :param projects: List of projects to search into.
        If None, all files from all indexed projects will be used.
    :param file: File to search into.

    :return: A generator that yields :class:`Symbol`.
    """
    if not indexing_enabled():
        return
    if projects and file:
        raise ValueError('Cannot set both file and projects parameter')
    project_ids = None
    if projects:
        project_ids = get_project_ids(projects)
    file_id = None
    if file:
        with db.DbHelper() as dbh:
            file_id = dbh.get_file_by_path(file)[db.COL_FILE_ID]
    with db.DbHelper() as dbh:
        for item in dbh.get_symbols(file_id=file_id, project_ids=project_ids,
                                    name_filter=name_filter):
            file_item = dbh.get_file_by_id(item[db.COL_SYMBOL_FILE_ID])
            if item and file_item:
                yield Symbol(item), File(file_item)


def perform_indexation(directories, callback=None, task_name=None):
    """
    Perform a background indexation of the specified directory.

    The optional callback function will be called automatically when operation
    has finished.

    :param directories: List of directories to perform indexation on.
    :param task_name: The name of the background task as show to the users.
                      Default is "Indexing project file (project_path)".
    :param callback: Callback function (callable).
    """
    if not indexing_enabled():
        return
    from hackedit.app.index import backend
    from ._shared import _window
    w = _window()
    ignored_patterns = w.project_explorer.get_ignored_patterns()
    parsers_plugins = w.project_explorer.parser_plugins
    args = directories, ignored_patterns, parsers_plugins
    if not task_name:
        task_name = _('Indexing project files')
    return w.task_manager.start(
        task_name, backend.index_project_files, callback, args, True, False)


def get_database_path():
    """
    Gets the path to the index database.
    """
    return db.DbHelper.get_db_path()


def remove_project(path):
    """
    Removes project from the index database

    :param path: path of the project to remove
    """
    with db.DbHelper() as dbh:
        dbh.delete_project(path)


def clear_database():
    """
    Clears the index database.

    The database file is deleted and an empty db is built.

    :return True if the operation succeeded, False otherwise.
    """
    try:
        os.remove(db.DbHelper.get_db_path())
    except OSError:
        return False
    else:
        # create empty db
        ok = False
        while not ok:
            try:
                ok = create_database()
            except IOError:
                ok = False
