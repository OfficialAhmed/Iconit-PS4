from PyQt5 import QtCore, QtWidgets
from Module.Default_icons import Main as Default_icons
from Interface.Custom_group import Ui as Custom_group


class Ui(Default_icons):
        
    def setupUi(self, window):
        self.window = window
        self.window.setObjectName("Form")
        self.window.resize(720, 420)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.caution_message = QtWidgets.QTextBrowser(self.window)
        self.caution_message.setObjectName("caution_message")
        self.verticalLayout.addWidget(self.caution_message)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_icons_label = QtWidgets.QLabel(self.window)
        self.new_icons_label.setObjectName("new_icons_label")
        self.horizontalLayout_2.addWidget(self.new_icons_label)
        self.new_icons_number = QtWidgets.QLCDNumber(self.window)
        self.new_icons_number.setFrameShape(QtWidgets.QFrame.Panel)
        self.new_icons_number.setFrameShadow(QtWidgets.QFrame.Plain)
        self.new_icons_number.setDigitCount(3)
        self.new_icons_number.setMode(QtWidgets.QLCDNumber.Hex)
        self.new_icons_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.new_icons_number.setProperty("intValue", 0)
        self.new_icons_number.setObjectName("new_icons_number")
        self.horizontalLayout_2.addWidget(self.new_icons_number)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.default_group_btn = QtWidgets.QPushButton(self.window)
        self.default_group_btn.setObjectName("default_group_btn")
        self.verticalLayout.addWidget(self.default_group_btn)
        self.custom_group_btn = QtWidgets.QPushButton(self.window)
        self.custom_group_btn.setObjectName("custom_group_btn")
        self.verticalLayout.addWidget(self.custom_group_btn)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.custom_group_btn.clicked.connect(self.render_custom_icons_window)

        self.retranslateUi(self.window)
        QtCore.QMetaObject.connectSlotsByName(self.window)


    def render_custom_icons_window(self):
        window = QtWidgets.QDialog()
        ui = Custom_group()
        ui.setupUi(window)
        window.show()


    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Form", "Form"))
            
        
        self.caution_message.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ff2a2d;\">CAUTION! Read carefully</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#ff2a2d;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#000000;\">This option will use the current set of icons as the default set. It\'s recommended that you make sure all icons have the original icon/without any mask, otherwise the resulting icons will end up incorrect.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#6db80a;\">* You only need to use this option once *</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#6db80a;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ea8d0b;\">If you have new icons/games installed, rerun this option, otherwise the mask maker won\'t be able detect them.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#ea8d0b;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#6db80a;\">No worries I will let you know if I detect new icons</span></p></body></html>")
        self.new_icons_label.setText(_translate("Form", "NEW ICONS NOT IN [DEFAULT GROUP]"))
        self.default_group_btn.setText(_translate("Form", "SET/UPDATE DEFAULT GROUP"))
        self.custom_group_btn.setText(_translate("Form", "SET CUSTOM GROUP"))

