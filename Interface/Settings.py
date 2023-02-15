import json
from PyQt5 import QtCore, QtGui, QtWidgets
from Module.Settings import Main as Settings
from Module.Widget.Translate import Translate

class Ui(Settings):
    def __init__(self) -> None:
        super().__init__()
        self.settings_cache = self.get_settings_cache()
        self.translation = Translate(self.language_path)
        self.supported_languages: dict = self.translation.get_supported_languages()
        self.translated_languages: dict = self.translation.get_translation(self.settings_cache.get("language"), "Languages")
        self.translated_languages_in_english = {key: value for value, key in self.translated_languages.items()}


    def get_settings_cache(self) -> dict:
        try:
            with open(f"{self.cache_path}Settings.json", encoding="utf-8") as file:
                return json.load(file)
        except: return self.local_settings_cache


    def setupUi(self, OptionsWin):
        self.OptionsWin = OptionsWin 
        self.OptionsWin.setObjectName("OptionsWin")
        self.OptionsWin.resize(680, 400)


        #_________________   VISUALS   ________________________#
        self.FontObj = QtGui.QFont()
        self.FontObj.setFamily(self.settings_cache.get("font"))
        self.FontObj.setPointSize(10)
        self.OptionsWin.setFont(self.FontObj)

        self.arrow_cursor = QtGui.QCursor(QtCore.Qt.ArrowCursor)
        self.pointing_cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        

        #_________________   BUTTONS   ________________________#
        self.SaveBtn = QtWidgets.QPushButton(self.OptionsWin)
        self.NoRadio = QtWidgets.QRadioButton(self.OptionsWin)
        self.YesRadio = QtWidgets.QRadioButton(self.OptionsWin)
        self.CancelBtn = QtWidgets.QPushButton(self.OptionsWin)
        self.DefaultBtn = QtWidgets.QPushButton(self.OptionsWin)
        self.IconsPathBtn = QtWidgets.QToolButton(self.OptionsWin)
        self.DownloadPathBtn = QtWidgets.QToolButton(self.OptionsWin)

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
        self.IpLabel = QtWidgets.QLabel(self.OptionsWin)
        self.PortLabel = QtWidgets.QLabel(self.OptionsWin)
        self.FontLabel = QtWidgets.QLabel(self.OptionsWin)
        self.LanguageLabel = QtWidgets.QLabel(self.OptionsWin)
        self.HomebrewLabel = QtWidgets.QLabel(self.OptionsWin)
        self.IconsPathLabel = QtWidgets.QLabel(self.OptionsWin)
        self.DownloadPathLabel = QtWidgets.QLabel(self.OptionsWin)


        #_________________   INPUTS   ________________________#
        self.Ip = QtWidgets.QLineEdit(self.OptionsWin)
        self.Port = QtWidgets.QSpinBox(self.OptionsWin)
        self.Fonts = QtWidgets.QFontComboBox(self.OptionsWin)
        self.IconPath = QtWidgets.QLineEdit(self.OptionsWin)
        self.Languages = QtWidgets.QComboBox(self.OptionsWin)
        self.DownloadPath = QtWidgets.QLineEdit(self.OptionsWin)
        self.EnableHbInfo = QtWidgets.QPlainTextEdit(self.OptionsWin)

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
        self.OptionsWin.setTabOrder(self.Fonts, self.Ip)
        self.OptionsWin.setTabOrder(self.Ip, self.IconsPathBtn)
        self.OptionsWin.setTabOrder(self.YesRadio, self.NoRadio)
        self.OptionsWin.setTabOrder(self.SaveBtn, self.CancelBtn)
        self.OptionsWin.setTabOrder(self.NoRadio, self.DefaultBtn)
        self.OptionsWin.setTabOrder(self.DefaultBtn, self.SaveBtn)
        self.OptionsWin.setTabOrder(self.DownloadPath, self.IconPath)
        self.OptionsWin.setTabOrder(self.CancelBtn, self.EnableHbInfo)
        self.OptionsWin.setTabOrder(self.DownloadPathBtn, self.YesRadio)
        self.OptionsWin.setTabOrder(self.EnableHbInfo, self.DownloadPath)
        self.OptionsWin.setTabOrder(self.IconsPathBtn, self.DownloadPathBtn)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)


        #_________________   LAYOUTS   ________________________#
        self.lineSeperator = QtWidgets.QFrame(self.OptionsWin)
        self.lineSeperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeperator.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.TopLayout = QtWidgets.QGridLayout()
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.FirstLayout = QtWidgets.QHBoxLayout()
        self.BottomLayout = QtWidgets.QHBoxLayout()
        self.SecondLayout = QtWidgets.QHBoxLayout()
        self.HombrewLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.OptionsWin)

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
        self.Port.setValue(int(self.settings_cache.get("port")))
        self.Ip.setPlaceholderText(self.settings_cache.get("ip"))
        self.Fonts.setCurrentText(self.settings_cache.get("font"))
        self.IconPath.setPlaceholderText(self.settings_cache.get("icons_path"))
        self.DownloadPath.setPlaceholderText(self.settings_cache.get("download_path"))


        #_________________      SIGNALS     _______________________#
        self.NoRadio.setChecked(True)
        if self.settings_cache.get("homebrew") == "True":
            self.YesRadio.setChecked(True)
        
        self.SaveBtn.clicked.connect(
            lambda: self.save_cache(
                self.Fonts.currentText(),
                self.IconPath.text(),
                self.DownloadPath.text(),
                str(self.YesRadio.isChecked()),
                self.Port.text(),
                self.Ip.text(),
                self.supported_languages.get(
                    self.translated_languages_in_english.get( 
                        self.Languages.currentText()
                    )
                ), True
            )
        )

        self.CancelBtn.clicked.connect(
            lambda: self.OptionsWin.close()
        )
        
        self.IconsPathBtn.clicked.connect(
            lambda: self.render_path_window("icons")
        )

        self.DownloadPathBtn.clicked.connect(
            lambda: self.render_path_window("download")
        )

        self.DefaultBtn.clicked.connect(self.reset_to_defaults)

        QtCore.QMetaObject.connectSlotsByName(self.OptionsWin)
        self.translate_ui()


    def translate_ui(self):
        translated_content: dict = self.translation.get_translation(self.settings_cache.get("language"), "Settings")
        self._translate = QtCore.QCoreApplication.translate

        self.translate_dropdown_list_items()
        
        self.NoRadio.setText(self._translate("OptionsWin", translated_content.get("NoRadio")))
        self.YesRadio.setText(self._translate("OptionsWin", translated_content.get("YesRadio")))
        self.SaveBtn.setText(self._translate("OptionsWin", translated_content.get("SaveBtn")))
        self.CancelBtn.setText(self._translate("OptionsWin", translated_content.get("CancelBtn")))
        self.IpLabel.setText(self._translate("OptionsWin", translated_content.get("IpLabel")))
        self.DefaultBtn.setText(self._translate("OptionsWin", translated_content.get("DefaultBtn")))
        self.PortLabel.setText(self._translate("OptionsWin", translated_content.get("PortLabel")))
        self.FontLabel.setText(self._translate("OptionsWin", translated_content.get("FontLabel")))
        self.HomebrewLabel.setText(self._translate("OptionsWin", translated_content.get("HomebrewLabel")))
        self.LanguageLabel.setText(self._translate("OptionsWin", translated_content.get("LanguageLabel")))
        self.IconsPathLabel.setText(self._translate("OptionsWin", translated_content.get("IconsPathLabel")))
        self.DownloadPathLabel.setText(self._translate("OptionsWin", translated_content.get("DownloadPathLabel")))
        self.EnableHbInfo.setPlainText(self._translate("OptionsWin", translated_content.get("EnableHbInfo")))
        self.OptionsWin.setWindowTitle(self._translate("OptionsWin", translated_content.get("WindowTitle")))


    def translate_dropdown_list_items(self) -> None:
        """ Translate the languages dropdown list according to the default language chosen """
        
        for index, language in enumerate(self.supported_languages):
            self.Languages.addItem(self.translated_languages.get(language))
            
            if language == self.settings_cache.get("language"):
                self.Languages.setCurrentIndex(index)