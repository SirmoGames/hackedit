# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Documents/hackedit/data/forms/settings_page_editor.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 656)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 752, 648))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cb_encoding = EncodingsComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_encoding.sizePolicy().hasHeightForWidth())
        self.cb_encoding.setSizePolicy(sizePolicy)
        self.cb_encoding.setObjectName("cb_encoding")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_encoding)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.cb_eol_convention = QtWidgets.QComboBox(self.groupBox_4)
        self.cb_eol_convention.setObjectName("cb_eol_convention")
        self.cb_eol_convention.addItem("")
        self.cb_eol_convention.addItem("")
        self.cb_eol_convention.addItem("")
        self.cb_eol_convention.addItem("")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_eol_convention)
        self.cb_autodetect_eol = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_autodetect_eol.setChecked(True)
        self.cb_autodetect_eol.setObjectName("cb_autodetect_eol")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_autodetect_eol)
        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cb_autocomplete = QtWidgets.QCheckBox(self.groupBox_5)
        self.cb_autocomplete.setObjectName("cb_autocomplete")
        self.verticalLayout_4.addWidget(self.cb_autocomplete)
        self.cb_autoindent = QtWidgets.QCheckBox(self.groupBox_5)
        self.cb_autoindent.setObjectName("cb_autoindent")
        self.verticalLayout_4.addWidget(self.cb_autoindent)
        self.cb_backspace_unindents = QtWidgets.QCheckBox(self.groupBox_5)
        self.cb_backspace_unindents.setObjectName("cb_backspace_unindents")
        self.verticalLayout_4.addWidget(self.cb_backspace_unindents)
        self.gridLayout_3.addWidget(self.groupBox_5, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spin_cc_trigger_len = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_cc_trigger_len.sizePolicy().hasHeightForWidth())
        self.spin_cc_trigger_len.setSizePolicy(sizePolicy)
        self.spin_cc_trigger_len.setObjectName("spin_cc_trigger_len")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_cc_trigger_len)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cb_cc_tooltips = QtWidgets.QCheckBox(self.groupBox_2)
        self.cb_cc_tooltips.setText("")
        self.cb_cc_tooltips.setObjectName("cb_cc_tooltips")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_cc_tooltips)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.cb_cc_case_sensitive = QtWidgets.QCheckBox(self.groupBox_2)
        self.cb_cc_case_sensitive.setText("")
        self.cb_cc_case_sensitive.setObjectName("cb_cc_case_sensitive")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cb_cc_case_sensitive)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cb_cc_filter_mode = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_cc_filter_mode.sizePolicy().hasHeightForWidth())
        self.cb_cc_filter_mode.setSizePolicy(sizePolicy)
        self.cb_cc_filter_mode.setObjectName("cb_cc_filter_mode")
        self.cb_cc_filter_mode.addItem("")
        self.cb_cc_filter_mode.addItem("")
        self.cb_cc_filter_mode.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_cc_filter_mode)
        self.gridLayout_3.addWidget(self.groupBox_2, 5, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.cb_safe_save = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_safe_save.setChecked(True)
        self.cb_safe_save.setObjectName("cb_safe_save")
        self.gridLayout.addWidget(self.cb_safe_save, 1, 1, 1, 1)
        self.cb_convert_tabs_to_spaces = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_convert_tabs_to_spaces.setChecked(True)
        self.cb_convert_tabs_to_spaces.setObjectName("cb_convert_tabs_to_spaces")
        self.gridLayout.addWidget(self.cb_convert_tabs_to_spaces, 0, 0, 1, 1)
        self.cb_restore_cursor = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_restore_cursor.setChecked(True)
        self.cb_restore_cursor.setObjectName("cb_restore_cursor")
        self.gridLayout.addWidget(self.cb_restore_cursor, 1, 0, 1, 1)
        self.cb_clean_trailing = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_clean_trailing.setChecked(True)
        self.cb_clean_trailing.setObjectName("cb_clean_trailing")
        self.gridLayout.addWidget(self.cb_clean_trailing, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 6, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.cb_spaces_instead_of_tabs = QtWidgets.QCheckBox(self.groupBox)
        self.cb_spaces_instead_of_tabs.setText("")
        self.cb_spaces_instead_of_tabs.setChecked(True)
        self.cb_spaces_instead_of_tabs.setObjectName("cb_spaces_instead_of_tabs")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_spaces_instead_of_tabs)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spin_tab_len = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_tab_len.sizePolicy().hasHeightForWidth())
        self.spin_tab_len.setSizePolicy(sizePolicy)
        self.spin_tab_len.setProperty("value", 4)
        self.spin_tab_len.setObjectName("spin_tab_len")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_tab_len)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        self.cb_cc_filter_mode.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_4.setTitle(_translate("Form", "File encodings & EOL"))
        self.label_5.setText(_translate("Form", "Default encoding:"))
        self.cb_encoding.setToolTip(_translate("Form", "Default encoding to use when opening files"))
        self.label_10.setText(_translate("Form", "Preferred EOL"))
        self.cb_eol_convention.setToolTip(_translate("Form", "Preferred EOL (will be used for new files and for saving files if auto detect is unchecked)."))
        self.cb_eol_convention.setItemText(0, _translate("Form", "System"))
        self.cb_eol_convention.setItemText(1, _translate("Form", "Linux"))
        self.cb_eol_convention.setItemText(2, _translate("Form", "Mac"))
        self.cb_eol_convention.setItemText(3, _translate("Form", "Windows"))
        self.cb_autodetect_eol.setToolTip(_translate("Form", "Automatically detects file line endings on open and use them for furute saves."))
        self.cb_autodetect_eol.setText(_translate("Form", "Autodetect EOL"))
        self.groupBox_5.setTitle(_translate("Form", "Typing"))
        self.cb_autocomplete.setToolTip(_translate("Form", "Enable automatic completion of quotes, parentheses and brackets."))
        self.cb_autocomplete.setText(_translate("Form", "Enable auto complete (of quotes and parentheses)"))
        self.cb_autoindent.setToolTip(_translate("Form", "Enable/Disable automatic indentation"))
        self.cb_autoindent.setText(_translate("Form", "Enable automatic indentation"))
        self.cb_backspace_unindents.setToolTip(_translate("Form", "Enable/Disable backspaces unindents. If checked, pressing backspace will deintent."))
        self.cb_backspace_unindents.setText(_translate("Form", "Backspace unindents"))
        self.groupBox_2.setTitle(_translate("Form", "Code completion"))
        self.label_3.setText(_translate("Form", "Trigger length:"))
        self.spin_cc_trigger_len.setToolTip(_translate("Form", "<html><head/><body><p>Numbers of character needed in a word to automatically  trigger code completion</p></body></html>"))
        self.label_6.setText(_translate("Form", "Show tooltips:"))
        self.cb_cc_tooltips.setToolTip(_translate("Form", "Show completion tooltip if available"))
        self.label_7.setText(_translate("Form", "Case sensitive:"))
        self.cb_cc_case_sensitive.setToolTip(_translate("Form", "Case sensitive completion"))
        self.label_9.setText(_translate("Form", "Filter mode:"))
        self.cb_cc_filter_mode.setToolTip(_translate("Form", "<html><head/><body><p>Completion filter mode: </p><p>  - Prefix (classic, fast and simple)</p><p>  - Subsequence (fuzzy, slower but more powerful)</p></body></html>"))
        self.cb_cc_filter_mode.setItemText(0, _translate("Form", "Prefix"))
        self.cb_cc_filter_mode.setItemText(1, _translate("Form", "Contains"))
        self.cb_cc_filter_mode.setItemText(2, _translate("Form", "Subsequence"))
        self.groupBox_3.setTitle(_translate("Form", "Open/Save"))
        self.cb_safe_save.setToolTip(_translate("Form", "Use a temporary file for the save, and rename that temporary file to final destination path if everything went right)"))
        self.cb_safe_save.setText(_translate("Form", "Safe save (save to a temporary file first)"))
        self.cb_convert_tabs_to_spaces.setToolTip(_translate("Form", "Convert tabs to spaces on open"))
        self.cb_convert_tabs_to_spaces.setText(_translate("Form", "Convert tabs to spaces"))
        self.cb_restore_cursor.setToolTip(_translate("Form", "Remember and restore previous cursor position on close/open"))
        self.cb_restore_cursor.setText(_translate("Form", "Restore cursor position"))
        self.cb_clean_trailing.setToolTip(_translate("Form", "Clean trailing whitespaces when saving editor content to disk"))
        self.cb_clean_trailing.setText(_translate("Form", "Clean trailing white-spaces"))
        self.groupBox.setTitle(_translate("Form", "Tabs and indentation"))
        self.label_11.setToolTip(_translate("Form", "Use n spaces instead of t"))
        self.label_11.setText(_translate("Form", "Use spaces instead of tabs"))
        self.label.setText(_translate("Form", "Indent size"))
        self.spin_tab_len.setToolTip(_translate("Form", "Number of spaces that makes up a t"))

from pyqode.core.widgets import EncodingsComboBox
