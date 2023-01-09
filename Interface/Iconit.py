from environment import html
from Module.Iconit import Main as Iconit

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui(Iconit):
    def __init__(self) -> None:
        super().__init__()
        
    def setupUi(self, window):
        self.local_path = self.local_path

        self.html = html()

        # init user prefrences & settings
        settings_elems = [
            self.userFont,
            self.userPort,
            self.userIp,
            self.userIPath,
            self.userDPath,
            self.userHB
        ]
        user_setting_cache = self.settings.get_cache()
        for indx, val in enumerate(user_setting_cache):
            settings_elems[indx] = val

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

        # Keyboard shortcuts v4.07
        self.Connect_btn.setShortcut("Return")

        # Autofill cached IP & port
        self.connection_history(mode="r")
