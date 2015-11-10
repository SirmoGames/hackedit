# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Documents/hackedit/data/forms/settings_page_workspaces.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(834, 496)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_add_workspace = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.bt_add_workspace.setIcon(icon)
        self.bt_add_workspace.setObjectName("bt_add_workspace")
        self.horizontalLayout_2.addWidget(self.bt_add_workspace)
        self.bt_remove_workspace = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.bt_remove_workspace.setIcon(icon)
        self.bt_remove_workspace.setObjectName("bt_remove_workspace")
        self.horizontalLayout_2.addWidget(self.bt_remove_workspace)
        self.bt_copy_workspace = QtWidgets.QToolButton(self.groupBox)
        self.bt_copy_workspace.setText("")
        icon = QtGui.QIcon.fromTheme("edit-copy")
        self.bt_copy_workspace.setIcon(icon)
        self.bt_copy_workspace.setObjectName("bt_copy_workspace")
        self.horizontalLayout_2.addWidget(self.bt_copy_workspace)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.list_workspaces = QtWidgets.QListWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_workspaces.sizePolicy().hasHeightForWidth())
        self.list_workspaces.setSizePolicy(sizePolicy)
        self.list_workspaces.setMinimumSize(QtCore.QSize(160, 0))
        self.list_workspaces.setMaximumSize(QtCore.QSize(160, 16777215))
        self.list_workspaces.setObjectName("list_workspaces")
        self.gridLayout.addWidget(self.list_workspaces, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.group_properties = QtWidgets.QGroupBox(Form)
        self.group_properties.setObjectName("group_properties")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_properties)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_read_only = QtWidgets.QLabel(self.group_properties)
        self.label_read_only.setStyleSheet("background-color: #DD8080;\n"
"color: white;\n"
"padding: 10px;\n"
"border-radius:3px;")
        self.label_read_only.setObjectName("label_read_only")
        self.verticalLayout.addWidget(self.label_read_only)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.group_properties)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.edit_name = QtWidgets.QLineEdit(self.group_properties)
        self.edit_name.setObjectName("edit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name)
        self.label_2 = QtWidgets.QLabel(self.group_properties)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.edit_description = QtWidgets.QLineEdit(self.group_properties)
        self.edit_description.setObjectName("edit_description")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_description)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.group_properties)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_available_plugins = QtWidgets.QListWidget(self.groupBox_4)
        self.list_available_plugins.setMinimumSize(QtCore.QSize(250, 0))
        self.list_available_plugins.setObjectName("list_available_plugins")
        self.gridLayout_2.addWidget(self.list_available_plugins, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.bt_add_plugin = QtWidgets.QPushButton(self.group_properties)
        self.bt_add_plugin.setText("")
        icon = QtGui.QIcon.fromTheme("go-next")
        self.bt_add_plugin.setIcon(icon)
        self.bt_add_plugin.setObjectName("bt_add_plugin")
        self.verticalLayout_2.addWidget(self.bt_add_plugin)
        self.bt_rm_plugin = QtWidgets.QPushButton(self.group_properties)
        self.bt_rm_plugin.setText("")
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.bt_rm_plugin.setIcon(icon)
        self.bt_rm_plugin.setObjectName("bt_rm_plugin")
        self.verticalLayout_2.addWidget(self.bt_rm_plugin)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.group_properties)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.list_used_plugins = QtWidgets.QListWidget(self.groupBox_5)
        self.list_used_plugins.setMinimumSize(QtCore.QSize(250, 0))
        self.list_used_plugins.setObjectName("list_used_plugins")
        self.gridLayout_3.addWidget(self.list_used_plugins, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addWidget(self.group_properties)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Workspaces"))
        self.bt_add_workspace.setToolTip(_translate("Form", "Add a new empty workspace"))
        self.bt_add_workspace.setText(_translate("Form", "..."))
        self.bt_remove_workspace.setToolTip(_translate("Form", "Delete selected workspace"))
        self.bt_remove_workspace.setText(_translate("Form", "..."))
        self.bt_copy_workspace.setToolTip(_translate("Form", "Copy the selected workspace"))
        self.list_workspaces.setToolTip(_translate("Form", "The list of available workspaces."))
        self.group_properties.setTitle(_translate("Form", "Properties"))
        self.label_read_only.setText(_translate("Form", "<html><head/><body><p align=\"center\">This workspace is read-only. You must clone it if you want to modify it...</p></body></html>"))
        self.label.setText(_translate("Form", "Name:"))
        self.edit_name.setToolTip(_translate("Form", "Name of the workspace"))
        self.label_2.setText(_translate("Form", "Description:"))
        self.edit_description.setToolTip(_translate("Form", "Description of the workspace"))
        self.groupBox_4.setTitle(_translate("Form", "Available"))
        self.list_available_plugins.setToolTip(_translate("Form", "List of available workspaces"))
        self.bt_add_plugin.setToolTip(_translate("Form", "Add the selected plugin to the workspace"))
        self.bt_rm_plugin.setToolTip(_translate("Form", "Remove the selected plugin from workspace"))
        self.groupBox_5.setTitle(_translate("Form", "Used"))
        self.list_used_plugins.setToolTip(_translate("Form", "List of plugins used by the workspace"))

