"""
This module contains the backend function that perform the actual indexation.

Those functions are run in a background task.
"""
import logging
import mimetypes
import os
import time
from fnmatch import fnmatch

from pyqode.core.share import Definition

from hackedit.api import utils
from hackedit.app.indexing import db


try:
    # new _scandir function in python 3.5
    from os import scandir as listdir
except ImportError:
    try:
        # new _scandir function from _scandir package on pypi
        from scandir import scandir as listdir
    except ImportError:
        # _scandir package not found, use the slow listdir function
        from os import listdir


def _logger():
    return logging.getLogger(__name__)


def index_project_files(task_handle, db_path, project_directory,
                        ignore_patterns, parser_plugins):
    """
    Perform project files indexation

    :param task_handle: TaskHandle to report task progress
    :param project_directory: Project directory to indexate
    :param ignore_patterns: The ignore patterns to respect.
    """
    # adjust ignore patterns to always exclude binary files from indexation
    ignore_patterns += ['*.exe', '*.dll', '*.usr', '*.so', '*.dylib', '*.svg',
                        '*.png', '*.jpeg', '*.jpg', '*.tga', '*.gif', '*.psd',
                        '*.db']
    try:
        with db.DbHelper(db_path) as dbhelper:
            # scan project dir recursively
            _scandir(task_handle, dbhelper, project_directory, ignore_patterns,
                     parser_plugins, project_directory)
            # remove paths that do not exist or that have been ignored
            task_handle.report_progress('Cleaning database', -1)
            for file_item in dbhelper.get_all_files():
                path = file_item[db.COL_FILE_PATH]
                if not os.path.exists(path) or \
                        _is_ignored_path(path, ignore_patterns):
                    dbhelper.delete_file(path)
    except Exception:
        _logger().exception('exception while indexing project: %s',
                            project_directory)


def _is_ignored_path(path, ignore_patterns=None):
    """
    Utility function that checks if a given path should be ignored.

    A path is ignored if it matches one of the ignored_patterns.

    :param path: the path to check
    :param ignore_patterns: The ignore patters to respect.
        If none, :func:hackedit.api.settings.ignore_patterns() is used instead.
    :returns: True if the path is in an directory that must be ignored
        or if the file name matches an ignore pattern, otherwise False.
    """
    if ignore_patterns is None:
        ignore_patterns = utils.get_ignored_patterns()

    def ignore(name):
        for ptrn in ignore_patterns:
            if fnmatch(name, ptrn):
                return True

    for part in os.path.normpath(path).split(os.path.sep):
        if part and ignore(part):
            return True
    return False


def _scandir(task_handle, dbhelper, directory, ignore_patterns,
             parser_plugins, root_directory):
    """
    :type task_handle: hackedit.api.tasks.TaskHandle
    :type dbhelper: hackedit.app.indexing.db.DbHelper
    :type directory: str
    :type ignore_patterns: list
    """
    rel_dir = os.path.relpath(directory, root_directory)
    task_handle.report_progress('Indexing %r' % rel_dir, -1)
    join = os.path.join
    isfile = os.path.isfile
    isdir = os.path.isdir
    for path in listdir(directory):
        try:
            path = path.name
        except AttributeError:
            _logger().debug('using the old python api for scanning dirs')
        full_path = join(directory, path)
        ignored = _is_ignored_path(full_path, ignore_patterns)
        if not ignored:
            if isfile(full_path):
                file_id = dbhelper.create_file(full_path)
                cur_mtime = os.path.getmtime(full_path)
                old_mtime = dbhelper.get_file_mtime(full_path)
                if old_mtime is None or cur_mtime > old_mtime:
                    # try to parse file symbols
                    _parse_document(task_handle, dbhelper, file_id, full_path,
                                    parser_plugins, root_directory)
                else:
                    print('skipping indexation for file %r, up to date' %
                          full_path)
            elif isdir(full_path):
                try:
                    _scandir(task_handle, dbhelper, full_path, ignore_patterns,
                             parser_plugins, root_directory)
                except PermissionError:
                    _logger().warn('failed to scan directory %r, permission '
                                   'error', full_path)
            time.sleep(0.0000001)


def _parse_document(task_handle, dbhelper, file_id, path, parser_plugins,
                    root_directory):
    """
    Parse file symbols using the indexor plugins.
    """
    rel_path = os.path.relpath(path, root_directory)
    task_handle.report_progress('Indexing %r' % rel_path, -1)
    mime = mimetypes.guess_type(path)[0]
    for plugin in parser_plugins:
        if mime in plugin.mimetypes:
            try:
                symbols = plugin.parse(path)
            except Exception as e:
                print(path, e)
            else:
                # flatten results and add to the db
                dbhelper.delete_file_symbols(file_id)
                _write_symbols_to_db(dbhelper, symbols, file_id,
                                     parent_id=None)
                dbhelper.update_file(path, os.path.getmtime(path))
                break


def _write_symbols_to_db(dbhelper, symbols, file_id, parent_id=None):
    """
    Writes the list of symbols to the index database.
    """
    for symbol in symbols:
        assert isinstance(symbol, Definition)
        try:
            icon_theme, icon_path = symbol.icon
        except TypeError:
            icon_theme, icon_path = '', ''
        symbol_id = dbhelper.create_symbol(
            symbol.name, symbol.line, symbol.column, icon_theme, icon_path,
            file_id, parent_symbol_id=parent_id)
        _write_symbols_to_db(dbhelper, symbol.children, file_id,
                             parent_id=symbol_id)
