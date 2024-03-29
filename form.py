# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_global_form(object):
    def setupUi(self, global_form):
        global_form.setObjectName("global_form")
        global_form.resize(594, 591)
        self.scrollArea = QtWidgets.QScrollArea(parent=global_form)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 571, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 556, 1045))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_template_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.select_template_button.setObjectName("select_template_button")
        self.horizontalLayout_2.addWidget(self.select_template_button)
        self.template_path = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.template_path.setEnabled(False)
        self.template_path.setObjectName("template_path")
        self.horizontalLayout_2.addWidget(self.template_path)
        self.line = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.max_width_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.max_width_label.setObjectName("max_width_label")
        self.horizontalLayout_2.addWidget(self.max_width_label)
        self.max_width_lineEdit = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.max_width_lineEdit.setSizePolicy(sizePolicy)
        self.max_width_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.max_width_lineEdit.setMaximumSize(QtCore.QSize(35, 16777215))
        self.max_width_lineEdit.setObjectName("max_width_lineEdit")
        self.horizontalLayout_2.addWidget(self.max_width_lineEdit)
        self.resize_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.resize_button.setObjectName("resize_button")
        self.horizontalLayout_2.addWidget(self.resize_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.detect_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.detect_button.setObjectName("detect_button")
        self.horizontalLayout_3.addWidget(self.detect_button)
        self.open_settings_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.open_settings_button.setObjectName("open_settings_button")
        self.horizontalLayout_3.addWidget(self.open_settings_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.mode_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.mode_label.setObjectName("mode_label")
        self.horizontalLayout_3.addWidget(self.mode_label)
        self.mode_comboBox = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.mode_comboBox.setObjectName("mode_comboBox")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.mode_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.export_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout_3.addWidget(self.export_button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.img_widget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.img_widget.setMinimumSize(QtCore.QSize(300, 1000))
        self.img_widget.setObjectName("img_widget")
        self.gridLayout.addWidget(self.img_widget, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(global_form)
        QtCore.QMetaObject.connectSlotsByName(global_form)

    def retranslateUi(self, global_form):
        _translate = QtCore.QCoreApplication.translate
        global_form.setWindowTitle(_translate("global_form", "Template Manager"))
        self.select_template_button.setText(_translate("global_form", "Select Template"))
        self.max_width_label.setText(_translate("global_form", "Max Width"))
        self.max_width_lineEdit.setText(_translate("global_form", "1150"))
        self.resize_button.setText(_translate("global_form", "Resize and save"))
        self.detect_button.setText(_translate("global_form", "Detection"))
        self.open_settings_button.setText(_translate("global_form", "Settings"))
        self.mode_label.setText(_translate("global_form", "Mode"))
        self.mode_comboBox.setItemText(0, _translate("global_form", "Owned"))
        self.mode_comboBox.setItemText(1, _translate("global_form", "Wanted"))
        self.mode_comboBox.setItemText(2, _translate("global_form", "Favorite"))
        self.export_button.setText(_translate("global_form", "Export"))
