# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/hackedit/data/forms/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 575)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/hackedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_edit = QtWidgets.QWidget()
        self.page_edit.setObjectName("page_edit")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_edit)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = SplittableCodeEditTabWidget(self.page_edit)
        self.tabs.setObjectName("tabs")
        self.verticalLayout.addWidget(self.tabs)
        self.stackedWidget.addWidget(self.page_edit)
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_empty)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 171, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(193, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(192, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.page_empty)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_empty)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 27))
        self.menubar.setObjectName("menubar")
        self.mnu_file = QtWidgets.QMenu(self.menubar)
        self.mnu_file.setObjectName("mnu_file")
        self.mnu_view = QtWidgets.QMenu(self.menubar)
        self.mnu_view.setObjectName("mnu_view")
        self.mnu_windows = QtWidgets.QMenu(self.mnu_view)
        self.mnu_windows.setObjectName("mnu_windows")
        self.mnu_help = QtWidgets.QMenu(self.menubar)
        self.mnu_help.setObjectName("mnu_help")
        self.mnu_edit = QtWidgets.QMenu(self.menubar)
        self.mnu_edit.setObjectName("mnu_edit")
        self.menuActive_editor = QtWidgets.QMenu(self.mnu_edit)
        icon = QtGui.QIcon.fromTheme("accessories-text-editor")
        self.menuActive_editor.setIcon(icon)
        self.menuActive_editor.setObjectName("menuActive_editor")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.toolBarFile = QtWidgets.QToolBar(MainWindow)
        self.toolBarFile.setObjectName("toolBarFile")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFile)
        self.action_open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("folder")
        self.action_open.setIcon(icon)
        self.action_open.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.action_save.setIcon(icon)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.action_save_as.setIcon(icon)
        self.action_save_as.setObjectName("action_save_as")
        self.action_close = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("window-close")
        self.action_close.setIcon(icon)
        self.action_close.setObjectName("action_close")
        self.action_quit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.action_quit.setIcon(icon)
        self.action_quit.setObjectName("action_quit")
        self.action_preferences = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("preferences-system")
        self.action_preferences.setIcon(icon)
        self.action_preferences.setObjectName("action_preferences")
        self.action_about = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.action_about.setIcon(icon)
        self.action_about.setObjectName("action_about")
        self.action_help = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.action_help.setIcon(icon)
        self.action_help.setObjectName("action_help")
        self.action_new = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.action_new.setIcon(icon)
        self.action_new.setObjectName("action_new")
        self.action_report_bug = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("tools-report-bug")
        self.action_report_bug.setIcon(icon)
        self.action_report_bug.setObjectName("action_report_bug")
        self.action_save_all = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-all")
        self.action_save_all.setIcon(icon)
        self.action_save_all.setObjectName("action_save_all")
        self.action_check_for_update = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("system-software-update")
        self.action_check_for_update.setIcon(icon)
        self.action_check_for_update.setObjectName("action_check_for_update")
        self.a_fullscreen = QtWidgets.QAction(MainWindow)
        self.a_fullscreen.setCheckable(True)
        self.a_fullscreen.setChecked(False)
        icon = QtGui.QIcon.fromTheme("view-fullscreen")
        self.a_fullscreen.setIcon(icon)
        self.a_fullscreen.setObjectName("a_fullscreen")
        self.a_menu = QtWidgets.QAction(MainWindow)
        self.a_menu.setCheckable(True)
        self.a_menu.setChecked(True)
        self.a_menu.setObjectName("a_menu")
        self.a_toolbars = QtWidgets.QAction(MainWindow)
        self.a_toolbars.setCheckable(True)
        self.a_toolbars.setChecked(True)
        self.a_toolbars.setObjectName("a_toolbars")
        self.action_open_file = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.action_open_file.setIcon(icon)
        self.action_open_file.setObjectName("action_open_file")
        self.mnu_file.addAction(self.action_new)
        self.mnu_file.addAction(self.action_open_file)
        self.mnu_file.addAction(self.action_open)
        self.mnu_file.addSeparator()
        self.mnu_file.addAction(self.action_save)
        self.mnu_file.addAction(self.action_save_as)
        self.mnu_file.addAction(self.action_save_all)
        self.mnu_file.addSeparator()
        self.mnu_file.addAction(self.action_close)
        self.mnu_file.addSeparator()
        self.mnu_file.addAction(self.action_quit)
        self.mnu_view.addAction(self.a_fullscreen)
        self.mnu_view.addAction(self.a_menu)
        self.mnu_view.addAction(self.a_toolbars)
        self.mnu_view.addSeparator()
        self.mnu_view.addAction(self.mnu_windows.menuAction())
        self.mnu_help.addAction(self.action_help)
        self.mnu_help.addAction(self.action_about)
        self.mnu_help.addSeparator()
        self.mnu_help.addAction(self.action_report_bug)
        self.mnu_help.addSeparator()
        self.mnu_help.addAction(self.action_check_for_update)
        self.mnu_edit.addAction(self.menuActive_editor.menuAction())
        self.mnu_edit.addSeparator()
        self.mnu_edit.addAction(self.action_preferences)
        self.menubar.addAction(self.mnu_file.menuAction())
        self.menubar.addAction(self.mnu_edit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.mnu_view.menuAction())
        self.menubar.addAction(self.mnu_help.menuAction())
        self.toolBarFile.addAction(self.action_new)
        self.toolBarFile.addAction(self.action_open_file)
        self.toolBarFile.addAction(self.action_open)
        self.toolBarFile.addSeparator()
        self.toolBarFile.addAction(self.action_save)
        self.toolBarFile.addAction(self.action_save_as)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        import gettext
        _ = gettext.gettext

        MainWindow.setWindowTitle(_("HackEdit"))
        self.label.setText(_("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Open a document</span></p><hr/><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">File &gt; Open File</span> (<span style=\" font-style:italic;\">Ctrl+O</span>)</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Goto &gt; Goto anything</span> (<span style=\" font-style:italic;\">Ctrl+P</span>) and type to open file from any open project</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use the project tree view</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Drag and drop files here</li></ul></body></html>"))
        self.mnu_file.setTitle(_("&File"))
        self.mnu_view.setTitle(_("&View"))
        self.mnu_windows.setToolTip(_("The list of windows"))
        self.mnu_windows.setTitle(_("&Windows"))
        self.mnu_help.setTitle(_("?"))
        self.mnu_edit.setTitle(_("&Edit"))
        self.menuActive_editor.setToolTip(_("Active editor actions"))
        self.menuActive_editor.setTitle(_("&Active editor"))
        self.menuTools.setTitle(_("&Tools"))
        self.toolBarFile.setWindowTitle(_("FileToolBar"))
        self.action_open.setText(_("&Open project"))
        self.action_open.setToolTip(_("Open a project"))
        self.action_open.setShortcut(_("Ctrl+O"))
        self.action_save.setText(_("&Save"))
        self.action_save.setToolTip(_("Save current editor"))
        self.action_save.setShortcut(_("Ctrl+S"))
        self.action_save_as.setText(_("Sa&ve as"))
        self.action_save_as.setToolTip(_("Save current editor as"))
        self.action_save_as.setShortcut(_("Ctrl+Alt+S"))
        self.action_close.setText(_("&Close window"))
        self.action_close.setShortcut(_("Ctrl+Shift+Q"))
        self.action_quit.setText(_("&Quit"))
        self.action_quit.setToolTip(_("Quit application"))
        self.action_quit.setShortcut(_("Ctrl+Q"))
        self.action_preferences.setText(_("&Preferences"))
        self.action_preferences.setToolTip(_("Edit preferences"))
        self.action_preferences.setShortcut(_("Ctrl+,"))
        self.action_about.setText(_("&About"))
        self.action_about.setToolTip(_("About HackEdit"))
        self.action_help.setText(_("&Help"))
        self.action_help.setToolTip(_("Get some help"))
        self.action_new.setText(_("&New"))
        self.action_new.setToolTip(_("Create a new file/project"))
        self.action_new.setShortcut(_("Ctrl+N"))
        self.action_report_bug.setText(_("&Report bug"))
        self.action_report_bug.setToolTip(_("Report a bug"))
        self.action_save_all.setText(_("Save a&ll"))
        self.action_save_all.setToolTip(_("Save all editors"))
        self.action_save_all.setShortcut(_("Ctrl+Shift+S"))
        self.action_check_for_update.setText(_("&Check for update"))
        self.a_fullscreen.setText(_("&Toggle fullscreen"))
        self.a_fullscreen.setToolTip(_("Toggle fullscreen"))
        self.a_menu.setText(_("Toggle &menu"))
        self.a_menu.setToolTip(_("Show/Hide menu bar"))
        self.a_toolbars.setText(_("T&oggle toolbars"))
        self.a_toolbars.setToolTip(_("Show/Hide toolbars"))
        self.a_toolbars.setShortcut(_("Ctrl+Shift+T"))
        self.action_open_file.setText(_("Open &file"))
        self.action_open_file.setToolTip(_("Open a file"))

from pyqode.core.widgets import SplittableCodeEditTabWidget
