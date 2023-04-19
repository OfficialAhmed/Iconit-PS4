import json
from PyQt5 import QtCore, QtGui, QtWidgets
from Module.Icons import Main as Icons

class Ui(Icons):
    
    def __init__(self) -> None:
        super().__init__()
        self.is_bg_image_changed = False
        self.ids = self.get_ids()
        self.selected_mode = self.get_selected_mode()
        self.icon_names = tuple(i for i in self.ids.keys())
        self.icon_path = f"{self.metadata_path}{self.selected_mode}/".replace("\\", "/")

        # Temp Settings | reset on app restart (v4.91)
        self.last_browse_path = ""

        self.external_games = self.external_game_ids
        self.current_game_id = self.icon_names[0]

        # Change bg accroding to screen resolution
        if self.screen_w <= 1366:
            self.background = "SDbg.@OfficialAhmed0"
        elif self.screen_w <= 1920:
            self.background = "HDbg.@OfficialAhmed0"
        elif self.screen_w <= 2048:
            self.background = "2kbg.@OfficialAhmed0"
        else:
            self.background = "4kbg.@OfficialAhmed0"


    def setupUi(self, window):
        self.window = window # for next window

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(25)
        font.setFamily(self.font)

        # ______________    WINDOW SPECS    _________________ # 
        window.setObjectName("IconsWindow")
        window.setMinimumSize(QtCore.QSize(self.screen_w, 720))
        window.setWindowIcon(QtGui.QIcon(f"{self.pref_path}ic1.@OfficialAhmed0"))
        window.setStyleSheet(f"background-image: url({self.pref_path}{self.background});")
        window.setWindowTitle(f"Iconit v{self.app_version} ({self.app_release_date})")


        # ______________       MENU BAR      ______________________#
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 22))

        self.SetDefaultIcon = QtWidgets.QAction(window)
        
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        self.menuMore.addAction(self.SetDefaultIcon)
        self.menubar.addAction(self.menuMore.menuAction())


        # ______________    LABELS    _________________ # 
        self.TitleLabel = QtWidgets.QLabel(window)
        self.HomebrewLabel = QtWidgets.QLabel(window)
        self.GameTitleLabel = QtWidgets.QLabel(window)

        font.setPointSize(22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        labels = (self.GameTitleLabel, self.TitleLabel, self.HomebrewLabel)
        for label in labels:
            label.setFont(font)
            label.setMinimumSize(QtCore.QSize(200, 40))
            label.setStyleSheet("color:rgb(255,255,255)")
            label.setFrameShape(QtWidgets.QFrame.Box)
            label.setAlignment(QtCore.Qt.AlignCenter)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)

        self.GameIdLabel = QtWidgets.QLabel(window)
        self.IconLocationLabel = QtWidgets.QLabel(window)
        self.TotalGamesLabel = QtWidgets.QLabel(window)
        self.IconSizeLabel = QtWidgets.QLabel(window)
        
        font.setPointSize(15)
        font.setBold(False)
        labels = (self.GameIdLabel, self.IconLocationLabel, self.TotalGamesLabel, self.IconSizeLabel)
        for label in labels:
            label.setFont(font)
            label.setMinimumSize(QtCore.QSize(230, 40))
            label.setStyleSheet("color:rgb(255, 255, 255);")
            label.setFrameShape(QtWidgets.QFrame.Box)
            label.setAlignment(QtCore.Qt.AlignCenter)

        # Unallocate memory
        del labels

        # ______________    BUTTONS    _________________ # 
        font.setPointSize(13)
        font.setBold(True)
        self.SelectBtn = QtWidgets.QPushButton(window)
        self.SelectBtn.setFont(font)
        self.SelectBtn.setMinimumSize(QtCore.QSize(230, 40))
        self.SelectBtn.setStyleSheet("color:rgb(255, 255, 255);")
        self.SelectBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font.setBold(False)
        self.MaskBtn = QtWidgets.QPushButton(window)
        self.ChangeIconBtn = QtWidgets.QPushButton(window)

        btns = (self.MaskBtn, self.ChangeIconBtn)
        for btn in btns:
            btn.setFont(font)
            btn.setMinimumSize(QtCore.QSize(170, 35))
            btn.setStyleSheet("color: rgb(255, 255, 255);")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
            btn.setSizePolicy(sizePolicy)

        self.PreviousBtn = QtWidgets.QToolButton(window)
        self.NextBtn = QtWidgets.QToolButton(window)

        btns = (self.PreviousBtn, self.NextBtn)
        for index, btn in enumerate(btns):
            btn.setArrowType(QtCore.Qt.RightArrow)
            if index == 0:
                btn.setArrowType(QtCore.Qt.LeftArrow)

            btn.setFont(font)
            btn.setMinimumSize(QtCore.QSize(170, 30))
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setStyleSheet("color: rgb(255, 255, 255);")
            sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
            btn.setSizePolicy(sizePolicy)
        del btns # remove memory allocation 

        font.setPointSize(15)
        self.ChangeBgBtn = QtWidgets.QPushButton(window)
        self.ChangeBgBtn.setFont(font)
        self.ChangeBgBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.ChangeBgBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeBgBtn.setStyleSheet("color:rgb(255, 255, 255);")

        font.setPointSize(17)
        self.SendBtn = QtWidgets.QPushButton(window)
        self.SendBtn.setFont(font)
        self.SendBtn.setEnabled(False)
        self.SendBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.SendBtn.setMaximumSize(QtCore.QSize(1000, 60))
        self.SendBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.SendBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # ______________    TEXT    _________________ # 
        font.setPointSize(16)
        self.GameIdTxt = QtWidgets.QLabel(window)
        self.IconSizeTxt = QtWidgets.QLabel(window)
        self.TotalGamesTxt = QtWidgets.QLabel(window)
        self.IconLocationTxt = QtWidgets.QLabel(window)
        
        texts = (self.GameIdTxt, self.IconSizeTxt, self.TotalGamesTxt, self.IconLocationTxt)
        for txt in texts:
            txt.setFont(font)
            txt.setStyleSheet("color:rgb(255, 255, 255);")
            txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        font.setPointSize(12)
        self.LogsTxt = QtWidgets.QTextEdit(window)
        self.LogsTxt.setReadOnly(True)

        del texts
        # ______________    LINES    ___________________ # 
        self.Line2 = QtWidgets.QFrame(window)
        self.Line3 = QtWidgets.QFrame(window)
        self.Line4 = QtWidgets.QFrame(window)
        self.Line5 = QtWidgets.QFrame(window)

        lines = (self.Line2, self.Line3, self.Line4, self.Line5)
        for line in lines:
            line.setMinimumSize(QtCore.QSize(10, 3))
            line.setStyleSheet(f"background-image: url({self.pref_path}White.@OfficialAhmed0);")
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)

        del lines
        # ______________    LINKS    _________________ # 
        self.TwitterLink = QtWidgets.QLabel(window)
        self.PaypalLink = QtWidgets.QLabel(window)

        links = (self.TwitterLink, self.PaypalLink)
        for link in links:
            link.setLineWidth(1)
            link.setOpenExternalLinks(True)
            link.setFrameShape(QtWidgets.QFrame.Box)
            link.setMinimumSize(QtCore.QSize(200, 20))
            link.setMaximumSize(QtCore.QSize(200, 20))
            link.setFrameShadow(QtWidgets.QFrame.Plain)
            link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            link.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHeightForWidth(link.sizePolicy().hasHeightForWidth())
            link.setSizePolicy(sizePolicy)

        del links 
        # ______________    SIGNALS    _________________ # 
        self.NextBtn.clicked.connect(self.next)
        self.SelectBtn.clicked.connect(self.select)
        self.PreviousBtn.clicked.connect(self.previous)
        self.SendBtn.clicked.connect(self.render_upload_window)
        self.MaskBtn.clicked.connect(self.render_mask_maker_window)
        self.ChangeBgBtn.clicked.connect(self.change_picture)
        self.ChangeIconBtn.clicked.connect(self.change_icon)

        self.menuMore.triggered.connect(self.render_set_default_icons_window)
        
        # ______________    GAME TITLES    _________________ # 
        font.setPointSize(15)
        self.GameTitles = QtWidgets.QComboBox(window)
        self.GameTitles.setFont(font)
        self.GameTitles.setDuplicatesEnabled(True)
        self.GameTitles.setMinimumSize(QtCore.QSize(0, 30))
        self.GameTitles.setStyleSheet("color: rgb(255,255,255);")
        self.GameTitles.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy.setHeightForWidth(self.GameTitles.sizePolicy().hasHeightForWidth())
        self.GameTitles.setSizePolicy(sizePolicy)

        # ______________    ICONS    _________________ # 
        self.Icon = QtWidgets.QGraphicsView(window)
        self.Icon.setMinimumSize(QtCore.QSize(340, 370))
        self.Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Icon.setStyleSheet(f"border-image: url('{self.icon_path}{self.icon_names[0]}')")
        sizePolicy.setHeightForWidth(self.Icon.sizePolicy().hasHeightForWidth())
        self.Icon.setSizePolicy(sizePolicy)

        # ______________    LAYOUTS    _________________ # 
        self.TopLayout = QtWidgets.QFormLayout()
        self.TopLayout.setContentsMargins(20, 20, 20, -1)
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TitleLabel)
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.HomebrewLabel)

        self.Change_Mask_btnLayout = QtWidgets.QFormLayout()
        self.Change_Mask_btnLayout.setVerticalSpacing(3)
        self.Change_Mask_btnLayout.setContentsMargins(-1, -1, -1, 0)
        self.Change_Mask_btnLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.PreviousBtn)
        self.Change_Mask_btnLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NextBtn)
        self.Change_Mask_btnLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.MaskBtn)
        self.Change_Mask_btnLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ChangeIconBtn)

        self.bg_change_browse_btnLayout = QtWidgets.QFormLayout()
        self.bg_change_browse_btnLayout.setContentsMargins(200, 0, 200, -1)
        self.bg_change_browse_btnLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ChangeBgBtn)

        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.setSpacing(5)
        self.LeftLayout.addWidget(self.Icon)
        self.LeftLayout.addWidget(self.SendBtn)
        self.LeftLayout.setContentsMargins(20, 30, -1, 10)
        self.LeftLayout.addLayout(self.Change_Mask_btnLayout)

        self.RightLayout = QtWidgets.QFormLayout()
        self.RightLayout.setContentsMargins(-1, 60, 20, -1)
        self.RightLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.GameTitleLabel)
        self.RightLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GameIdLabel)
        self.RightLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.GameIdTxt)
        self.RightLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.Line2)
        self.RightLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.IconLocationLabel)
        self.RightLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.Line3)
        self.RightLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.TotalGamesLabel)
        self.RightLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.IconLocationTxt)
        self.RightLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.TotalGamesTxt)
        self.RightLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.Line4)
        self.RightLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.IconSizeLabel)
        self.RightLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.IconSizeTxt)
        self.RightLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.Line5)
        self.RightLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.GameTitles)
        self.RightLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.SelectBtn)
        self.RightLayout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.bg_change_browse_btnLayout)
        self.RightLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.LogsTxt)

        self.CreditsLayout = QtWidgets.QVBoxLayout()
        self.CreditsLayout.setSpacing(5)
        self.CreditsLayout.addWidget(self.PaypalLink)
        self.CreditsLayout.addWidget(self.TwitterLink)
        self.CreditsLayout.setContentsMargins(500, 0, 0, -1)
        self.CreditsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

        self.BottomLayout = QtWidgets.QVBoxLayout()
        self.BottomLayout.addLayout(self.CreditsLayout)
        self.BottomLayout.setContentsMargins(20, 10, 20, 0)

        self.formLayout = QtWidgets.QFormLayout(window)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.TopLayout)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.LeftLayout)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.RightLayout)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.BottomLayout)
        

        self.retranslateUi()

        self.GameTitles.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.SetDefaultIcon.setText(_translate("window", self.translated_content.get("setDefaultIcons")))
        self.menuMore.setTitle(_translate("window", self.translated_content.get("menuMore")))

        self.GameIdTxt.setText(_translate("IconsWindow", self.current_game_id))
        self.TotalGamesTxt.setText(_translate("IconsWindow", f"1/{len(self.ids)}"))
        self.NextBtn.setText(_translate("IconsWindow", self.translated_content.get("NextBtn")))
        self.MaskBtn.setText(_translate("IconsWindow", self.translated_content.get("MaskBtn")))
        self.SendBtn.setText(_translate("IconsWindow", self.translated_content.get("SendBtn")))
        self.SelectBtn.setText(_translate("IconsWindow", self.translated_content.get("SelectBtn")))
        self.ChangeBgBtn.setText(_translate("IconsWindow", self.translated_content.get("ChangeBgBtn")))
        self.GameIdLabel.setText(_translate("IconsWindow", self.translated_content.get("GameIdLabel")))
        self.ChangeIconBtn.setText(_translate("IconsWindow", self.translated_content.get("ChangeIconBtn")))
        self.IconSizeLabel.setText(_translate("IconsWindow", self.translated_content.get("IconSizeLabel")))
        self.TotalGamesLabel.setText(_translate("IconsWindow", self.translated_content.get("TotalGamesLabel")))
        self.IconLocationLabel.setText(_translate("IconsWindow", self.translated_content.get("IconLocationLabel")))
        self.IconSizeTxt.setText(_translate("IconsWindow", f"{self.translated_content.get('IconSizeTxt')}(512x512)"))
        self.TwitterLink.setText(_translate("IconsWindow", self.html.a_tag("https://twitter.com/OfficialAhmed0", self.translated_content.get("TwitterLink"), "#90f542", 14, "text-decoration: underline; vertical-align:super;", font=self.font)))
        self.PaypalLink.setText(_translate("IconsWindow",self.html.a_tag("https://www.paypal.com/paypalme/Officialahmed0", self.translated_content.get("PaypalLink"), "#90f542", 14, "text-decoration: underline; vertical-align:super; font-style:italic", font=self.font)))
        self.LogsTxt.setHtml(_translate("IconsWindow",
            f"""
                {self.html.span_tag(f"*{self.translated_content.get('LogsTxt')}: {self.ip}*", "#ffffff", 12)}
                {self.html.p_tag(f"-qt-paragraph-type:empty; margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;")}
            """
            )
        )

        # 
        """
        #################################################################
                    KEYBOARD RECOGNITION SHORTCUTS v4.07
        #################################################################
        """
        self.NextBtn.setShortcut("Right")
        self.PreviousBtn.setShortcut("Left")
        self.SelectBtn.setShortcut("return")


        """
        #################################################################
                        HOVEROVER TOOL TIPS
        #################################################################
        """
        translated_tooltips:dict = self.translated_content.get("ToolTips")

        self.NextBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("NextBtn")))
        self.MaskBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("MaskBtn")))
        self.SendBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("SendBtn")))
        self.SelectBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("SelectBtn")))
        self.PreviousBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("PreviousBtn")))
        self.ChangeBgBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("ChangeBgBtn")))
        self.ChangeIconBtn.setToolTip(self.html.tooltip_tag(translated_tooltips.get("ChangeIconBtn")))
        self.HomebrewLabel.setToolTip(self.html.tooltip_tag(translated_tooltips.get("HomebrewLabel")))
        self.GameTitleLabel.setToolTip(self.html.tooltip_tag(translated_tooltips.get("GameTitleLabel")))
        self.IconLocationTxt.setToolTip(self.html.tooltip_tag(translated_tooltips.get("IconLocationTxt")))
    

        """
        #################################################################
                    MODE SPECIFIC FEATURES
        #################################################################
        """
        match self.selected_mode:
            case "game":
                for index, current_game_id in enumerate(self.ids):
                    self.GameTitles.addItem(f"{index + 1}: {self.ids.get(current_game_id).get('title')} [{current_game_id}]")
                
                # ______________    IS HOMEBREW    _________________ # 
                if self.is_toggled_homebrew == "True":
                    if "CUSA" in self.current_game_id:
                        state = self.translated_content.get("HomebrewLabel_Y") 
                    elif "CUSA" not in self.current_game_id:
                        state = self.translated_content.get("HomebrewLabel_N")

                else:
                    state = self.translated_content.get("HomebrewLabel_T")
                    

                # ______________    ICON LOCATION    _________________ # 
                if self.ids[self.current_game_id] in self.external_games:
                    location = self.translated_content.get("IconLocation_Ex")
                
                else:
                    location = self.translated_content.get("IconLocation_In")


                # ______________    UPDATE TEXTs    _________________ # 
                self.HomebrewLabel.setText(_translate("IconsWindow", state))
                self.IconLocationTxt.setText(_translate("IconsWindow", location))
                
                self.GameTitleLabel.setText(self.ids.get(self.current_game_id).get("title"))
                self.TitleLabel.setText(_translate("IconsWindow", self.translated_content.get("TitleLabel_GameIcons")))


            case "system apps":
                for index, current_game_id in enumerate(self.ids):
                    self.GameTitles.addItem(f"{index + 1}: {self.ids.get(current_game_id)} [{current_game_id}]")
                
                # ______________    UPDATE TEXT    _________________ # 
                self.TitleLabel.setText(_translate("IconsWindow", self.translated_content.get("TitleLabel_SysIcons")))
                self.GameTitleLabel.setText(self.ids.get(self.current_game_id))
                self.HomebrewLabel.setText(_translate("IconsWindow", "SYSTEM ICON: YES"))

                # ______________    HIDE WIDGETS    _________________ # 
                self.IconLocationLabel.hide()
                self.IconLocationTxt.hide()
                self.ChangeBgBtn.hide()


    def translate_dynamic_elements(self):
        """
            Translate changable elements on button click 
        """
