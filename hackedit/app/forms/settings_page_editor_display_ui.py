# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Documents/HackEdit/hackedit/data/forms/settings_page_editor_display.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 575)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 633, 563))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cb_text_wrapping = QtWidgets.QCheckBox(self.groupBox_5)
        self.cb_text_wrapping.setObjectName("cb_text_wrapping")
        self.verticalLayout_5.addWidget(self.cb_text_wrapping)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_margin = QtWidgets.QCheckBox(self.groupBox_5)
        self.cb_margin.setObjectName("cb_margin")
        self.horizontalLayout.addWidget(self.cb_margin)
        self.spin_margin_pos = QtWidgets.QSpinBox(self.groupBox_5)
        self.spin_margin_pos.setMaximum(200)
        self.spin_margin_pos.setProperty("value", 79)
        self.spin_margin_pos.setObjectName("spin_margin_pos")
        self.horizontalLayout.addWidget(self.spin_margin_pos)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.cb_show_global_errors = QtWidgets.QCheckBox(self.groupBox)
        self.cb_show_global_errors.setObjectName("cb_show_global_errors")
        self.gridLayout.addWidget(self.cb_show_global_errors, 2, 0, 1, 1)
        self.cb_show_line_numbers = QtWidgets.QCheckBox(self.groupBox)
        self.cb_show_line_numbers.setObjectName("cb_show_line_numbers")
        self.gridLayout.addWidget(self.cb_show_line_numbers, 0, 0, 1, 1)
        self.cb_caret_cope = QtWidgets.QCheckBox(self.groupBox)
        self.cb_caret_cope.setObjectName("cb_caret_cope")
        self.gridLayout.addWidget(self.cb_caret_cope, 0, 1, 1, 1)
        self.cb_show_folding = QtWidgets.QCheckBox(self.groupBox)
        self.cb_show_folding.setObjectName("cb_show_folding")
        self.gridLayout.addWidget(self.cb_show_folding, 1, 0, 1, 1)
        self.cb_show_whitespaces = QtWidgets.QCheckBox(self.groupBox)
        self.cb_show_whitespaces.setObjectName("cb_show_whitespaces")
        self.gridLayout.addWidget(self.cb_show_whitespaces, 4, 0, 1, 1)
        self.cb_caret_line = QtWidgets.QCheckBox(self.groupBox)
        self.cb_caret_line.setObjectName("cb_caret_line")
        self.gridLayout.addWidget(self.cb_caret_line, 1, 1, 1, 1)
        self.cb_show_errors = QtWidgets.QCheckBox(self.groupBox)
        self.cb_show_errors.setObjectName("cb_show_errors")
        self.gridLayout.addWidget(self.cb_show_errors, 3, 0, 1, 1)
        self.cb_parentheses = QtWidgets.QCheckBox(self.groupBox)
        self.cb_parentheses.setObjectName("cb_parentheses")
        self.gridLayout.addWidget(self.cb_parentheses, 2, 1, 1, 1)
        self.cb_center_on_scoll = QtWidgets.QCheckBox(self.groupBox)
        self.cb_center_on_scoll.setObjectName("cb_center_on_scoll")
        self.gridLayout.addWidget(self.cb_center_on_scoll, 3, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_5.setTitle(_translate("Form", "Text Wrapping"))
        self.cb_text_wrapping.setToolTip(_translate("Form", "Enable/Disable text wrapping"))
        self.cb_text_wrapping.setText(_translate("Form", "Enable text wrapping"))
        self.cb_margin.setToolTip(_translate("Form", "Show/Hide margin at the specified column"))
        self.cb_margin.setText(_translate("Form", "Show right margin at column:"))
        self.spin_margin_pos.setToolTip(_translate("Form", "Column where to draw the margin"))
        self.groupBox.setTitle(_translate("Form", "Display"))
        self.cb_show_global_errors.setToolTip(_translate("Form", "Show/Hide global panel (next to editor\'s vertical scrollbars)"))
        self.cb_show_global_errors.setText(_translate("Form", "Display global error panel"))
        self.cb_show_line_numbers.setToolTip(_translate("Form", "Show/Hide line numbers panel"))
        self.cb_show_line_numbers.setText(_translate("Form", "Display line numbers"))
        self.cb_caret_cope.setToolTip(_translate("Form", "Highlight scope under caret"))
        self.cb_caret_cope.setText(_translate("Form", "Highlight caret scope"))
        self.cb_show_folding.setToolTip(_translate("Form", "Show/Hide code folding markers"))
        self.cb_show_folding.setText(_translate("Form", "Display folding markers"))
        self.cb_show_whitespaces.setToolTip(_translate("Form", "Show whitespaces in editor"))
        self.cb_show_whitespaces.setText(_translate("Form", "Vizualize whitespaces"))
        self.cb_caret_line.setToolTip(_translate("Form", "Highlight line under caret"))
        self.cb_caret_line.setText(_translate("Form", "Highlight caret line"))
        self.cb_show_errors.setToolTip(_translate("Form", "Display linter/checker messages panel"))
        self.cb_show_errors.setText(_translate("Form", "Display linter panel"))
        self.cb_parentheses.setToolTip(_translate("Form", "Highlight matching/unmatching parentheses/brackets"))
        self.cb_parentheses.setText(_translate("Form", "Highlight matching parentheses"))
        self.cb_center_on_scoll.setToolTip(_translate("Form", "Center text cursor on scroll"))
        self.cb_center_on_scoll.setText(_translate("Form", "Center on scroll"))
