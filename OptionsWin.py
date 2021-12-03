from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class Ui_OptionsWin(object):
    def setupUi(self, OptionsWin):
        self.appPath = str(os.getcwd())
        self.tempPath = self.appPath + "\Data\prxUserMeta\\"
        # Settings
        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIp = ""
        self.userIPath = self.appPath
        self.userDPath = self.appPath
        self.userHB = "False"
        try:
            with open("Data/Pref/pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2: -1]
                self.userPort = content[1][2: -1]
                self.userIp = content[2][3: -1]
                self.userIPath = content[3][6: -1]
                self.userDPath = content[4][6: -1]
                self.userHB = (content[5][content[4].find(":")+1:])
        except:
            pass

        OptionsWin.setObjectName("OptionsWin")
        OptionsWin.resize(473, 246)
        OptionsWin.setMinimumSize(QtCore.QSize(473, 246))
        OptionsWin.setMaximumSize(QtCore.QSize(473, 246))
        self.font = QtGui.QFont()
        self.font.setFamily(self.userFont)
        self.font.setPointSize(10)
        OptionsWin.setFont(self.font)
        self.OptionsWin = OptionsWin  # For class methods to use

        self.Window_btn = QtWidgets.QDialogButtonBox(OptionsWin)
        self.Window_btn.setGeometry(QtCore.QRect(30, 210, 300, 23))
        self.Window_btn.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.Window_btn.setObjectName("Window_btn")

        self.Window_btn.accepted.connect(self.SaveOptions)
        self.Window_btn.rejected.connect(OptionsWin.close)

        self.Default_btn = QtWidgets.QDialogButtonBox(OptionsWin)
        self.Default_btn.setGeometry(QtCore.QRect(25, 210, 110, 23))

        self.Default_btn.setStandardButtons(
            QtWidgets.QDialogButtonBox.Yes)
        self.Default_btn.button(QtWidgets.QDialogButtonBox.Yes).setText(
            "Default settings")
        self.Default_btn.setObjectName("Default_btn")

        self.Default_btn.accepted.connect(self.ResetDefaults)

        self.BrowseIconPath_btn = QtWidgets.QToolButton(OptionsWin)
        self.BrowseIconPath_btn.setGeometry(QtCore.QRect(410, 89, 31, 24))
        self.BrowseIconPath_btn.setObjectName("BrowseIconPath_btn")
        self.BrowseDownloadPath_btn = QtWidgets.QToolButton(OptionsWin)
        self.BrowseDownloadPath_btn.setGeometry(QtCore.QRect(410, 119, 31, 24))
        self.BrowseDownloadPath_btn.setObjectName("BrowseDownloadPath_btn")

        self.BrowseDownloadPath_btn.clicked.connect(self.GetDownloadPath)
        self.BrowseIconPath_btn.clicked.connect(self.GetIconPath)

        self.Port_label = QtWidgets.QLabel(OptionsWin)
        self.Port_label.setGeometry(QtCore.QRect(30, 40, 120, 22))
        self.Port_label.setObjectName("Port_label")

        self.IP_label = QtWidgets.QLabel(OptionsWin)
        self.IP_label.setObjectName("IP_Label")
        self.IP_label.setGeometry(QtCore.QRect(30, 59, 120, 22))

        self.Font_label = QtWidgets.QLabel(OptionsWin)
        self.Font_label.setGeometry(QtCore.QRect(30, 8, 120, 22))
        self.Font_label.setObjectName("Font_label")
        self.IconPath_label = QtWidgets.QLabel(OptionsWin)
        self.IconPath_label.setGeometry(QtCore.QRect(30, 89, 120, 22))
        self.IconPath_label.setObjectName("IconPath_label")
        self.DownloadPath_label = QtWidgets.QLabel(OptionsWin)
        self.DownloadPath_label.setGeometry(QtCore.QRect(30, 119, 135, 22))
        self.DownloadPath_label.setObjectName("DownloadPath_label")
        self.ShowHB_label = QtWidgets.QLabel(OptionsWin)
        self.ShowHB_label.setGeometry(QtCore.QRect(30, 150, 99, 31))
        self.ShowHB_label.setObjectName("ShowHB_label")

        self.Port = QtWidgets.QLineEdit(OptionsWin)
        self.Port.setGeometry(QtCore.QRect(170, 40, 271, 22))
        self.Port.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Port.setMaxLength(8)
        self.Port.setAlignment(QtCore.Qt.AlignCenter)
        self.Port.setClearButtonEnabled(True)
        self.Port.setObjectName("Port")

        self.IP = QtWidgets.QLineEdit(OptionsWin)
        self.IP.setGeometry(QtCore.QRect(170, 59, 271, 22))
        self.IP.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.IP.setMaxLength(28)
        self.IP.setAlignment(QtCore.Qt.AlignCenter)
        self.IP.setClearButtonEnabled(True)
        self.IP.setObjectName("IP")

        self.Font = QtWidgets.QFontComboBox(OptionsWin)
        self.Font.setGeometry(QtCore.QRect(170, 8, 271, 22))
        self.Font.setFont(self.font)
        self.Font.setEditable(False)
        self.Font.setFontFilters(QtWidgets.QFontComboBox.AllFonts)
        self.Font.setCurrentFont(self.font)
        self.Font.setObjectName("Font")
        self.IconPath = QtWidgets.QLineEdit(OptionsWin)
        self.IconPath.setGeometry(QtCore.QRect(170, 89, 241, 22))
        self.IconPath.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.IconPath.setText("")
        self.IconPath.setMaxLength(50)
        self.IconPath.setAlignment(QtCore.Qt.AlignCenter)
        self.IconPath.setReadOnly(True)
        self.IconPath.setObjectName("IconPath")
        self.DownloadPath = QtWidgets.QLineEdit(OptionsWin)
        self.DownloadPath.setGeometry(QtCore.QRect(170, 119, 241, 22))
        self.DownloadPath.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DownloadPath.setText("")
        self.DownloadPath.setMaxLength(50)
        self.DownloadPath.setAlignment(QtCore.Qt.AlignCenter)
        self.DownloadPath.setReadOnly(True)
        self.DownloadPath.setObjectName("DownloadPath")

        self.Yes = QtWidgets.QRadioButton(OptionsWin)
        self.Yes.setGeometry(QtCore.QRect(170, 160, 82, 17))
        self.Yes.setObjectName("Yes")
        self.No = QtWidgets.QRadioButton(OptionsWin)
        self.No.setGeometry(QtCore.QRect(220, 160, 82, 17))
        self.No.setObjectName("No")

        if self.userHB == "True":
            self.Yes.setChecked(True)
        else:
            self.No.setChecked(True)

        self.font.setPointSize(8)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(OptionsWin)
        self.plainTextEdit.setGeometry(QtCore.QRect(270, 140, 171, 51))
        self.plainTextEdit.setFont(self.font)
        self.plainTextEdit.setStyleSheet("color: rgb(255, 53, 53);")
        self.plainTextEdit.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.IconPath.raise_()
        self.Window_btn.raise_()
        self.Default_btn.raise_()
        self.BrowseIconPath_btn.raise_()
        self.Port_label.raise_()
        self.IP_label.raise_()
        self.Font_label.raise_()
        self.IconPath_label.raise_()
        self.Port.raise_()
        self.Font.raise_()
        self.DownloadPath_label.raise_()
        self.ShowHB_label.raise_()
        self.DownloadPath.raise_()
        self.BrowseDownloadPath_btn.raise_()
        self.Yes.raise_()
        self.No.raise_()
        self.plainTextEdit.raise_()

        self.retranslateUi(OptionsWin)
        QtCore.QMetaObject.connectSlotsByName(OptionsWin)

    def retranslateUi(self, OptionsWin):
        _translate = QtCore.QCoreApplication.translate
        OptionsWin.setWindowTitle(_translate("OptionsWin", "Options"))
        self.BrowseIconPath_btn.setText(_translate("OptionsWin", "..."))
        self.BrowseDownloadPath_btn.setText(_translate("OptionsWin", "..."))
        self.Port_label.setText(_translate("OptionsWin", "Default Port"))
        self.IP_label.setText(_translate("OptionsWin", "Default IP"))
        self.Font_label.setText(_translate("OptionsWin", "Default Font"))
        self.IconPath_label.setText(_translate(
            "OptionsWin", "Default Icon Path"))
        self.ShowHB_label.setText(_translate("OptionsWin", "Show Homebrew"))
        self.Port.setPlaceholderText(_translate("OptionsWin", self.userPort))
        self.IP.setPlaceholderText(_translate("OptionsWin", self.userIp))
        self.IconPath.setPlaceholderText(
            _translate("OptionsWin", self.userIPath))
        self.Font.setCurrentText(_translate("OptionsWin", self.userFont))
        self.DownloadPath_label.setText(_translate(
            "OptionsWin", "Default Download Path"))
        self.DownloadPath.setPlaceholderText(
            _translate("OptionsWin", self.userDPath))
        self.Yes.setText(_translate("OptionsWin", "Yes"))
        self.No.setText(_translate("OptionsWin", "No"))
        self.plainTextEdit.setPlainText(_translate(
            "OptionsWin", "Yes will allow you to change Homebrew / Applications icons\n(This will take longer to cache)"))

    def ResetDefaults(self):
        try:
            with open("Data/Pref/pref.ini", "w+") as file:
                file.write("Set to default")
        except:
            pass

    def SaveOptions(self):
        Font = self.Font.currentText()
        IconPath = self.IconPath.text()
        DownloadPath = self.DownloadPath.text()
        ShowHB = str(self.Yes.isChecked())
        Port = self.Port.text()
        IP = self.IP.text()

        if len(Port) == 0:
            Port = self.userPort
        if len(IP) == 0:
            IP = self.userIp
        if len(IconPath) == 0:
            IconPath = self.userIPath
        if len(DownloadPath) == 0:
            DownloadPath = self.userDPath

        with open("Data/Pref/pref.ini", "w+") as file:
            file.write("F:" + Font + "\nP:" + str(Port) + "\nIP:" + IP + "\nIPath:" +
                       IconPath + "\nDPath:" + DownloadPath + "\nHB:" + ShowHB)
        self.OptionsWin.close()

    def GetDownloadPath(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.appPath)
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Default Download Directory...", self.appPath, options=opt)
        if path:
            self.DownloadPath.setText(path)

    def GetIconPath(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.appPath)
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Default Icon Directory...", self.appPath, options=opt)
        if path:
            self.IconPath.setText(path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionsWin = QtWidgets.QDialog()
    ui = Ui_OptionsWin()
    ui.setupUi(OptionsWin)
    OptionsWin.show()
    sys.exit(app.exec_())
