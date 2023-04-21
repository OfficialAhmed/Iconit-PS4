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
        self.new_icons_number.setMode(QtWidgets.QLCDNumber.Dec)
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
        

        #______________    SIGNALS    ____________________ #
        self.custom_group_btn.setEnabled(False)
        self.custom_group_btn.clicked.connect(self.render_custom_icons_window)
        self.default_group_btn.clicked.connect(lambda: self.set_default(self.custom_group_btn, self.default_group_btn, self.new_icons_number))

        self.calc_new_titles(self.custom_group_btn, self.new_icons_number)

        self.retranslateUi(self.window)
        QtCore.QMetaObject.connectSlotsByName(self.window)


    def render_custom_icons_window(self):
        window = QtWidgets.QDialog()
        ui = Custom_group()
        ui.setupUi(window)
        window.show()


    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Form", "SET ICON GROUP"))
            
        self.translated_content: dict = self.translation.get_translation(self.language, "SetDefaultIcons")       
        self.caution_message.setHtml(
            "<html><head><meta name='qrichtext' content='1' /><style type='text/css'>\n""p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=' font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;'>\n"
            f"{self.html.caution_p_tag('#ff2a2d')}{self.translated_content.get('caution')}</span></p>\n"
            f"{self.html.caution_msg_2('#ff2a2d')}<br /></p>\n"
            f"{self.html.caution_p_tag('#000000')}{self.translated_content.get('optionInfo')}</span></p>\n"
            f"{self.html.caution_msg_2('#000000')}<br /></p>\n"
            f"{self.html.caution_p_tag('#6db80a')}*{self.translated_content.get('moreInfo')}*</span></p>\n"
            f"{self.html.caution_msg_2('#6db80a')}<br /></p>\n"
            f"{self.html.caution_p_tag('#ea8d0b')}{self.translated_content.get('moreInfo2')}</span></p>\n"
            f"{self.html.caution_msg_2('#ea8d0b')}<br /></p>\n"
            f"{self.html.caution_p_tag('#6db80a')}{self.translated_content.get('moreInfo3')}</span></p></body></html>"
        )
        self.new_icons_label.setText(_translate("Form", self.translated_content.get('new_icons_label')))
        self.default_group_btn.setText(_translate("Form", self.translated_content.get('default_group_btn')))
        self.custom_group_btn.setText(_translate("Form", self.translated_content.get('custom_group_btn')))

