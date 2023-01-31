import json
from PyQt5 import QtCore, QtGui, QtWidgets
from Module.Settings import Main as Settings

class Ui(Settings):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, OptionsWin):
        # Save window for the methods in Module/Settings
        self.OptionsWin = OptionsWin 
        OptionsWin.setObjectName("OptionsWin")
        OptionsWin.setWindowTitle("Options")
        OptionsWin.resize(675, 380)


        #_________________   VISUALS   ________________________#
        self.FontObj = QtGui.QFont()
        self.FontObj.setFamily(self.userFont)
        self.FontObj.setPointSize(10)
        OptionsWin.setFont(self.FontObj)

        self.arrow_cursor = QtGui.QCursor(QtCore.Qt.ArrowCursor)
        self.pointing_cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        

        #_________________   BUTTONS   ________________________#
        self.SaveBtn = QtWidgets.QPushButton(OptionsWin)
        self.NoRadio = QtWidgets.QRadioButton(OptionsWin)
        self.YesRadio = QtWidgets.QRadioButton(OptionsWin)
        self.CancelBtn = QtWidgets.QPushButton(OptionsWin)
        self.DefaultBtn = QtWidgets.QPushButton(OptionsWin)
        self.IconsPathBtn = QtWidgets.QToolButton(OptionsWin)
        self.DownloadPathBtn = QtWidgets.QToolButton(OptionsWin)

        self.SaveBtn.setMaximumSize(QtCore.QSize(16777215, 28))
        self.CancelBtn.setMaximumSize(QtCore.QSize(16777215, 28))
        self.DefaultBtn.setMaximumSize(QtCore.QSize(16777215, 28))
        self.IconsPathBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.DownloadPathBtn.setMaximumSize(QtCore.QSize(30, 30))

        self.IconsPathBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.DownloadPathBtn.setMinimumSize(QtCore.QSize(30, 30))

        self.NoRadio.setChecked(True)
        self.CancelBtn.setDefault(True)

        self.IconsPathBtn.setText("...")
        self.DownloadPathBtn.setText("...")
        
        self.YesRadio.setCursor(self.pointing_cursor)
        self.NoRadio.setCursor(self.pointing_cursor)


        #_________________   LABELS   ________________________#
        self.IpLabel = QtWidgets.QLabel(OptionsWin)
        self.PortLabel = QtWidgets.QLabel(OptionsWin)
        self.FontLabel = QtWidgets.QLabel(OptionsWin)
        self.LanguageLabel = QtWidgets.QLabel(OptionsWin)
        self.HomebrewLabel = QtWidgets.QLabel(OptionsWin)
        self.IconsPathLabel = QtWidgets.QLabel(OptionsWin)
        self.DownloadPathLabel = QtWidgets.QLabel(OptionsWin)


        #_________________   INPUTS   ________________________#
        self.Ip = QtWidgets.QLineEdit(OptionsWin)
        self.Port = QtWidgets.QSpinBox(OptionsWin)
        self.Fonts = QtWidgets.QFontComboBox(OptionsWin)
        self.IconPath = QtWidgets.QLineEdit(OptionsWin)
        self.Languages = QtWidgets.QComboBox(OptionsWin)
        self.DownloadPath = QtWidgets.QLineEdit(OptionsWin)
        self.EnableHbInfo = QtWidgets.QPlainTextEdit(OptionsWin)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.Ip.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.Port.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.Fonts.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.IconPath.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.DownloadPath.sizePolicy().hasHeightForWidth())

        self.Ip.setSizePolicy(sizePolicy)
        self.Port.setSizePolicy(sizePolicy)
        self.IconPath.setSizePolicy(sizePolicy)
        self.DownloadPath.setSizePolicy(sizePolicy)

        self.Languages.addItem("")
        self.Languages.addItem("")
        self.Languages.addItem("")
        self.Languages.setFrame(False)
        self.Languages.setFont(self.FontObj)
        self.Languages.setMaxVisibleItems(5)
        self.Languages.setCursor(self.pointing_cursor)
        self.Languages.setSizePolicy(sizePolicy)

        self.Fonts.setFrame(False)
        self.Fonts.setEditable(False)
        self.Fonts.setFont(self.FontObj)
        self.Fonts.setSizePolicy(sizePolicy)
        self.Fonts.setCurrentFont(self.FontObj)


        self.Ip.setFrame(False)
        self.Ip.setMaxLength(22)
        self.Ip.setFont(self.FontObj)
        self.Ip.setClearButtonEnabled(True)
        self.Ip.setCursor(self.pointing_cursor)
        self.Ip.setAlignment(QtCore.Qt.AlignCenter)
        
        self.Port.setFrame(False)
        self.Port.setMaximum(99999)
        self.Port.setFont(self.FontObj)
        self.Port.setAlignment(QtCore.Qt.AlignCenter)
        self.Port.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Port.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        paths = (self.IconPath, self.DownloadPath)
        for path in paths:
            path.setFrame(False)
            path.setReadOnly(True)
            path.setFont(self.FontObj)
            path.setClearButtonEnabled(True)
            path.setAlignment(QtCore.Qt.AlignCenter)
            path.setStyleSheet("border-radius: 13px;")

        self.EnableHbInfo.setEnabled(True)
        self.EnableHbInfo.setReadOnly(True)
        self.EnableHbInfo.setFont(self.FontObj)
        self.EnableHbInfo.setFrameShape(QtWidgets.QFrame.Box)

        max_40_height = QtCore.QSize(16777215, 40)
        max_50_height = QtCore.QSize(16777215, 50)

        self.Ip.setMaximumSize(max_40_height)
        self.Port.setMaximumSize(max_40_height)
        self.Fonts.setMaximumSize(max_50_height)
        self.IconPath.setMaximumSize(max_40_height)
        self.Languages.setMaximumSize(max_50_height)
        self.DownloadPath.setMaximumSize(max_40_height)
        self.EnableHbInfo.setMaximumSize(QtCore.QSize(16777215, 60))


        #_________________   TAB ORDER   ________________________#
        OptionsWin.setTabOrder(self.Fonts, self.Ip)
        OptionsWin.setTabOrder(self.Ip, self.IconsPathBtn)
        OptionsWin.setTabOrder(self.YesRadio, self.NoRadio)
        OptionsWin.setTabOrder(self.SaveBtn, self.CancelBtn)
        OptionsWin.setTabOrder(self.NoRadio, self.DefaultBtn)
        OptionsWin.setTabOrder(self.DefaultBtn, self.SaveBtn)
        OptionsWin.setTabOrder(self.DownloadPath, self.IconPath)
        OptionsWin.setTabOrder(self.CancelBtn, self.EnableHbInfo)
        OptionsWin.setTabOrder(self.DownloadPathBtn, self.YesRadio)
        OptionsWin.setTabOrder(self.EnableHbInfo, self.DownloadPath)
        OptionsWin.setTabOrder(self.IconsPathBtn, self.DownloadPathBtn)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)


        #_________________   LAYOUTS   ________________________#
        self.lineSeperator = QtWidgets.QFrame(OptionsWin)
        self.lineSeperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeperator.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.TopLayout = QtWidgets.QGridLayout()
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.FirstLayout = QtWidgets.QHBoxLayout()
        self.BottomLayout = QtWidgets.QHBoxLayout()
        self.SecondLayout = QtWidgets.QHBoxLayout()
        self.HombrewLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(OptionsWin)

        self.TopLayout.setVerticalSpacing(20)
        self.TopLayout.setHorizontalSpacing(10)
        self.TopLayout.setContentsMargins(-1, 10, -1, 10)

        self.verticalLayout_2.addLayout(self.MainLayout)
        
        self.MainLayout.addLayout(self.TopLayout)
        self.MainLayout.addWidget(self.lineSeperator)
        self.MainLayout.addLayout(self.BottomLayout)
        self.FirstLayout.addWidget(self.IconPath)
        self.FirstLayout.addWidget(self.IconsPathBtn)
        self.SecondLayout.addWidget(self.DownloadPath)
        self.SecondLayout.addWidget(self.DownloadPathBtn)
        
        self.TopLayout.addWidget(self.Languages, 0, 1, 1, 1,)
        self.TopLayout.addWidget(self.LanguageLabel, 0, 0, 1, 1)

        self.TopLayout.addWidget(self.Fonts, 1, 1, 1, 1)
        self.TopLayout.addWidget(self.FontLabel, 1, 0, 1, 1)
        
        self.TopLayout.addWidget(self.Ip, 2, 1, 1, 1)
        self.TopLayout.addWidget(self.IpLabel, 2, 0, 1, 1)

        self.TopLayout.addWidget(self.Port, 3, 1, 1, 1)
        self.TopLayout.addWidget(self.PortLabel, 3, 0, 1, 1)

        self.TopLayout.addLayout(self.FirstLayout, 4, 1, 1, 1)
        self.TopLayout.addWidget(self.IconsPathLabel, 4, 0, 1, 1)

        self.TopLayout.addLayout(self.SecondLayout, 5, 1, 1, 1)
        self.TopLayout.addWidget(self.DownloadPathLabel, 5, 0, 1, 1)
        
        self.TopLayout.addLayout(self.HombrewLayout, 6, 1, 1, 1)
        self.TopLayout.addWidget(self.HomebrewLabel, 6, 0, 1, 1)

        self.BottomLayout.setContentsMargins(50, 0, 50, -1)
        self.BottomLayout.addItem(spacerItem)
        self.BottomLayout.addWidget(self.SaveBtn)
        self.BottomLayout.addWidget(self.CancelBtn)
        self.BottomLayout.addWidget(self.DefaultBtn)

        self.HombrewLayout.addWidget(self.NoRadio)
        self.HombrewLayout.addWidget(self.YesRadio)
        self.HombrewLayout.addWidget(self.EnableHbInfo)


        #_________________   DEFAULT VALUES   _____________________#
        self.Port.setValue(int(self.userPort))
        self.Ip.setPlaceholderText(self.userIp)
        self.Fonts.setCurrentText(self.userFont)
        self.IconPath.setPlaceholderText(self.userIPath)
        self.DownloadPath.setPlaceholderText(self.userDPath)


        #_________________   SIGNALS        _______________________#
        self.NoRadio.setChecked(True)
        if self.userHB == "True":
            self.YesRadio.setChecked(True)
        
        self.SaveBtn.clicked.connect(
            lambda: self.save_cache(
                self.Fonts.currentText(),
                self.IconPath.text(),
                self.DownloadPath.text(),
                str(self.YesRadio.isChecked()),
                self.Port.text(),
                self.Ip.text(),
                self.Languages.currentText()
            )
        )

        self.DefaultBtn.clicked.connect(self.reset_to_defaults)
        self.CancelBtn.clicked.connect(lambda: OptionsWin.close())
        self.IconsPathBtn.clicked.connect(lambda: self.get_path("icons"))
        self.DownloadPathBtn.clicked.connect(lambda: self.get_path("download"))

        QtCore.QMetaObject.connectSlotsByName(OptionsWin)
        self.translate_ui()

    def get_cache(self) -> dict:
        with open(f"{self.temp_path}Settings.json", encoding="utf-8") as file:
            return json.load(file)

    def translate_ui(self):
        cache = self.get_cache()
        content = self.get_translation(cache.get("language"), "Settings")

        _translate = QtCore.QCoreApplication.translate
        self.Languages.setCurrentText(cache.get("Language"))
        self.NoRadio.setText(_translate("OptionsWin", content.get("NoRadio")))
        self.YesRadio.setText(_translate("OptionsWin", content.get("YesRadio")))
        self.SaveBtn.setText(_translate("OptionsWin", content.get("SaveBtn")))
        self.CancelBtn.setText(_translate("OptionsWin", content.get("CancelBtn")))
        self.IpLabel.setText(_translate("OptionsWin", content.get("YesRadio")))
        self.DefaultBtn.setText(_translate("OptionsWin", "DEFAULT"))
        self.PortLabel.setText(_translate("OptionsWin", "DEFAULT PORT"))
        self.FontLabel.setText(_translate("OptionsWin", "Default Font"))
        self.HomebrewLabel.setText(_translate("OptionsWin", "ENABLE HOMEBREW"))
        self.LanguageLabel.setText(_translate("OptionsWin", "DEFAULT LANGUAGE"))
        self.IconsPathLabel.setText(_translate("OptionsWin", "DEFAULT ICONS PATH"))
        self.DownloadPathLabel.setText(_translate("OptionsWin", "DEFAULT DOWNLOAD PATH"))
        self.EnableHbInfo.setPlainText(_translate("OptionsWin", "NOTE: Enabling this option will allow you to change homebrew icons but the caching will take longer depends on how many homebrews you have installed."))

        self.Languages.setItemText(0, _translate("OptionsWin", "Arabic"))
        self.Languages.setItemText(1, _translate("OptionsWin", "English"))
        self.Languages.setItemText(2, _translate("OptionsWin", "Spanish"))