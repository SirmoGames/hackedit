"""
This module contains a plugin that is able to render the html preview of
the current editor.
"""
from PyQt5 import QtGui, QtCore
from pyqode.core.widgets import HtmlPreviewWidget

from hackedit import api


class HtmlPreview(api.plugins.WorkspacePlugin):
    def activate(self):
        self.preview = HtmlPreviewWidget()
        self._dock = api.window.add_dock_widget(
            self.preview, 'Preview', icon=QtGui.QIcon.fromTheme(
                'internet-web-browser'), area=QtCore.Qt.RightDockWidgetArea)
        api.signals.connect_slot(api.signals.CURRENT_EDITOR_CHANGED,
                                 self.preview.set_editor)
        self.preview.hide_requested.connect(self._dock.hide)
        self.preview.show_requested.connect(self._dock.show)
        self.preview.set_editor(None)
        self._dock.hide()
