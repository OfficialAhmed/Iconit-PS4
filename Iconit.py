import os
import json

# from ftplib import FTP
from PyQt5 import QtCore, QtGui, QtWidgets

# Custom mod.
import ChangeAvatar
import ChangeIcon
import Message
import func
from environment import Environment
from environment import html

from xml.dom import minidom  # XML parsing

class Ui(Environment):
    def __init__(self) -> None:
        super().__init__()
        
    def setupUi(self, window):
        self.local_path = self.local_path

        #######################################################
        #####
        #####  Settings
        #####
        #######################################################
        self.html = html.html()
        self.logs = func.logs

        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIp = ""
        self.userIPath = self.local_path
        self.userDPath = self.local_path
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
            self.logs(str(e), "Warning")

        #############################################################
        #####
        #####  Data used to determine the best Game Title possible
        #####
        ############################################################

        self.file_name = "pronunciation.xml"
        self.icon_name = "icon0.png"
        self.Eng1 = [chr(x) for x in range(ord("a"), ord("a") + 26)]  # a - z
        self.Eng2 = [chr(x) for x in range(ord("A"), ord("A") + 26)]  # A - Z
        self.Eng = self.Eng1 + self.Eng2
        self.Eng.append(" ")
        self.alphaNum = (
            "one", 
            "two", 
            "three",
            "four", 
            "five", 
            "six", 
            "seven",
            "eight",
            "nine",
            "™",
            "'",
            "!",
            "?",
        )

        self.modeSelected = ""
        self.cached = ""
       
        ######################################################
        #####
        #####           GUI and Signals
        #####           Starting point
        #####
        ######################################################

        font = QtGui.QFont()
        font.setFamily(self.userFont)
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)

        # v4.05 new UI support 2k, 4k res
        window.setObjectName("window")
        window.setWindowModality(QtCore.Qt.WindowModal)

        window.resize(720, 521)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        window.setMinimumSize(QtCore.QSize(720, 512))
        window.setWindowOpacity(1.0)
        window.setStyleSheet("")
        window.setDocumentMode(False)
        window.setTabShape(QtWidgets.QTabWidget.Rounded)
        window.setObjectName("window")
        window.resize(701, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        window.setMinimumSize(QtCore.QSize(701, 620))

        ######################################################
        #####           Background Design
        ######################################################
        self.mainWidget = QtWidgets.QWidget(window)
        self.mainWidget.setStyleSheet(
            "QWidget#mainWidget{\n"
            "background-image: url(Data//Pref//IPortWinbg.@OfficialAhmed0);\n"
            "background-size:  cover;               \n"
            "background-repeat:   no-repeat;\n"
            "background-position: center center;        \n"
            "\n"
            "}"
        )
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TitleLabel_withURL = QtWidgets.QLabel(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel_withURL.sizePolicy().hasHeightForWidth())
        self.TitleLabel_withURL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.TitleLabel_withURL.setFont(font)
        self.TitleLabel_withURL.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TitleLabel_withURL.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel_withURL.setOpenExternalLinks(True)
        self.TitleLabel_withURL.setObjectName("TitleLabel_withURL")
        self.verticalLayout_5.addWidget(self.TitleLabel_withURL)
        self.widgetWithRadius = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetWithRadius.sizePolicy().hasHeightForWidth())
        self.widgetWithRadius.setSizePolicy(sizePolicy)
        self.widgetWithRadius.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.widgetWithRadius.setStyleSheet(
            "QWidget#widgetWithRadius{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(124, 57, 191, 120), stop:1 rgba(42, 44, 89, 220));\n"
            "border-radius: 80px;\n"
            "}"
        )
        self.widgetWithRadius.setObjectName("widgetWithRadius")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widgetWithRadius)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Status = QtWidgets.QLabel(self.widgetWithRadius)
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")
        self.verticalLayout_6.addWidget(self.Status)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.SystemIcon = QtWidgets.QRadioButton(self.widgetWithRadius)

        ######################################################
        #####           Labels and inputs
        ######################################################
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.SystemIcon.setFont(font)
        self.SystemIcon.setStyleSheet("color: rgb(255, 255, 255);")
        self.SystemIcon.setObjectName("SystemIcon")
        self.gridLayout.addWidget(self.SystemIcon, 10, 2, 1, 1)
        self.Port_Label = QtWidgets.QLabel(self.widgetWithRadius)
        self.Port_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_Label.setObjectName("Port_Label")
        self.gridLayout.addWidget(self.Port_Label, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.GameIcon = QtWidgets.QRadioButton(self.widgetWithRadius)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.GameIcon.setFont(font)
        self.GameIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GameIcon.setStyleSheet("color: rgb(255, 255, 255);")
        self.GameIcon.setChecked(True)
        self.GameIcon.setObjectName("GameIcon")
        self.gridLayout.addWidget(self.GameIcon, 8, 2, 1, 1)
        self.Port_input = QtWidgets.QLineEdit(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Port_input.sizePolicy().hasHeightForWidth())
        self.Port_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        self.Port_input.setFont(font)
        self.Port_input.setStyleSheet("border-radius: 10px;")
        self.Port_input.setText(self.userPort)
        self.Port_input.setMaxLength(6)
        self.Port_input.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_input.setObjectName("Port_input")
        self.gridLayout.addWidget(self.Port_input, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.SysIcon_Note = QtWidgets.QLabel(self.widgetWithRadius)
        self.SysIcon_Note.setObjectName("SysIcon_Note")
        self.gridLayout.addWidget(self.SysIcon_Note, 11, 2, 1, 1)
        self.IP_input = QtWidgets.QLineEdit(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_input.sizePolicy().hasHeightForWidth())
        self.IP_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        self.IP_input.setFont(font)
        self.IP_input.setStyleSheet("border-radius: 10px;")
        self.IP_input.setText(self.userIp)
        self.IP_input.setMaxLength(16)
        self.IP_input.setAlignment(QtCore.Qt.AlignCenter)
        self.IP_input.setClearButtonEnabled(True)
        self.IP_input.setObjectName("IP_input")
        self.gridLayout.addWidget(self.IP_input, 2, 2, 1, 1)
        self.Change_label = QtWidgets.QLabel(self.widgetWithRadius)
        self.Change_label.setObjectName("Change_label")
        self.gridLayout.addWidget(self.Change_label, 10, 1, 1, 1)
        self.IP_Label = QtWidgets.QLabel(self.widgetWithRadius)
        self.IP_Label.setObjectName("IP_Label")
        self.gridLayout.addWidget(self.IP_Label, 2, 1, 1, 1)
        self.ChangeAvatar = QtWidgets.QRadioButton(self.widgetWithRadius)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ChangeAvatar.setFont(font)
        self.ChangeAvatar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeAvatar.setStyleSheet("color: rgb(255, 255, 255);")
        self.ChangeAvatar.setObjectName("ChangeAvatar")
        self.gridLayout.addWidget(self.ChangeAvatar, 12, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.GameIcon_Note = QtWidgets.QLabel(self.widgetWithRadius)
        self.GameIcon_Note.setAlignment(QtCore.Qt.AlignCenter)
        self.GameIcon_Note.setObjectName("GameIcon_Note")
        self.gridLayout.addWidget(self.GameIcon_Note, 9, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        ######################################################
        #####           Custom progressBar
        ######################################################
        self.CacheBar = QtWidgets.QProgressBar(self.widgetWithRadius)
        self.CacheBar.setStyleSheet(
            """QProgressBar {
            border-radius: 10px;
            color:rgb(255, 255, 255);
            }
            QProgressBar::chunk {
            background: QLinearGradient( x1:0.358, y1:0.602182, x2:0.960318, y2:0.648, stop:0 rgb(124, 57, 191), stop:0.903409 rgb(242, 80, 231));
            border-radius: 10px;
            };
            """
        )
        self.CacheBar.setProperty("value", 0)
        self.CacheBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CacheBar.setTextVisible(True)
        self.CacheBar.setObjectName("CacheBar")
        self.gridLayout_2.addWidget(self.CacheBar, 4, 2, 1, 1)
        self.Cache_label = QtWidgets.QLabel(self.widgetWithRadius)
        self.Cache_label.setObjectName("Cache_label")
        self.gridLayout_2.addWidget(self.Cache_label, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widgetWithRadius)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 7, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 2, 1, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 0, 1, 1)
        self.Credits = QtWidgets.QLabel(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Credits.sizePolicy().hasHeightForWidth())
        self.Credits.setSizePolicy(sizePolicy)
        self.Credits.setAlignment(QtCore.Qt.AlignCenter)
        self.Credits.setOpenExternalLinks(True)
        self.Credits.setObjectName("Credits")
        self.gridLayout_2.addWidget(self.Credits, 6, 2, 1, 1)
        self.Connect_btn = QtWidgets.QPushButton(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Connect_btn.sizePolicy().hasHeightForWidth())
        self.Connect_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Connect_btn.setFont(font)
        self.Connect_btn.setStyleSheet("color: rgb(42, 44, 89);")
        self.Connect_btn.setCheckable(False)
        self.Connect_btn.setFlat(False)
        self.Connect_btn.setObjectName("Connect_btn")
        self.gridLayout_2.addWidget(self.Connect_btn, 2, 2, 2, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 5, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widgetWithRadius)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 8, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.verticalLayout_5.addWidget(self.widgetWithRadius)

        ######################################################
        #####           The Menu/Settings hierarchy
        ######################################################
        window.setCentralWidget(self.mainWidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        window.setMenuBar(self.menubar)
        self.Options = QtWidgets.QAction(window)
        self.Options.setObjectName("Options")
        self.actionAbout = QtWidgets.QAction(window)
        self.actionAbout.setObjectName("actionAbout")
        self.About = QtWidgets.QAction(window)
        self.About.setObjectName("About")
        self.actionRemove_cache = QtWidgets.QAction(window)
        self.actionRemove_cache.setObjectName("actionAbout")
        self.Remove_cache = QtWidgets.QAction(window)
        self.Remove_cache.setObjectName("Remove_cache")
        self.Special_thanks = QtWidgets.QAction(window)
        self.Special_thanks.setObjectName("Special_thanks")
        self.menuSettings.addAction(self.Options)
        self.menuSettings.addAction(self.Remove_cache)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.About)
        self.menuSettings.addAction(self.Special_thanks)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(window)

        ######################################################
        #####           Slots and Signals
        ######################################################
        self.GameIcon.toggled["bool"].connect(self.GameIcon_Note.setVisible)
        self.SystemIcon.toggled["bool"].connect(self.SysIcon_Note.setVisible)
        self.ChangeAvatar.toggled["bool"].connect(self.SysIcon_Note.hide)
        self.ChangeAvatar.toggled["bool"].connect(self.GameIcon_Note.hide)
        QtCore.QMetaObject.connectSlotsByName(window)

        self.Connect_btn.clicked.connect(self.Check_IPort)
        self.Options.triggered.connect(self.open_options)
        self.About.triggered.connect(self.about)

        self.Special_thanks.triggered.connect(self.thanks_2)
        self.Remove_cache.triggered.connect(self.remove_cache)

    def open_options(self):
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

    def thanks_2(self):
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        self.ui.setupUi(self.window, "CUSTOMspecial_thanks")
        self.window.show()

    def remove_cache(self):
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        cache_dir = "Data\prxUserMeta\MegaSRX\metadata\game"
        all = os.listdir(cache_dir)
        try:
            for i in all:
                os.remove(cache_dir + "\\" + i)
            self.ui.setupUi(self.window, "CUSTOMdoneRmvCache")
        except:
            self.ui.setupUi(self.window, "PermissionDenied")
        self.window.show()

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", f"Iconit v{self.get_update_version()} ({self.get_update_release_date()})"))
        self.TitleLabel_withURL.setText(_translate("window", self.html.a_tag("https://github.com/OfficialAhmed/Iconit-PS4/releases", f"Iconit v{self.get_update_version()}", "#f250e7", 18),))
        self.Status.setText(_translate("window", self.html.span_tag("Awaiting Connection ..", "#f2ae30", 18)))
        self.SystemIcon.setText(_translate("window", "System Icons"))
        self.Port_Label.setText( _translate( "window", self.html.span_tag("PS4 Port", "#f2ae30", 16)))
        self.GameIcon.setText(_translate("window", "Game Icon/Pic"))
        self.Port_input.setText(_translate("window", self.userPort))
        self.SysIcon_Note.setText(_translate("window", self.html.span_tag("Note: Full R/W permissions required ( PS4 Xplorer FTP by enabling danger mode)", "#f2ae30", 8),))
        self.IP_input.setPlaceholderText(_translate("window", "192.168.XXX.XXX"))
        self.Change_label.setText(_translate("window", self.html.span_tag("MODE", "#f2ae30", 16)))
        self.IP_Label.setText(_translate("window", self.html.span_tag("PS4 IP", "#f2ae30", 16)))
        self.ChangeAvatar.setText(_translate("window", "Profile Avatar"))
        self.GameIcon_Note.setText(_translate("window", self.html.span_tag("Note: You can enable Homebrew icons in the settings before connecting to the PS4", "#f2ae30", 8)))
        self.Cache_label.setText(_translate("window", self.html.span_tag("Cache", "#f2ae30", 10)))
        self.label.setText(_translate("MainWindow", self.html.a_tag("https://www.paypal.com/paypalme/Officialahmed0", "Donate (PayPal)", "#f250e7", 8, "font-style:italic")))
        self.Credits.setText(_translate("MainWindow", self.html.a_tag("https://all-exhost.github.io/Icons.html", "Download Free Icons", "#f250e7", 8)))
        self.label_2.setText(_translate("MainWindow", self.html.a_tag("https://twitter.com/OfficialAhmed0", "Created by @OfficialAhmed0", "#f250e7", 8, "font-style:italic")))

        self.Connect_btn.setText(_translate("window", "Connect PS4"))
        self.menuSettings.setTitle(_translate("window", "Settings"))
        self.Options.setText(_translate("window", "Options..."))
        self.actionAbout.setText(_translate("window", "About"))
        self.About.setText(_translate("window", "About"))
        self.Remove_cache.setText(_translate("window", "Remove cache"))
        self.Special_thanks.setText(_translate("window", "Special thanks"))

        # Keyboard recognition v4.07
        self.Connect_btn.setShortcut("Return")

        # Auto write used IP & port
        self.connection_history(mode="r")

    def Check_IPort(self):
        self.Status.setText(self.html.span_tag("Connecting...", "#f2ae30", 18))
        try:
            self.IP = self.IP_input.text()
            self.Port = self.Port_input.text()
            self.connection_history(mode="w")

            if len(self.IP) < 8:
                self.Connect_PS4(False)
            else:
                valid = True
                for i in self.IP + str(self.Port):
                    if i.isalpha():
                        valid = False
                        break
                self.Connect_PS4(valid)
        except Exception as e:
            self.logs(str(e), "Warning")

    def change_colors(self, Connected):
        labels = {
            self.IP_Label: "PS4 IP",
            self.Port_Label: "PS4 Port",
            self.Change_label: "Mode",
            self.Cache_label: "Cache",
        }
        if Connected:
            self.Status.setText(self.html.span_tag("Connected", "rgb(92, 213, 21)", 18))
        else:
            self.Status.setText(self.html.span_tag("Failed to connect", "rgb(255, 0, 0)", 18))
        for l in labels:
            l.setText(self.html.span_tag(labels[l], "rgb(255, 0, 0)", 16))
            if Connected:
                l.setText(self.html.span_tag(labels[l], "color:rgb(92, 213, 21)", 16))

    def connection_history(self, mode: str) -> None:
        ################################################################
        ###               Store IP and Port for next session
        ################################################################
        file_name = "connection_history.dat"
        if mode == "r":
            try:
                with open(f"{self.temp_path}\{file_name}", "r") as file:
                    line = file.readline().strip()
                    ip, port = line.split(",")
                    self.IP_input.setText(ip)
                    self.Port_input.setText(port)

            except Exception as e:
                self.logs(str(e), "Warning")
        else:
            with open(f"{self.temp_path}\{file_name}", "w+") as file:
                ip = self.IP_input.text()
                port = self.Port_input.text()
                file.write(f"{ip},{port}")

    def Connect_PS4(self, isvalid):
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()

        if isvalid:
            """
                    Naive Approach  ;)
                Solution for one connection only (GoldHen FTP)
                *Try to connect, otherwise, try to close the connection might not been closed properly before.
                *Never close connection until we move to the next window
                *Avoid reconnceting to step back to root dir, Change dir manually (/)
            """
            try:
                self.ftp.set_debuglevel(0)
                self.ftp.connect(self.IP, int(self.Port))
                self.ftp.login("", "")
                self.ftp.getwelcome()
            except ConnectionRefusedError:
                self.change_colors(False)
                self.ui.setupUi(
                    self.window,
                    "Cannot make connection with the given IP/Port. DEV| ConnectionRefusedError",
                )
                self.window.show()
                return
            except Exception as e:
                self.ftp.close()
                self.logs(e, "Error")
                self.change_colors(False)
                self.ui.setupUi(
                    self.window,
                    "Cannot make connection with the given IP/Port. DEV|" + str(e),
                )
                self.window.show()
                return

            ##############################################
            ###       User Picked Game Icon
            ###############################################
            self.Status.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
            if self.GameIcon.isChecked():
                # v4.72 json for caching
                jsonPath = "Data\prxUserMeta\MegaSRX\metadata\game\info.json"
                if os.path.isfile(jsonPath):
                    ReadJson = open(jsonPath)
                    Game = json.load(ReadJson)

                self.modeSelected = "game"
                self.iconDirs = [self.working_dir]
                self.ftp.cwd("/")
                self.ftp.cwd("user/appmeta")

                directories = []
                self.ftp.retrlines("LIST ", directories.append)
                for dir in directories:
                    if "external" in dir:
                        self.iconDirs.append(self.working_dir + "/external")
                        break
                self.change_colors(True)
                self.Connect_btn.setEnabled(False)
                self.GameIcon.setEnabled(False)
                self.ChangeAvatar.setEnabled(False)

                for dir in self.iconDirs:
                    self.ftp.cwd("/")
                    try:
                        self.ftp.cwd(dir)
                    except Exception as e:
                        self.logs(str(e), "Warning")
                    directories = []
                    self.ftp.retrlines("LIST ", directories.append)

                    game_ids = [line.split(" ")[-1] for line in directories]
                    all_Games = []

                    for game_id in game_ids:
                        if len(game_id) == len("CUSA00000"):
                            accept = True

                            """
                            If HB is on
                            check each game id for CUSA or NPXS(sys icons) only
                            """
                            if self.userHB != "True":
                                if "CUSA" not in game_id:
                                    accept = False
                                    try:
                                        Game.pop(game_id)
                                    except:
                                        pass

                            if accept:
                                if "external" in dir:
                                    all_Games.append(game_id)
                                    self.all_CUSA_sys.append(game_id)
                                else:
                                    all_Games.append(game_id)
                                    self.all_CUSA.append(game_id)
                self.cache_game_icon()

            ##############################################
            ###       User picked Sys icons
            ###############################################
            elif self.SystemIcon.isChecked():
                self.ftp.cwd("/")
                self.ftp.cwd(self.sys_path)

                sys_files = self.listDirs()

                self.change_colors(True)
                self.Connect_btn.setEnabled(False)
                self.GameIcon.setEnabled(False)
                self.ChangeAvatar.setEnabled(False)

                for sys_game in sys_files:
                    if len(sys_game) == len("CUSA00000"):
                        self.ftp.cwd(sys_game)
                        folders_inside = self.listDirs()
                        if "sce_sys" in folders_inside:
                            self.ftp.cwd("sce_sys")
                            files_inside = self.listDirs()
                            if "icon0.png" in files_inside:
                                self.all_CUSA_sys.append(sys_game)

                    self.ftp.cwd("/")
                    self.ftp.cwd(self.sys_path)

                self.CacheSysIcon()
            ##############################################
            ###       User picked Avatar change
            ###############################################
            else:
                self.sysProfileRoot = "system_data/priv/cache/profile/"
                self.ftp.cwd("/")
                self.ftp.cwd(self.sysProfileRoot)
                self.userID = []

                self.change_colors(True)

                self.Connect_btn.setEnabled(False)
                self.GameIcon.setEnabled(False)
                self.ChangeAvatar.setEnabled(False)
                directories = []
                self.ftp.retrlines("LIST ", directories.append)

                with open(
                    self.temp_path + "directories in system.dat", "w+"
                ) as all_directories_in_system:
                    for line in directories:
                        all_directories_in_system.write(line + "\n")

                with open(self.temp_path + "directories in system.dat") as file:
                    lines = file.readlines()
                    for line in lines:
                        if "0x" in line:
                            account_index = line.index("0x")
                            self.userID.append(line[account_index:-1])
                self.cache_change_avatar()
        else:
            self.change_colors(False)
            self.ui.setupUi(
                self.window,
                "Double check PS4 IP and Port\n Note: If you're using GoldHen FTP\n make sure you're not connected to the PS4 with a different app as it only allow one connection",
            )
            self.window.show()

    def cache_change_avatar(self):
        ###############################################
        #            Prepare Avatars
        ################################################

        fileName = "online.json"
        dir = self.temp_path + "MegaSRX\metaprodata\\"
        # Remove old data
        if len(os.listdir(dir)) != 0:
            data = os.listdir(dir)
            try:
                for i in data:
                    os.remove(dir + i)
            except Exception as e:
                self.logs(str(e), "Warning")

        progress = int(100 / len(self.userID))
        progressed = 0
        self.CacheBar.setProperty("value", 1)

        for user in self.userID:
            self.ftp.cwd("/")
            self.ftp.cwd(self.sysProfileRoot + "/" + user)

            with open(dir + "\\" + user + ".png", "wb") as file:
                # cache avatar if available
                try:
                    self.ftp.retrbinary("RETR " + "avatar.png", file.write, 1024)
                except Exception as e:
                    self.logs(str(e), "Warning")
            with open(dir + "\\" + user + ".json", "wb") as file:
                # Fix (v4.07) make a fake one if online json not found
                # fix (json not found) v4.51
                try:
                    self.ftp.retrbinary("RETR " + fileName, file.write, 1024)
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
                        json.dump(data, jsonFile, indent=4)

                    with open(dir + "\\" + user + ".json", "rb") as json:
                        self.ftp.storbinary("STOR online.json", json, 1024)

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
                self.logs(str(e), "Warning")

            for i in range(1, progress):
                self.CacheBar.setProperty("value", progressed + i)

            progressed += progress

        self.CacheBar.setProperty("value", 100)
        self.OpenWindow("ChangeAvatar")

    def CacheSysIcon(self):

        ###############################################
        #            Sys Icons impl v4.72
        ################################################

        global all_CUSA_sys
        GameWeightInFraction = (1 / len(all_CUSA_sys)) * 100
        percentage = 0
        self.ftp.set_debuglevel(0)
        self.ftp.cwd("/")
        self.ftp.cwd(self.sys_path)

        for sysIcon in all_CUSA_sys:
            self.ftp.cwd(sysIcon + "/sce_sys")
            inside_sce_sys = self.listDirs()
            icon_2_fetch = "icon0.png"

            # fetch 4k version if found
            if "icon0_4k.png" in inside_sce_sys:
                icon_2_fetch = "icon0_4k.png"

            self.fetchData(
                icon_2_fetch,
                f"{self.temp_path}MegaSRX\metadata\\{sysIcon}.png",
            )
            if self.file_name in inside_sce_sys:
                self.fetchData(self.file_name, self.temp_path + self.file_name)

                diff_titles = []  # all different titles for current fetched game
                file = minidom.parse(self.temp_path + self.file_name).getElementsByTagName(
                    "text"
                )

                for name in file:
                    diff_titles.append(name.firstChild.data)

                GameTitle = ""
                for title in diff_titles:
                    english = True

                    for alpha in self.alphaNum:
                        if alpha in title or alpha.title() in title:
                            GameTitle = title
                            Game[sysIcon] = GameTitle
                        else:
                            for char in title:
                                if char not in self.Eng:
                                    english = False
                                    break
                    if english:
                        GameTitle = title
                        Game[sysIcon] = GameTitle
            else:
                if "NPXS" in sysIcon:
                    Game[sysIcon] = 'Unknown system icon "Sony didn\'t provide one :)"'
                else:
                    Game[sysIcon] = f"Cannot find title for {sysIcon}"

            self.ftp.cwd("/")
            self.ftp.cwd(self.sys_path)
            percentage += GameWeightInFraction
            self.CacheBar.setProperty(
                "value", str(percentage)[: str(percentage).index(".")]
            )

        try:
            self.OpenWindow("GameIcon")
        except Exception as e:
            print(str(e), "(O) go to line 700")

    def cache_game_icon(self):
        ################################################
        #   Internal/External HDD Game Icons
        ################################################

        try:
            self.cached = os.listdir(f"{self.temp_path}MegaSRX\metadata\\game")
            numGames = len(self.all_CUSA + self.all_CUSA_sys)
            GameWeightInFraction = (1 / numGames) * 100
            percentage = 0

            for dir in self.iconDirs:
                self.ftp.cwd("/")
                self.ftp.cwd(dir)
                counter = 0

                if "external" in dir:
                    currentDir = self.all_CUSA_sys
                else:
                    currentDir = self.all_CUSA

                for i in currentDir:
                    self.ftp.cwd(i)
                    gameId = currentDir[counter]

                    if gameId not in Game:
                        ######################################################
                        ###  Fetch icons only if its not it the cache => info.json
                        ###  impl. v4.72
                        ######################################################

                        files_in_dir = self.listDirs()

                        for content_in_file in files_in_dir:
                            if (
                                self.file_name in content_in_file
                                or self.icon_name in content_in_file
                            ):
                                if self.file_name in content_in_file:
                                    self.fetchData(
                                        self.file_name, self.temp_path + self.file_name
                                    )
                                if self.icon_name in content_in_file:
                                    self.fetchData(
                                        self.icon_name,
                                        f"{self.temp_path}MegaSRX\metadata\\game\\{gameId}.png",
                                    )
                                diff_titles = (
                                    []
                                )  # all different titles for current fetched game
                                try:
                                    file = minidom.parse(
                                        self.temp_path + self.file_name
                                    ).getElementsByTagName("text")

                                    for name in file:
                                        diff_titles.append(name.firstChild.data)
                                except Exception as e:
                                        diff_titles.append("UNKNOWN TITLE")

                                GameTitle = ""
                                for title in diff_titles:
                                    if self.file_name in files_in_dir:
                                        GameTitle = title
                                        Game[gameId] = GameTitle
                                    else:
                                        GameTitle = "Unknown"
                                        Game[gameId] = GameTitle
                                        break
                                    english = True

                                    for char in title:
                                        if char not in self.Eng:
                                            english = False
                                            break
                                    if english:
                                        GameTitle = title
                                        Game[gameId] = GameTitle
                                        break

                    # Get back to root directory
                    self.ftp.cwd("/")

                    if "external" in dir:
                        self.ftp.cwd(dir)
                    else:
                        self.ftp.cwd(self.working_dir)
                    counter += 1
                    percentage += GameWeightInFraction
                    self.CacheBar.setProperty(
                        "value", str(percentage)[: str(percentage).index(".")]
                    )
            try:
                self.OpenWindow("GameIcon")
            except Exception as e:
                print(str(e))
        except Exception as e:
            self.logs(e, "Error")
            self.change_colors(False)
            self.ui.setupUi(self.window, str(e))
            self.window.show()

    def listDirs(self):
        ######################################################
        ##     Equevalent of nlst() method
        ##     PS4 FTP doesn't support nlst             impl. v4.72
        ######################################################

        dir_with_info = []
        self.ftp.retrlines("LIST ", dir_with_info.append)

        directories = [x.split(" ")[-1] for x in dir_with_info]
        return directories

    def fetchData(self, file_name, file_path_with_extension):
        self.Status.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
        with open(
            file_path_with_extension,
            "wb",
        ) as downloaded_file:
            self.ftp.retrbinary("RETR " + file_name, downloaded_file.write)

    def OpenWindow(self, WinType):
        global Game
        sorted_Games = {k: v for k, v in sorted(Game.items(), key=lambda item: item[1])}
        self.ftp.close()

        if WinType == "GameIcon":
            # store games in json for cache if not IconSys
            if len(self.all_CUSA_sys) == 0:
                with open(
                    "Data\prxUserMeta\MegaSRX\metadata\game\info.json", "w+"
                ) as jsonFile:
                    json.dump(sorted_Games, jsonFile)

            # window.hide()
            self.window = QtWidgets.QWidget()
            self.ui = ChangeIcon.Ui_ChangeIconWindow()
            self.ui.setupUi(
                self.window,
                sorted_Games,
                self.userFont,
                self.userIPath,
                self.userDPath,
                self.userHB,
                self.modeSelected,
            )
            self.window.show()
        else:
            # window.hide()
            self.window = QtWidgets.QWidget()
            self.ui = ChangeAvatar.Ui_ChangeAvatarWin()
            self.ui.setupUi(self.window, self.userID, self.IP, self.Port, self.w, self.h)
            self.window.show()

