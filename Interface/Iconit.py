from environment import html
from Module.Iconit import Main as Iconit

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui(Iconit):
    def __init__(self) -> None:
        super().__init__()
        
    def setupUi(self, window):
        self.html = html()

        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setPointSize(13)
        font.setFamily(self.userFont)

        pointing_hand_cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)

        # ______________   WINDOW SPECS   _____________________ #
        window.setWindowTitle(f"Iconit v{self.get_update_version()} ({self.get_update_release_date()})")

        window.resize(720, 620)
        window.setMinimumSize(QtCore.QSize(720, 620))
        window.setWindowModality(QtCore.Qt.WindowModal)
        window.setTabShape(QtWidgets.QTabWidget.Rounded)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)

        self.mainWidget = QtWidgets.QWidget(window)
        bg_path = self.pref_path.replace('\\', '/')
        self.mainWidget.setObjectName("mainWidget")
        self.mainWidget.setStyleSheet(
            f"""
            QWidget#mainWidget{'{'}
            background-image: url({bg_path}MainBG.@OfficialAhmed0);
            background-size: cover; 
            background-repeat: no-repeat; 
            background-position: center;
            {'}'}
            """
        )

        # ______________   LABELS   _____________________ #
        font.setPointSize(22)
        font.setItalic(False)

        self.TransparentLayer = QtWidgets.QWidget(self.mainWidget)
        self.TransparentLayer.setObjectName("TransparentLayer")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.TransparentLayer.sizePolicy().hasHeightForWidth())
        self.TransparentLayer.setSizePolicy(sizePolicy)
        self.TransparentLayer.setStyleSheet(
            f"""
            QWidget#TransparentLayer{'{'}
            border-radius: 100px;
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 rgba(124, 57, 191, 120), 
                stop:1 rgba(42, 44, 89, 220)
            );
            {'}'}
            """
        )
        self.IpLabel = QtWidgets.QLabel(self.TransparentLayer)
        self.ModeLabel = QtWidgets.QLabel(self.TransparentLayer)
        self.PortLabel = QtWidgets.QLabel(self.TransparentLayer)
        self.CacheLabel = QtWidgets.QLabel(self.TransparentLayer)
        self.StatusLabel = QtWidgets.QLabel(self.TransparentLayer)

        # ______________   BUTTONS   _____________________ #
        font.setPointSize(14)
        font.setItalic(True)

        self.ConnectBtn = QtWidgets.QPushButton(self.TransparentLayer)
        self.GameIconsRadio = QtWidgets.QRadioButton(self.TransparentLayer)
        self.SystemIconsRadio = QtWidgets.QRadioButton(self.TransparentLayer)
        self.AvatarIconsRadio = QtWidgets.QRadioButton(self.TransparentLayer)

        btns = (
            self.GameIconsRadio, 
            self.SystemIconsRadio, 
            self.AvatarIconsRadio, 
            self.ConnectBtn
        )
        
        for btn in btns:
            btn.setFont(font)
            btn.setCursor(pointing_hand_cursor)
            btn.setStyleSheet("color: rgb(255, 255, 255);")

        font.setBold(True)
        font.setItalic(False)
        font.setPointSize(13)
        self.ConnectBtn.setFont(font)
        self.ConnectBtn.setStyleSheet("color: rgb(0, 0, 0);")
        self.GameIconsRadio.setChecked(True)

        # ______________   INPUTS   _____________________ #
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)

        self.PortInput = QtWidgets.QLineEdit(self.TransparentLayer)
        self.IpInput = QtWidgets.QLineEdit(self.TransparentLayer)
        inputs = (self.IpInput, self.PortInput)

        for input in inputs:
            input.setFont(font)
            input.setMaxLength(16)
            input.setText(self.userPort)
            input.setSizePolicy(sizePolicy)
            input.setClearButtonEnabled(True)
            input.setAlignment(QtCore.Qt.AlignCenter)
            input.setStyleSheet("border-radius: 10px;")

        # ______________   DESCRIPTION   _____________________ #
        self.SysIconsInfo = QtWidgets.QLabel(self.TransparentLayer)
        self.GameIconsInfo = QtWidgets.QLabel(self.TransparentLayer)

        # ______________   CUSTOM PROGRESS BAR   _____________________ #
        self.CacheBar = QtWidgets.QProgressBar(self.TransparentLayer)
        self.CacheBar.setStyleSheet(
            f"""
                QProgressBar{'{'}
                    border-radius: 10px;
                    color:rgb(255, 255, 255)
                {'}'}
                QProgressBar::chunk{'{'}
                    border-radius: 10px;
                    background: QLinearGradient( x1:0.358, y1:0.602182, x2:0.960318, y2:0.648, stop:0 rgb(124, 57, 191), stop:0.903409 rgb(242, 80, 231));
                {'}'}
            """
        )
        self.CacheBar.setProperty("value", 0)
        self.CacheBar.setAlignment(QtCore.Qt.AlignCenter)

        # ______________   CLICKABLE LINKS   _____________________ #

        self.TitleLink = QtWidgets.QLabel(self.mainWidget)
        self.PaypalLink = QtWidgets.QLabel(self.TransparentLayer)
        self.TwitterLink = QtWidgets.QLabel(self.TransparentLayer)
        self.OnlineIconsLink = QtWidgets.QLabel(self.TransparentLayer)

        links = (
            self.TitleLink,
            self.PaypalLink,
            self.TwitterLink,
            self.OnlineIconsLink
            )

        for link in links:
            link.setFont(font)
            link.setOpenExternalLinks(True)

        font.setPointSize(19)
        font.setItalic(False)
        font.setBold(True)
        self.TitleLink.setFont(font)

        # ______________   SPACERS AND LAYOUTS (Order matter)  _____________________ #
        SpacerMinExp = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        SpacerExpMin = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        SpacerFixMin = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        spacerItem = SpacerExpMin
        spacerItem1 = SpacerMinExp
        spacerItem2 = SpacerExpMin
        spacerItem3 = SpacerMinExp
        spacerItem4 = SpacerFixMin
        spacerItem5 = SpacerMinExp
        spacerItem6 = SpacerMinExp
        spacerItem7 = SpacerExpMin
        spacerItem8 = SpacerMinExp
        spacerItem9 = SpacerExpMin
        spacerItem10 = SpacerExpMin
        spacerItem11 = SpacerMinExp

        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.setObjectName("GridLayout")
        self.GridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.GridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.GridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.GridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.GridLayout.addItem(spacerItem4, 6, 2, 1, 1)
        self.GridLayout.addWidget(self.IpInput, 2, 2, 1, 1)
        self.GridLayout.addWidget(self.IpLabel, 2, 1, 1, 1)
        self.GridLayout.addWidget(self.PortLabel, 3, 1, 1, 1)
        self.GridLayout.addWidget(self.PortInput, 3, 2, 1, 1)
        self.GridLayout.addWidget(self.GameIconsRadio, 8, 2, 1, 1)
        self.GridLayout.addWidget(self.GameIconsInfo, 9, 2, 1, 1)
        self.GridLayout.addWidget(self.ModeLabel, 10, 1, 1, 1)
        self.GridLayout.addWidget(self.SystemIconsRadio, 10, 2, 1, 1)
        self.GridLayout.addWidget(self.SysIconsInfo, 11, 2, 1, 1)
        self.GridLayout.addWidget(self.AvatarIconsRadio, 12, 2, 1, 1)

        self.VerticalLayout4 = QtWidgets.QVBoxLayout(self.TransparentLayer)
        self.VerticalLayout4.setObjectName("VerticalLayout4")
        self.VerticalLayout5 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.VerticalLayout5.setObjectName("VerticalLayout5")
        self.VerticalLayout6 = QtWidgets.QVBoxLayout()
        self.VerticalLayout6.setObjectName("VerticalLayout6")

        self.GridLayout2 = QtWidgets.QGridLayout()
        self.GridLayout2.setObjectName("GridLayout2")
        self.GridLayout2.setContentsMargins(-1, 15, -1, -1)
        self.GridLayout2.addItem(spacerItem5, 0, 2, 1, 1)
        self.GridLayout2.addItem(spacerItem7, 2, 0, 1, 1)
        self.GridLayout2.addItem(spacerItem6, 2, 1, 2, 1)
        self.GridLayout2.addItem(spacerItem8, 5, 2, 1, 1)
        self.GridLayout2.addItem(spacerItem9, 1, 2, 1, 1)
        self.GridLayout2.addItem(spacerItem10, 2, 3, 1, 1)
        self.GridLayout2.addWidget(self.CacheBar, 4, 2, 1, 1)
        self.GridLayout2.addWidget(self.CacheLabel, 4, 1, 1, 1)
        self.GridLayout2.addWidget(self.PaypalLink, 7, 2, 1, 1)
        self.GridLayout2.addWidget(self.ConnectBtn, 2, 2, 2, 1)
        self.GridLayout2.addWidget(self.TwitterLink, 8, 2, 1, 1)
        self.GridLayout2.addWidget(self.OnlineIconsLink, 6, 2, 1, 1)
        self.VerticalLayout4.addItem(spacerItem11)
        self.VerticalLayout5.addWidget(self.TitleLink)
        self.VerticalLayout5.addWidget(self.TransparentLayer)
        self.VerticalLayout6.addWidget(self.StatusLabel)
        self.VerticalLayout6.addLayout(self.GridLayout)
        self.VerticalLayout6.addLayout(self.GridLayout2)
        self.VerticalLayout4.addLayout(self.VerticalLayout6)

        # ______________   SETTINGS TREE   _____________________ #
        window.setCentralWidget(self.mainWidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 22))

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        window.setMenuBar(self.menubar)
        self.About = QtWidgets.QAction(window)
        self.Options = QtWidgets.QAction(window)
        self.actionAbout = QtWidgets.QAction(window)
        self.Remove_cache = QtWidgets.QAction(window)
        self.Special_thanks = QtWidgets.QAction(window)
        self.actionRemove_cache = QtWidgets.QAction(window)

        self.menuSettings.addAction(self.Options)
        self.menuSettings.addAction(self.Remove_cache)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.About)
        self.menuSettings.addAction(self.Special_thanks)
        self.menubar.addAction(self.menuSettings.menuAction())

        # ______________   SIGNALS   _____________________ #
        self.AvatarIconsRadio.toggled["bool"].connect(self.SysIconsInfo.hide)
        self.AvatarIconsRadio.toggled["bool"].connect(self.GameIconsInfo.hide)
        self.GameIconsRadio.toggled["bool"].connect(self.GameIconsInfo.setVisible)
        self.SystemIconsRadio.toggled["bool"].connect(self.SysIconsInfo.setVisible)
        QtCore.QMetaObject.connectSlotsByName(window)

        self.About.triggered.connect(self.open_about)
        self.ConnectBtn.clicked.connect(self.check_ip_port)
        self.Options.triggered.connect(self.open_options)
        self.Special_thanks.triggered.connect(self.open_credits)
        self.Remove_cache.triggered.connect(self.remove_cache)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.PortInput.setText(_translate("window", self.userPort))
        self.GameIconsRadio.setText(_translate("window", "Game Icon/Pic"))
        self.SystemIconsRadio.setText(_translate("window", "System Icons"))
        self.AvatarIconsRadio.setText(_translate("window", "Profile Avatar"))
        self.IpInput.setPlaceholderText(_translate("window", "192.168.XXX.XXX"))
        self.ModeLabel.setText(_translate("window", self.html.span_tag("MODE", "#f2ae30", 16, font=self.userFont)))
        self.IpLabel.setText(_translate("window", self.html.span_tag("PS4 IP", "#f2ae30", 16, font=self.userFont)))
        self.CacheLabel.setText(_translate("window", self.html.span_tag("Cache", "#f2ae30", 10, font=self.userFont)))
        self.PortLabel.setText( _translate( "window", self.html.span_tag("PS4 Port", "#f2ae30", 16, font=self.userFont)))
        self.StatusLabel.setText(_translate("window", self.html.span_tag("Awaiting ..", "#f2ae30", 18, font=self.userFont)))
        self.OnlineIconsLink.setText(_translate("window", self.html.a_tag("https://all-exhost.github.io/Icons.html", "Download Free Icons", "#f250e7", 8, font=self.userFont)))
        self.PaypalLink.setText(_translate("window", self.html.a_tag("https://www.paypal.com/paypalme/Officialahmed0", "Donate (PayPal)", "#f250e7", 8, font=self.userFont)))
        self.TwitterLink.setText(_translate("window", self.html.a_tag("https://twitter.com/OfficialAhmed0", "Created by @OfficialAhmed0", "#f250e7", 8, font=self.userFont)))
        self.SysIconsInfo.setText(_translate("window", self.html.span_tag("Note: Full R/W permissions required ( PS4 Xplorer FTP by enabling danger mode)", "#f2ae30", 8, font=self.userFont),))
        self.GameIconsInfo.setText(_translate("window", self.html.span_tag("Note: You can enable Homebrew icons in the settings before connecting to the PS4", "#f2ae30", 8, font=self.userFont)))
        self.TitleLink.setText(_translate("window", self.html.a_tag("https://github.com/OfficialAhmed/Iconit-PS4/releases", f"Iconit v{self.get_update_version()}", "#f250e7", 18, font=self.userFont),))

        self.About.setText(_translate("window", "About"))
        self.actionAbout.setText(_translate("window", "About"))
        self.Options.setText(_translate("window", "Options..."))
        self.ConnectBtn.setText(_translate("window", "Connect PS4"))
        self.menuSettings.setTitle(_translate("window", "Settings"))
        self.Remove_cache.setText(_translate("window", "Remove cache"))
        self.Special_thanks.setText(_translate("window", "Special thanks"))

        self.ConnectBtn.setShortcut("Return")

        # Autofill cached IP & port from pref.ini
        cache = self.settings.update_cache(self.pref_path)
        self.PortInput.setText(cache[1])
        self.IpInput.setText(cache[2])
        