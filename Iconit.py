from itertools import count
import time  # (Ahm) 505
import os
import sys
import ctypes

# import threading v4.72
import _thread
from multiprocessing import Pool

from black import E
from sqlalchemy import false
import ChangeAvatar
import ChangeIcon
import Message
import Update
from ftplib import FTP
from PyQt5 import QtCore, QtGui, QtWidgets

myappid = "mycompany.myproduct.subproduct.version"  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# connection through FTP
# resizing images

ftp = FTP()
working_dir = "user/appmeta"
local_path = str(os.getcwd())
temp_path = local_path + "\Data\prxUserMeta\\"
img_dir = local_path + "\\data\\User\\appmeta"

sys_path = "system_ex\\app\\"

setting_path = ""
for change in local_path:
    if change == "\\":
        setting_path += "/"
    else:
        setting_path += change

IP = ""
Port = 21

all_CUSA = []
all_CUSA_ex = []
Game = {}


class Ui_IPortWindow(object):
    def setupUi(self, IPortWindow, w, h):
        global local_path, setting_path, temp_path, screenHeight, screenWidth
        self.ver = Update.get_update_version()

        # screen res
        self.w = w
        self.h = h

        # Settings
        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIp = ""
        self.userIPath = local_path
        self.userDPath = local_path
        self.userHB = "False"
        try:
            with open("Data/Pref/pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2:-1]
                self.userPort = content[1][2:-1]
                self.userIp = content[2][3:-1]
                self.userIPath = content[3][6:-1]
                self.userDPath = content[4][6:-1]
                self.userHB = content[5][3:].strip()
        except Exception as e:
            self.logIt(str(e), "Warning")
        font = QtGui.QFont()
        font.setFamily(self.userFont)
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)

        # v4.05 new UI support 2k, 4k res
        IPortWindow.setObjectName("IPortWindow")
        IPortWindow.setWindowModality(QtCore.Qt.WindowModal)
        IPortWindow.setWindowIcon(
            QtGui.QIcon(local_path + "\\Data\\Pref\\" + "ic1.@OfficialAhmed0")
        )

        IPortWindow.resize(720, 521)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IPortWindow.sizePolicy().hasHeightForWidth())
        IPortWindow.setSizePolicy(sizePolicy)
        IPortWindow.setMinimumSize(QtCore.QSize(720, 512))
        IPortWindow.setWindowOpacity(1.0)
        IPortWindow.setStyleSheet(
            "color: rgb(73, 170, 255); background-color: rgb(1, 10, 30);"
        )
        IPortWindow.setDocumentMode(False)
        IPortWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainWidget = QtWidgets.QWidget(IPortWindow)
        self.MainWidget.setObjectName("MainWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MainWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.FormLayout = QtWidgets.QFormLayout()
        self.FormLayout.setContentsMargins(20, 50, 20, 0)
        self.FormLayout.setHorizontalSpacing(5)
        self.FormLayout.setVerticalSpacing(0)
        self.FormLayout.setObjectName("FormLayout")
        self.Status = QtWidgets.QLabel(self.MainWidget)
        self.Status.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status.sizePolicy().hasHeightForWidth())
        self.Status.setSizePolicy(sizePolicy)
        self.Status.setMinimumSize(QtCore.QSize(500, 45))
        self.Status.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Status.setFont(font)
        self.Status.setStyleSheet("color: rgb(85, 170, 255);")
        self.Status.setFrameShape(QtWidgets.QFrame.Box)
        self.Status.setLineWidth(2)
        self.Status.setMidLineWidth(0)
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setIndent(-1)
        self.Status.setObjectName("label")
        self.FormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Status)
        self.hidenLabel = QtWidgets.QLabel(self.MainWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.hidenLabel.setFont(font)
        self.hidenLabel.setText("")
        self.hidenLabel.setObjectName("label_2")
        self.FormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hidenLabel)
        self.IP_Label = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_Label.sizePolicy().hasHeightForWidth())
        self.IP_Label.setSizePolicy(sizePolicy)
        self.IP_Label.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.IP_Label.setFont(font)
        self.IP_Label.setStyleSheet("color: rgb(85, 170, 255);")
        self.IP_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.IP_Label.setLineWidth(2)
        self.IP_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.IP_Label.setObjectName("IP_Label")
        self.FormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.IP_Label)
        self.IP_input = QtWidgets.QLineEdit(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_input.sizePolicy().hasHeightForWidth())
        self.IP_input.setSizePolicy(sizePolicy)
        self.IP_input.setMinimumSize(QtCore.QSize(500, 50))
        self.IP_input.setSizeIncrement(QtCore.QSize(0, 0))
        self.IP_input.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.IP_input.setFont(font)
        self.IP_input.setText(self.userIp)
        self.IP_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.IP_input.setMaxLength(24)
        self.IP_input.setAlignment(QtCore.Qt.AlignCenter)
        self.IP_input.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.IP_input.setClearButtonEnabled(True)
        self.IP_input.setObjectName("IP_input")
        self.FormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.IP_input)
        self.Port_Label = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Port_Label.sizePolicy().hasHeightForWidth())
        self.Port_Label.setSizePolicy(sizePolicy)
        self.Port_Label.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Port_Label.setFont(font)
        self.Port_Label.setStyleSheet("color: rgb(85, 170, 255);")
        self.Port_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.Port_Label.setLineWidth(2)
        self.Port_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_Label.setObjectName("Port_Label")
        self.FormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Port_Label)
        self.Port_input = QtWidgets.QLineEdit(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Port_input.sizePolicy().hasHeightForWidth())
        self.Port_input.setSizePolicy(sizePolicy)
        self.Port_input.setMinimumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Port_input.setFont(font)
        self.Port_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.Port_input.setText(self.userPort)
        self.Port_input.setMaxLength(10)
        self.Port_input.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_input.setClearButtonEnabled(True)
        self.Port_input.setObjectName("Port_input")
        self.FormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Port_input)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(0, 70, 0, 10)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Connect_btn = QtWidgets.QPushButton(self.MainWidget)
        self.Connect_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)

        self.Connect_btn.setFont(font)
        self.Connect_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Connect_btn.setStyleSheet(
            "color: rgb(85, 170, 255); background-color: rgb(206, 206, 206);"
        )
        self.Connect_btn.setDefault(False)
        self.Connect_btn.setFlat(False)
        self.Connect_btn.setObjectName("Connect_btn")
        self.gridLayout_3.addWidget(self.Connect_btn, 2, 3, 1, 1)
        self.Cache_label = QtWidgets.QLabel(self.MainWidget)
        self.Cache_label.setMinimumSize(QtCore.QSize(90, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Cache_label.setFont(font)
        self.Cache_label.setStyleSheet("color: rgb(85, 170, 255);")
        self.Cache_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cache_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cache_label.setLineWidth(3)
        self.Cache_label.setMidLineWidth(2)
        self.Cache_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cache_label.setObjectName("Cache_label")
        self.gridLayout_3.addWidget(self.Cache_label, 7, 1, 1, 1)
        self.GameIcon = QtWidgets.QRadioButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameIcon.sizePolicy().hasHeightForWidth())
        self.GameIcon.setSizePolicy(sizePolicy)
        self.GameIcon.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.GameIcon.setFont(font)
        self.GameIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GameIcon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameIcon.setAutoFillBackground(False)
        self.GameIcon.setStyleSheet("color: rgb(255, 255, 255);")
        self.GameIcon.setChecked(True)
        self.GameIcon.setObjectName("GameIcon")
        self.gridLayout_3.addWidget(self.GameIcon, 0, 1, 1, 2)
        self.ChangeAvatar = QtWidgets.QRadioButton(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChangeAvatar.sizePolicy().hasHeightForWidth())
        self.ChangeAvatar.setSizePolicy(sizePolicy)
        self.ChangeAvatar.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ChangeAvatar.setFont(font)
        self.ChangeAvatar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeAvatar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ChangeAvatar.setStyleSheet("color: rgb(255, 255, 255);")
        self.ChangeAvatar.setObjectName("ChangeAvatar")
        self.gridLayout_3.addWidget(self.ChangeAvatar, 2, 1, 1, 1)
        self.CacheBar = QtWidgets.QProgressBar(self.MainWidget)
        self.CacheBar.setMinimumSize(QtCore.QSize(100, 30))
        self.CacheBar.setProperty("value", 0)
        self.CacheBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CacheBar.setTextVisible(True)
        self.CacheBar.setOrientation(QtCore.Qt.Horizontal)
        self.CacheBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.CacheBar.setObjectName("CacheBar")
        self.gridLayout_3.addWidget(self.CacheBar, 7, 3, 1, 1)
        self.Change_label = QtWidgets.QLabel(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Change_label.sizePolicy().hasHeightForWidth())
        self.Change_label.setSizePolicy(sizePolicy)
        self.Change_label.setMinimumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Change_label.setFont(font)
        self.Change_label.setStyleSheet("color: rgb(85, 170, 255);")
        self.Change_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Change_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Change_label.setLineWidth(2)
        self.Change_label.setMidLineWidth(0)
        self.Change_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Change_label.setObjectName("Change_label")
        self.gridLayout_3.addWidget(self.Change_label, 0, 0, 5, 1)
        self.line = QtWidgets.QFrame(self.MainWidget)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 5, 0, 2, 6)
        self.FormLayout.setLayout(
            4, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_3
        )

        self.iconWS = QtWidgets.QLabel(self.MainWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iconWS.setFont(font)
        self.iconWS.setTextFormat(QtCore.Qt.AutoText)
        self.iconWS.setAlignment(QtCore.Qt.AlignCenter)
        self.iconWS.setOpenExternalLinks(True)
        self.iconWS.setObjectName("iconWS")
        self.FormLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.iconWS)

        self.PayPal = QtWidgets.QLabel(self.MainWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PayPal.setFont(font)
        self.PayPal.setTextFormat(QtCore.Qt.AutoText)
        self.PayPal.setAlignment(QtCore.Qt.AlignCenter)
        self.PayPal.setOpenExternalLinks(True)
        self.PayPal.setObjectName("PayPal")
        self.FormLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.PayPal)

        self.Credits = QtWidgets.QLabel(self.MainWidget)
        self.Credits.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(True)
        self.Credits.setFont(font)
        self.Credits.setStyleSheet("color: rgb(152, 255, 88);")
        self.Credits.setAlignment(QtCore.Qt.AlignCenter)
        self.Credits.setOpenExternalLinks(True)
        self.Credits.setObjectName("Credits")
        self.FormLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.Credits)

        self.gridLayout_2.addLayout(self.FormLayout, 0, 0, 1, 1)
        IPortWindow.setCentralWidget(self.MainWidget)
        self.menuBar = QtWidgets.QMenuBar(IPortWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        IPortWindow.setMenuBar(self.menuBar)
        self.Options = QtWidgets.QAction(IPortWindow)
        self.Options.setObjectName("Options")
        self.About = QtWidgets.QAction(IPortWindow)
        self.About.setObjectName("About")
        self.menuSettings.addAction(self.Options)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.About)
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.Connect_btn.clicked.connect(self.Check_IPort)
        self.Options.triggered.connect(self.OpenOptions)
        self.About.triggered.connect(self.about)

        self.retranslateUi(IPortWindow)
        QtCore.QMetaObject.connectSlotsByName(IPortWindow)

    def OpenOptions(self):
        import OptionsWin

        self.window = QtWidgets.QDialog()
        self.ui = OptionsWin.Ui_OptionsWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def about(self):
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        self.ui.setupUi(self.window, "About")
        self.window.show()

    def retranslateUi(self, IPortWindow):
        _translate = QtCore.QCoreApplication.translate
        IPortWindow.setWindowTitle(
            _translate(
                "IPortWindow",
                "Iconit v"
                + str(self.ver)
                + " ("
                + str(Update.get_update_release_date())
                + ")",
            )
        )

        self.Status.setText(_translate("IPortWindow", "Waiting connection..."))
        self.IP_Label.setText(_translate("IPortWindow", "PS4 IP"))
        self.IP_input.setPlaceholderText(_translate("IPortWindow", "Exp: 192.168.1.10"))
        self.Port_Label.setText(_translate("IPortWindow", "PS4 Port"))
        self.Port_input.setPlaceholderText(_translate("IPortWindow", self.userPort))
        self.Connect_btn.setText(_translate("IPortWindow", "Connect PS4"))
        self.Cache_label.setText(_translate("IPortWindow", "Caching"))
        self.GameIcon.setText(_translate("IPortWindow", "Game Icon / Game Pic"))
        self.ChangeAvatar.setText(_translate("IPortWindow", "Profile avatar"))
        self.Change_label.setText(_translate("IPortWindow", "Mode"))
        self.Credits.setText(
            _translate(
                "IPortWindow",
                '<html><head/><body><p align="center"><a href="https://twitter.com/OfficialAhmed0"><span style=" font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#98ff58; vertical-align:super;">Created By @OfficialAhmed0</span></a></p></body></html>',
            )
        )
        self.iconWS.setText(
            _translate(
                "IPortWindow",
                '<html><head/><body><p align="center"><a href="https://all-exhost.github.io/icon%20downloader.html"><span style=" font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#98ff58; vertical-align:super;">Download free icons</span></a></p></body></html>',
            )
        )
        self.PayPal.setText(
            _translate(
                "IPortWindow",
                '<html><head/><body><p align="center"><a href="https://www.paypal.com/paypalme/Officialahmed0"><span style=" font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#98ff58; vertical-align:super;">Donate (PayPal)</span></a></p></body></html>',
            )
        )
        self.Options.setText(_translate("IPortWindow", "Options..."))
        self.menuSettings.setTitle(_translate("IPortWindow", "Settings"))
        self.About.setText(_translate("IPortWindow", "About"))

        # Keyboard recognition v4.07
        self.Connect_btn.setShortcut("Return")

    def Check_IPort(self):
        global IP, Port
        try:
            IP = self.IP_input.text()
            Port = self.Port_input.text()

            valid = True
            for i in IP + str(Port):
                if i.isalpha():
                    valid = False
                    break

            self.Connect_PS4(valid)

        except Exception as e:
            self.logIt(str(e), "Warning")

    def ChangeColors(self, Connected):
        labels = (
            self.Status,
            self.IP_Label,
            self.Port_Label,
            self.Change_label,
            self.Cache_label,
        )
        if Connected:
            self.Status.setText("Connected")
        else:
            self.Status.setText("Not Connected")
        for l in labels:
            l.setStyleSheet("color: rgb(255, 0, 0);")
            if Connected:
                l.setStyleSheet("color: rgb(92, 213, 21);")

    # (ed0) Done
    def Connect_PS4(self, isvalid):
        global ftp, working_dir, IP, Port, local_path, all_CUSA, all_CUSA_ex, temp_path
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        if isvalid:
            try:
                # Delete old Cache
                try:
                    cache = os.listdir(temp_path + "MegaSRX\metadata")
                    for i in cache:
                        os.remove(temp_path + "MegaSRX\metadata\\" + str(i))
                except Exception as e:
                    print(str(e), ": Couldn't remove cache")

                # Iconit Or Profileit ?
                if self.GameIcon.isChecked() == True:  # Iconit
                    self.iconDirs = [working_dir]
                    ftp.set_debuglevel(0)
                    ftp.connect(IP, int(Port))
                    ftp.login("", "")
                    ftp.cwd("user/appmeta")
                    # look for external folder in appmeta
                    directories = []
                    ftp.retrlines("LIST ", directories.append)
                    for dir in directories:
                        if "external" in dir:
                            self.iconDirs.append(working_dir + "/external")
                            break

                    self.ChangeColors(True)
                    self.Connect_btn.setEnabled(False)
                    self.GameIcon.setEnabled(False)
                    self.ChangeAvatar.setEnabled(False)
                    for dir in self.iconDirs:
                        ftp.set_debuglevel(0)
                        ftp.connect(IP, int(Port))
                        ftp.login("", "")
                        try:
                            ftp.cwd(dir)
                        except Exception as e:
                            self.logIt(str(e), "Warning")
                        directories = []
                        ftp.retrlines("LIST ", directories.append)

                        game_ids = [line.split(" ")[-1] for line in directories]
                        all_Games = []

                        for game_id in game_ids:
                            if len(game_id) == len("CUSA00000"):
                                accept = True
                                if self.userHB != "True":
                                    # skip homebrews if turned off
                                    if "CUSA" not in game_id:
                                        accept = False

                                if accept:
                                    if "external" in dir:
                                        all_Games.append(game_id)
                                        all_CUSA_ex.append(game_id)
                                    else:
                                        all_Games.append(game_id)
                                        all_CUSA.append(game_id)

                    _thread.start_new_thread(self.CacheGameIcon())

                else:  # Profileit
                    self.sysProfileRoot = "system_data/priv/cache/profile/"
                    ftp.set_debuglevel(0)
                    ftp.connect(IP, int(Port))
                    ftp.login("", "")
                    ftp.cwd(self.sysProfileRoot)
                    self.userID = []

                    self.ChangeColors(True)

                    self.Connect_btn.setEnabled(False)
                    self.GameIcon.setEnabled(False)
                    self.ChangeAvatar.setEnabled(False)
                    directories = []
                    ftp.retrlines("LIST ", directories.append)

                    with open(
                        temp_path + "directories in system.dat", "w+"
                    ) as all_directories_in_system:
                        for line in directories:
                            all_directories_in_system.write(line + "\n")

                    with open(temp_path + "directories in system.dat") as file:
                        lines = file.readlines()
                        for line in lines:
                            if "0x" in line:
                                account_index = line.index("0x")
                                self.userID.append(line[account_index:-1])
                    self.CacheChangeAvatar()

            except Exception as e:
                self.logIt(str(e), "Error")
                self.ChangeColors(False)
                self.ui.setupUi(self.window, str(e))
                self.window.show()
        else:
            self.ChangeColors(False)
            self.ui.setupUi(self.window, "Invalid")
            self.window.show()

    def CacheChangeAvatar(self):
        fileName = "online.json"
        dir = temp_path + "MegaSRX\metaprodata\\"
        # Remove old data
        if len(os.listdir(dir)) != 0:
            data = os.listdir(dir)
            try:
                for i in data:
                    os.remove(dir + i)
            except Exception as e:
                self.logIt(str(e), "Warning")

        progress = int(100 / len(self.userID))
        progressed = 0
        self.CacheBar.setProperty("value", 1)

        for user in self.userID:
            ftp.set_debuglevel(0)
            ftp.connect(IP, int(Port))
            ftp.login("", "")
            ftp.cwd(self.sysProfileRoot + "/" + user)

            with open(dir + "\\" + user + ".png", "wb") as file:
                # cache avatar if available
                try:
                    ftp.retrbinary("RETR " + "avatar.png", file.write, 1024)
                except Exception as e:
                    self.logIt(str(e), "Warning")
            with open(dir + "\\" + user + ".json", "wb") as file:
                # Fix (v4.07) make a fake one if online json not found
                # fix (json not found) v4.51
                try:
                    ftp.retrbinary("RETR " + fileName, file.write, 1024)
                except Exception as e:
                    print(str(e))

                    import json

                    data = {
                        "avatarUrl": "http://static-resource.np.community.playstation.net/a/vatar_xl/WWS_E/E0012_XL.png",
                        "firstName": "Unknown",
                        "lastName": "username",
                        "pictureUrl": "https://image.api.np.km.playstation.net/images/?format=png&w=440&h=440&image=https%3A%2F%2Fkfscdn.api.np.km.playstation.net%2F00000000000008%2F000000000000003.png&sign=blablabla019501",
                        "trophySummary": '{"level":1,"progress":0,"earnedTrophies":{"platinum":0,"gold":0,"silver":0,"bronze":0}}',
                        "isOfficiallyVerified": "true",
                        "aboutMe": "Temporary file created by Iconit app by @OfficialAhmed0",
                    }

                    with open(dir + "\\" + user + ".json", "w+") as jsonFile:
                        json.dump(data, jsonFile)

                    with open(dir + "\\" + user + ".json", "rb") as json:
                        ftp.storbinary("STOR online.json", json, 1024)

            # Download original Profile Icon from Sony server
            import requests as req

            try:
                with open(dir + "\\" + user + ".json") as file:
                    # Extract Icon url from json file
                    read = file.read()
                    url = read[
                        read.find("avatarUrl")
                        + len("avatarUrl")
                        + 3 : read.find(".png")
                        + len(".png")
                    ]
                    cont = url.split("\/")
                    link = ""

                    for i in cont:
                        if i != "":
                            link += i + "//"
                    img = req.get(link[:-2])

                    with open(dir + "\\" + user + "Original.png", "wb") as origIcon:
                        origIcon.write(img.content)

            except Exception as e:
                self.logIt(str(e), "Warning")

            for i in range(1, progress):
                self.CacheBar.setProperty("value", progressed + i)

            progressed += progress

        self.CacheBar.setProperty("value", 100)
        self.OpenWindow("ChangeAvatar")

    def fetchIcon(self, current_CUSA, icon_name):
        # called by multiprocessing method
        with open(
            temp_path + "MegaSRX\metadata\\" + str(current_CUSA) + ".png",
            "wb",
        ) as downloaded_file:
            ftp.retrbinary("RETR " + icon_name, downloaded_file.write, 24)

    def CacheGameIcon(self):
        from xml.dom import minidom

        global all_CUSA, all_CUSA_ex, ftp, temp_path, working_dir, IP, Port, Game
        t1 = time.time()

        numGames = len(all_CUSA + all_CUSA_ex)
        # (FF) (go to 900)
        file_name = "pronunciation.xml"
        icon_name = "icon0.png"
        self.CacheBar.setProperty("value", 1)
        Eng1 = [chr(x) for x in range(ord("a"), ord("a") + 26)]  # a - z
        Eng2 = [chr(x) for x in range(ord("A"), ord("A") + 26)]  # A - Z
        Eng = Eng1 + Eng2
        Eng.append(" ")
        alphaNum = (
            "one",  # @
            "two",  # O
            "three",  # f
            "four",  # f
            "five",  # i
            "six",  # c
            "seven",  # i
            "eight",  # a
            "nine",  # l
            "™",  # A
            "'",  # h
            "!",  # m
            "?",  # ed0
        )

        for dir in self.iconDirs:
            ftp.set_debuglevel(0)
            ftp.connect(IP, int(Port))
            ftp.login("", "")
            ftp.cwd(dir)
            counter = 0

            if "external" in dir:
                currentDir = all_CUSA_ex
            else:
                currentDir = all_CUSA

            for i in currentDir:
                if counter == int(numGames / 2):
                    for i in range(25, 50):
                        self.CacheBar.setProperty("value", i)
                        time.sleep(0.00001)
                elif counter == int(numGames / 4):
                    for i in range(2, 25):
                        self.CacheBar.setProperty("value", i)
                        time.sleep(0.00001)
                elif counter == int(numGames / (75 / 100)):
                    for i in range(50, 75):
                        self.CacheBar.setProperty("value", i)
                        time.sleep(0.00001)
                ftp.cwd(currentDir[counter])

                files_in_dir = ftp.nlst()

                # Check for pronunciation.xml or icon0
                for content_in_file in files_in_dir:
                    if file_name in content_in_file or icon_name in content_in_file:
                        current_CUSA = currentDir[counter]

                        if file_name in content_in_file:
                            # Cache xml file
                            with open(temp_path + file_name, "wb") as downloaded_file:
                                ftp.retrbinary(
                                    "RETR " + file_name, downloaded_file.write, 1024
                                )

                            # cache icon0

                            # with open(
                            #     temp_path
                            #     + "MegaSRX\metadata\\"
                            #     + str(current_CUSA)
                            #     + ".png",
                            #     "wb",
                            # ) as downloaded_file:
                            #     ftp.retrbinary(
                            #         "RETR " + icon_name, downloaded_file.write, 1024
                            #     )

                            # MultiProccesing
                            pool = Pool(1)
                            pool.apply_async(
                                self.fetchIcon,
                                args=(current_CUSA, icon_name),
                            )

                            """
                            Algorithm implemented(v4.72)
                            fetch the best gameTitle for the current game [pronunciation.xml]

                            """
                            diff_titles = (
                                []
                            )  # all different titles for current fetched game
                            file = minidom.parse(
                                temp_path + file_name
                            ).getElementsByTagName("text")

                            for name in file:
                                diff_titles.append(name.firstChild.data)

                            GameTitle = ""
                            for title in diff_titles:
                                english = True

                                for alpha in alphaNum:
                                    if alpha in title or alpha.title() in title:
                                        GameTitle = title
                                        Game[current_CUSA] = GameTitle
                                    else:
                                        for char in title:
                                            if char not in Eng:
                                                english = False
                                                break
                                if english:
                                    GameTitle = title
                                    Game[current_CUSA] = GameTitle
                        else:
                            with open(
                                temp_path
                                + "MegaSRX\metadata\\"
                                + str(current_CUSA)
                                + ".png",
                                "wb",
                            ) as downloaded_file:
                                ftp.retrbinary(
                                    "RETR " + icon_name, downloaded_file.write, 1024
                                )
                            if "CUSA" in current_CUSA:
                                Game[current_CUSA] = "Unknown"
                            else:
                                Game[current_CUSA] = "Unknown Homebrew"

                if "external" in dir:
                    # Get back to root directory
                    ftp.set_debuglevel(0)
                    ftp.connect(IP, int(Port))
                    ftp.login("", "")
                    ftp.cwd(dir)
                else:
                    ftp.set_debuglevel(0)
                    ftp.connect(IP, int(Port))
                    ftp.login("", "")
                    ftp.cwd(working_dir)
                counter += 1

        for i in range(51, 100):
            self.CacheBar.setProperty("value", i)
            time.sleep(0.01)

        try:
            t2 = time.time()
            print((t2 - t1) / 60)
            self.OpenWindow("GameIcon")
        except Exception as e:
            print(str(e), "(O) go to line 700")

    def OpenWindow(self, WinType):
        if WinType == "GameIcon":
            global IP, Port, Game
            IPortWindow.hide()
            self.window = QtWidgets.QWidget()
            self.ui = ChangeIcon.Ui_ChangeIconWindow()
            self.ui.setupUi(
                self.window,
                IP,
                Port,
                Game,
                self.userFont,
                self.userIPath,
                self.userDPath,
                self.userHB,
                all_CUSA_ex,
                self.w,
                self.h,
            )
            self.window.show()
        else:
            IPortWindow.hide()
            self.window = QtWidgets.QWidget()
            self.ui = ChangeAvatar.Ui_ChangeAvatarWin()
            self.ui.setupUi(self.window, self.userID, IP, Port, self.w, self.h)
            self.window.show()

    def logIt(self, description, Type):
        import datetime

        try:
            error_file = open("Logs.txt", "a")
        except:
            error_file = open("Logs.txt", "w")
        if Type == "Warning":
            error_file.write(
                str(datetime.datetime.now())
                + " | "
                + "_DEV Warning: "
                + str(description)
                + "\n"
            )
        else:
            error_file.write(
                str(datetime.datetime.now())
                + " | "
                + "_DEV ERROR: "
                + str(description)
                + "\n"
            )  # (al) to 1


if __name__ == "__main__":
    import sys
    from func import playSound as play

    play(f"{local_path}/Data/Pref/bgm/home.mp3")

    app = QtWidgets.QApplication(sys.argv)
    screenResolution = app.desktop().screenGeometry()
    screenWidth, screenHeight = screenResolution.width(), screenResolution.height()
    IPortWindow = QtWidgets.QMainWindow()
    ui = Ui_IPortWindow()  # (ici) line 890
    ui.setupUi(IPortWindow, screenWidth, screenHeight)
    IPortWindow.show()
    sys.exit(app.exec_())