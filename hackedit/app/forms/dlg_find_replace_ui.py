# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Colin/Documents/hackedit/data/forms/dlg_find_replace.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(441, 399)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.edit_find = QtWidgets.QLineEdit(Dialog)
        self.edit_find.setObjectName("edit_find")
        self.horizontalLayout_5.addWidget(self.edit_find)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_replace = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace.sizePolicy().hasHeightForWidth())
        self.label_replace.setSizePolicy(sizePolicy)
        self.label_replace.setObjectName("label_replace")
        self.horizontalLayout_6.addWidget(self.label_replace)
        self.edit_replace = QtWidgets.QLineEdit(Dialog)
        self.edit_replace.setObjectName("edit_replace")
        self.horizontalLayout_6.addWidget(self.edit_replace)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkbox_case_sensitive = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_case_sensitive.setObjectName("checkbox_case_sensitive")
        self.verticalLayout_2.addWidget(self.checkbox_case_sensitive)
        self.checkbox_whole_words = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_whole_words.setObjectName("checkbox_whole_words")
        self.verticalLayout_2.addWidget(self.checkbox_whole_words)
        self.checkbox_regexp = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_regexp.setObjectName("checkbox_regexp")
        self.verticalLayout_2.addWidget(self.checkbox_regexp)
        self.verticalLayout.addWidget(self.groupBox)
        self.scopes = QtWidgets.QGroupBox(Dialog)
        self.scopes.setObjectName("scopes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scopes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radio_all_projects = QtWidgets.QRadioButton(self.scopes)
        self.radio_all_projects.setChecked(True)
        self.radio_all_projects.setObjectName("radio_all_projects")
        self.verticalLayout_3.addWidget(self.radio_all_projects)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_project = QtWidgets.QRadioButton(self.scopes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_project.sizePolicy().hasHeightForWidth())
        self.radio_project.setSizePolicy(sizePolicy)
        self.radio_project.setObjectName("radio_project")
        self.horizontalLayout.addWidget(self.radio_project)
        self.combo_projects = QtWidgets.QComboBox(self.scopes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_projects.sizePolicy().hasHeightForWidth())
        self.combo_projects.setSizePolicy(sizePolicy)
        self.combo_projects.setObjectName("combo_projects")
        self.horizontalLayout.addWidget(self.combo_projects)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.scopes)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.edit_pattern = QtWidgets.QLineEdit(self.scopes)
        self.edit_pattern.setObjectName("edit_pattern")
        self.horizontalLayout_4.addWidget(self.edit_pattern)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.scopes)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.edit_find, self.edit_replace)
        Dialog.setTabOrder(self.edit_replace, self.checkbox_case_sensitive)
        Dialog.setTabOrder(self.checkbox_case_sensitive, self.checkbox_whole_words)
        Dialog.setTabOrder(self.checkbox_whole_words, self.checkbox_regexp)
        Dialog.setTabOrder(self.checkbox_regexp, self.radio_all_projects)
        Dialog.setTabOrder(self.radio_all_projects, self.radio_project)
        Dialog.setTabOrder(self.radio_project, self.combo_projects)
        Dialog.setTabOrder(self.combo_projects, self.edit_pattern)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Text to find:   "))
        self.edit_find.setToolTip(_translate("Dialog", "Text to find"))
        self.label_replace.setText(_translate("Dialog", "Replace with:"))
        self.edit_replace.setToolTip(_translate("Dialog", "Replacement text"))
        self.groupBox.setTitle(_translate("Dialog", "Options"))
        self.checkbox_case_sensitive.setToolTip(_translate("Dialog", "Case sensitive search"))
        self.checkbox_case_sensitive.setText(_translate("Dialog", "Case sensitive"))
        self.checkbox_whole_words.setToolTip(_translate("Dialog", "Search whole words only (may be faster)"))
        self.checkbox_whole_words.setText(_translate("Dialog", "Whole words only"))
        self.checkbox_regexp.setToolTip(_translate("Dialog", "Use a regular expression"))
        self.checkbox_regexp.setText(_translate("Dialog", "Regular expression"))
        self.scopes.setTitle(_translate("Dialog", "Scope"))
        self.radio_all_projects.setToolTip(_translate("Dialog", "Search in all open projects"))
        self.radio_all_projects.setText(_translate("Dialog", "A&ll projects"))
        self.radio_project.setToolTip(_translate("Dialog", "Search in the specified project"))
        self.radio_project.setText(_translate("Dialog", "Specific pro&ject"))
        self.combo_projects.setToolTip(_translate("Dialog", "The project to search in"))
        self.label_3.setText(_translate("Dialog", "File patterns:     "))
        self.edit_pattern.setToolTip(_translate("Dialog", "<html><head/><body><p>Match pattern. Files that don\'t match any pattern will get excluded from search.</p><p><br/></p><p>Use \';\' to separate patterns</p></body></html>"))

