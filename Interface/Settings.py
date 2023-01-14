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
        OptionsWin.resize(473, 246)
        OptionsWin.setMinimumSize(QtCore.QSize(473, 246))
        OptionsWin.setMaximumSize(QtCore.QSize(473, 246))

        #_________________   VISUALS   ________________________#
        self.FontObj = QtGui.QFont()
        self.FontObj.setFamily(self.userFont)
        self.FontObj.setPointSize(10)
        OptionsWin.setFont(self.FontObj)
        self.cursor = QtGui.QCursor(QtCore.Qt.ArrowCursor)
        
        #_________________   BUTTONS   ________________________#
        self.WindowBtns = QtWidgets.QDialogButtonBox(OptionsWin)
        self.WindowBtns.setGeometry(QtCore.QRect(30, 210, 300, 23))
        self.WindowBtns.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.WindowBtns.setObjectName("WindowBtns")

        self.DefaultBtn = QtWidgets.QDialogButtonBox(OptionsWin)
        self.DefaultBtn.setGeometry(QtCore.QRect(25, 210, 110, 23))
        self.DefaultBtn.setStandardButtons(QtWidgets.QDialogButtonBox.Yes)
        self.DefaultBtn.button(QtWidgets.QDialogButtonBox.Yes).setText("Default")
        self.DefaultBtn.setObjectName("DefaultBtn")

        self.IconsPathBtn = QtWidgets.QToolButton(OptionsWin)
        self.IconsPathBtn.setGeometry(QtCore.QRect(410, 89, 31, 24))
        self.IconsPathBtn.setObjectName("IconsPathBtn")

        self.DownloadPathBtn = QtWidgets.QToolButton(OptionsWin)
        self.DownloadPathBtn.setGeometry(QtCore.QRect(410, 119, 31, 24))
        self.DownloadPathBtn.setObjectName("DownloadPathBtn")

        self.YesRadio = QtWidgets.QRadioButton(OptionsWin)
        self.YesRadio.setGeometry(QtCore.QRect(170, 160, 82, 17))
        self.YesRadio.setObjectName("YesRadio")
        
        self.NoRadio = QtWidgets.QRadioButton(OptionsWin)
        self.NoRadio.setGeometry(QtCore.QRect(220, 160, 82, 17))
        self.NoRadio.setObjectName("NoRadio")

        #_________________   LABELS   ________________________#
        self.IpLabel = QtWidgets.QLabel(OptionsWin)
        self.IpLabel.setObjectName("IpLabel")
        self.IpLabel.setGeometry(QtCore.QRect(30, 59, 120, 22))

        self.PortLabel = QtWidgets.QLabel(OptionsWin)
        self.PortLabel.setGeometry(QtCore.QRect(30, 40, 120, 22))
        self.PortLabel.setObjectName("PortLabel")

        self.FontLabel = QtWidgets.QLabel(OptionsWin)
        self.FontLabel.setGeometry(QtCore.QRect(30, 8, 120, 22))
        self.FontLabel.setObjectName("FontLabel")

        self.IconsPathLabel = QtWidgets.QLabel(OptionsWin)
        self.IconsPathLabel.setGeometry(QtCore.QRect(30, 89, 120, 22))
        self.IconsPathLabel.setObjectName("IconsPathLabel")

        self.DownloadPathLabel = QtWidgets.QLabel(OptionsWin)
        self.DownloadPathLabel.setGeometry(QtCore.QRect(30, 119, 135, 22))
        self.DownloadPathLabel.setObjectName("DownloadPathLabel")

        self.HomebrewLabel = QtWidgets.QLabel(OptionsWin)
        self.HomebrewLabel.setGeometry(QtCore.QRect(30, 150, 110, 31))
        self.HomebrewLabel.setObjectName("HomebrewLabel")

        self.FontObj.setPointSize(8)
        self.EnableHbInfo = QtWidgets.QPlainTextEdit(OptionsWin)
        self.EnableHbInfo.setGeometry(QtCore.QRect(270, 140, 171, 51))
        self.EnableHbInfo.setFont(self.FontObj)
        self.EnableHbInfo.setStyleSheet("color: rgb(255, 53, 53);")
        self.EnableHbInfo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EnableHbInfo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EnableHbInfo.setReadOnly(True)
        self.EnableHbInfo.setObjectName("EnableHbInfo")

        #_________________   INPUTS   ________________________#
        self.Port = QtWidgets.QLineEdit(OptionsWin)
        self.Port.setGeometry(QtCore.QRect(170, 40, 271, 22))
        self.Port.setCursor(self.cursor)
        self.Port.setMaxLength(8)
        self.Port.setAlignment(QtCore.Qt.AlignCenter)
        self.Port.setClearButtonEnabled(True)
        self.Port.setObjectName("Port")

        self.Ip = QtWidgets.QLineEdit(OptionsWin)
        self.Ip.setGeometry(QtCore.QRect(170, 59, 271, 22))
        self.Ip.setCursor(self.cursor)
        self.Ip.setMaxLength(28)
        self.Ip.setAlignment(QtCore.Qt.AlignCenter)
        self.Ip.setClearButtonEnabled(True)
        self.Ip.setObjectName("Ip")

        self.FontPicker = QtWidgets.QFontComboBox(OptionsWin)
        self.FontPicker.setGeometry(QtCore.QRect(170, 8, 271, 22))
        self.FontPicker.setFont(self.FontObj)
        self.FontPicker.setCurrentFont(self.FontObj)
        self.FontPicker.setEditable(False)
        self.FontPicker.setFontFilters(QtWidgets.QFontComboBox.AllFonts)
        self.FontPicker.setObjectName("FontPicker")

        self.IconPath = QtWidgets.QLineEdit(OptionsWin)
        self.IconPath.setGeometry(QtCore.QRect(170, 89, 241, 22))
        self.IconPath.setCursor(self.cursor)
        self.IconPath.setText("")
        self.IconPath.setMaxLength(50)
        self.IconPath.setAlignment(QtCore.Qt.AlignCenter)
        self.IconPath.setReadOnly(True)
        self.IconPath.setObjectName("IconPath")

        self.DownloadPath = QtWidgets.QLineEdit(OptionsWin)
        self.DownloadPath.setGeometry(QtCore.QRect(170, 119, 241, 22))
        self.DownloadPath.setCursor(self.cursor)
        self.DownloadPath.setText("")
        self.DownloadPath.setMaxLength(50)
        self.DownloadPath.setAlignment(QtCore.Qt.AlignCenter)
        self.DownloadPath.setReadOnly(True)
        self.DownloadPath.setObjectName("DownloadPath")
        
        #_________________   SIGNALS   ________________________#
        self.NoRadio.setChecked(True)
        if self.userHB == "True":
            self.YesRadio.setChecked(True)

        self.WindowBtns.accepted.connect(
            lambda: self.save_cache(
                self.FontPicker.currentText(),
                self.IconPath.text(),
                self.DownloadPath.text(),
                str(self.YesRadio.isChecked()),
                self.Port.text(),
                self.Ip.text()
            )
        )
        self.DownloadPathBtn.clicked.connect(lambda: self.get_path("download"))
        self.IconsPathBtn.clicked.connect(lambda: self.get_path("icons"))
        self.WindowBtns.rejected.connect(OptionsWin.close)
        self.DefaultBtn.accepted.connect(self.reset_to_defaults)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(OptionsWin)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.NoRadio.setText(_translate("OptionsWin", "Off"))
        self.YesRadio.setText(_translate("OptionsWin", "On"))
        self.IconsPathBtn.setText(_translate("OptionsWin", "..."))
        self.IpLabel.setText(_translate("OptionsWin", "Default IP"))
        self.DownloadPathBtn.setText(_translate("OptionsWin", "..."))
        self.PortLabel.setText(_translate("OptionsWin", "Default Port"))
        self.FontLabel.setText(_translate("OptionsWin", "Default Font"))
        self.HomebrewLabel.setText(_translate("OptionsWin", "Detect Homebrew"))
        self.IconsPathLabel.setText(_translate("OptionsWin", "Default Icon Path"))
        self.DownloadPathLabel.setText(_translate("OptionsWin", "Default Download Path"))
        self.EnableHbInfo.setPlainText(_translate("OptionsWin", "Allow Homebrew / Apps icons\n to be detected(This will take longer to cache)",))

        self.Ip.setPlaceholderText(_translate("OptionsWin", self.userIp))
        self.Port.setPlaceholderText(_translate("OptionsWin", self.userPort))
        self.FontPicker.setCurrentText(_translate("OptionsWin", self.userFont))
        self.IconPath.setPlaceholderText(_translate("OptionsWin", self.userIPath))
        self.DownloadPath.setPlaceholderText(_translate("OptionsWin", self.userDPath))