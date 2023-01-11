import json, os
from PyQt5 import QtCore, QtGui, QtWidgets
from environment import html
from Module.Icons import Main as Icons

class Ui(Icons):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, window, Games, modeSelected):
        self.window = window

        self.exGames = self.all_CUSA_ex
        self.sysGames = self.all_CUSA_sys

        # Temp Settings | reset on app restart (v4.91)
        self.last_browse_path = ""

        self.sysIconsAlgo = False
        if len(self.sysGames) > 0:
            self.sysIconsAlgo = True

        self.modeSelected = modeSelected
        self.Games = Games
        temp = self.temp_path + "MegaSRX\\metadata\\" + self.modeSelected + "\\"
        self.CUSA_img = temp.replace("\\", "/")

        # Get all icon names from local path sorted by value(game title)
        self.game_icons = tuple(i for i in self.Games.keys())

        self.changeIconPath = ""
        self.changeBgPath = ""
        self.img_limit = len(self.game_icons)
        self.img_counter = 0

        # v4.72
        if len(self.sysGames) == 0:
            ReadJson = open(self.info_json_path)
            self.gameInfo = json.load(ReadJson)

        # v4.61
        self.bgImageChanged = False

        window.setObjectName("IconsWindow")
        window.resize(1080, 720)
        window.setWindowIcon(
            QtGui.QIcon(self.pref_location + "ic1.@OfficialAhmed0")
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        window.setMinimumSize(QtCore.QSize(1300, 720))

        # Change bg accroding to screen resolution
        if self.screen_w <= 1366:
            self.background = "SDbg.@OfficialAhmed0"
        elif self.screen_w <= 1920:
            self.background = "HDbg.@OfficialAhmed0"
        elif self.screen_w <= 2048:
            self.background = "2kbg.@OfficialAhmed0"
        else:
            self.background = "4kbg.@OfficialAhmed0"

        window.setStyleSheet(
            f"background-image: url({self.pref_location + self.background});"
        )

        self.formLayout = QtWidgets.QFormLayout(window)
        self.formLayout.setObjectName("formLayout")
        self.TopLayout = QtWidgets.QFormLayout()
        self.TopLayout.setContentsMargins(20, 20, 20, -1)
        self.TopLayout.setObjectName("TopLayout")
        self.Title_label = QtWidgets.QLabel(window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_label.sizePolicy().hasHeightForWidth())
        self.Title_label.setSizePolicy(sizePolicy)
        self.Title_label.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setFamily(self.userFont)
        font.setWeight(75)
        self.Title_label.setFont(font)
        self.Title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Title_label)
        self.homebrewLabel = QtWidgets.QLabel(window)
        self.homebrewLabel.setEnabled(False)

        sizePolicy.setHeightForWidth(
            self.homebrewLabel.sizePolicy().hasHeightForWidth()
        )
        self.homebrewLabel.setSizePolicy(sizePolicy)
        self.homebrewLabel.setMinimumSize(QtCore.QSize(200, 0))
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.homebrewLabel.setFont(font)
        self.homebrewLabel.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.homebrewLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.homebrewLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.homebrewLabel.setObjectName("homebrewLabel")
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.homebrewLabel)
        self.whiteBg = QtWidgets.QFrame(window)
        self.whiteBg.setMinimumSize(QtCore.QSize(4000, 1))
        self.whiteBg.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.whiteBg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.whiteBg.setLineWidth(1)
        self.whiteBg.setFrameShape(QtWidgets.QFrame.HLine)
        self.whiteBg.setObjectName("whiteBg")
        self.TopLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.whiteBg)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.TopLayout)
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.setContentsMargins(20, 30, -1, 10)
        self.LeftLayout.setSpacing(5)
        self.LeftLayout.setObjectName("LeftLayout")
        self.Icon = QtWidgets.QGraphicsView(window)

        sizePolicy.setHeightForWidth(self.Icon.sizePolicy().hasHeightForWidth())
        self.Icon.setSizePolicy(sizePolicy)
        self.Icon.setMinimumSize(QtCore.QSize(340, 370))
        self.Icon.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.Icon.setObjectName("Icon")
        self.LeftLayout.addWidget(self.Icon)
        self.Change_Mask_btnLayout = QtWidgets.QFormLayout()
        self.Change_Mask_btnLayout.setContentsMargins(-1, -1, -1, 0)
        self.Change_Mask_btnLayout.setVerticalSpacing(3)
        self.Change_Mask_btnLayout.setObjectName("Change_Mask_btnLayout")
        self.ChangeIcon_btn = QtWidgets.QPushButton(window)

        sizePolicy.setHeightForWidth(
            self.ChangeIcon_btn.sizePolicy().hasHeightForWidth()
        )
        self.ChangeIcon_btn.setSizePolicy(sizePolicy)
        self.ChangeIcon_btn.setMinimumSize(QtCore.QSize(170, 35))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ChangeIcon_btn.setFont(font)
        self.ChangeIcon_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeIcon_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.ChangeIcon_btn.setObjectName("ChangeIcon_btn")
        self.Change_Mask_btnLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.ChangeIcon_btn
        )
        self.Mask_btn = QtWidgets.QPushButton(window)

        sizePolicy.setHeightForWidth(
            self.Mask_btn.sizePolicy().hasHeightForWidth()
        )
        self.Mask_btn.setSizePolicy(sizePolicy)
        self.Mask_btn.setMinimumSize(QtCore.QSize(0, 35))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Mask_btn.setFont(font)
        self.Mask_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mask_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mask_btn.setObjectName("Mask_btn")
        self.Change_Mask_btnLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.Mask_btn
        )
        self.Prev_btn = QtWidgets.QToolButton(window)

        sizePolicy.setHeightForWidth(self.Prev_btn.sizePolicy().hasHeightForWidth())
        self.Prev_btn.setSizePolicy(sizePolicy)
        self.Prev_btn.setMinimumSize(QtCore.QSize(170, 30))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Prev_btn.setFont(font)
        self.Prev_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_btn.setAutoFillBackground(False)
        self.Prev_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Prev_btn.setArrowType(QtCore.Qt.LeftArrow)
        self.Prev_btn.setObjectName("Prev_btn")
        self.Change_Mask_btnLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.Prev_btn
        )
        self.Next_btn = QtWidgets.QToolButton(window)

        sizePolicy.setHeightForWidth(self.Next_btn.sizePolicy().hasHeightForWidth())
        self.Next_btn.setSizePolicy(sizePolicy)
        self.Next_btn.setMinimumSize(QtCore.QSize(0, 25))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Next_btn.setFont(font)
        self.Next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Next_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Next_btn.setArrowType(QtCore.Qt.RightArrow)
        self.Next_btn.setObjectName("Next_btn")

        self.Change_Mask_btnLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.Next_btn
        )
        self.LeftLayout.addLayout(self.Change_Mask_btnLayout)
        self.Submit_btn = QtWidgets.QPushButton(window)

        sizePolicy.setHeightForWidth(self.Submit_btn.sizePolicy().hasHeightForWidth())
        self.Submit_btn.setSizePolicy(sizePolicy)
        self.Submit_btn.setMinimumSize(QtCore.QSize(0, 50))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Submit_btn.setFont(font)
        self.Submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Submit_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Submit_btn.setObjectName("Submit_btn")
        self.LeftLayout.addWidget(self.Submit_btn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.LeftLayout)
        self.RightLayout = QtWidgets.QFormLayout()
        self.RightLayout.setContentsMargins(-1, 60, 20, -1)
        self.RightLayout.setObjectName("RightLayout")
        self.GameTitle = QtWidgets.QLabel(window)
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.GameTitle.setFont(font)
        self.GameTitle.setMinimumHeight(45)
        self.GameTitle.setStyleSheet("color:rgb(255,255,255);")
        self.GameTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.GameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.GameTitle.setObjectName("GameTitle")
        self.RightLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.GameTitle
        )
        self.GameID_label = QtWidgets.QLabel(window)
        self.GameID_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(15)
        self.GameID_label.setFont(font)
        self.GameID_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.GameID_label.setFrameShape(QtWidgets.QFrame.Box)
        self.GameID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.GameID_label.setObjectName("GameID_label")
        self.RightLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.GameID_label
        )
        self.GameID = QtWidgets.QLabel(window)
        font.setPointSize(16)
        self.GameID.setFont(font)
        self.GameID.setStyleSheet("color:rgb(255, 255, 255);")
        self.GameID.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.GameID.setObjectName("GameID")
        self.RightLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.GameID)
        self.line = QtWidgets.QFrame(window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(50, 0))
        self.line.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.RightLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.Ex_In_label = QtWidgets.QLabel(window)

        sizePolicy.setHeightForWidth(self.Ex_In_label.sizePolicy().hasHeightForWidth())
        self.Ex_In_label.setSizePolicy(sizePolicy)
        self.Ex_In_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Ex_In_label.setFont(font)
        self.Ex_In_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.Ex_In_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Ex_In_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ex_In_label.setObjectName("Ex_In_label")
        self.RightLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Ex_In_label)
        self.Ex_In = QtWidgets.QLabel(window)
        font.setPointSize(16)
        self.Ex_In.setFont(font)
        self.Ex_In.setStyleSheet("color:rgb(255, 255, 255);")
        self.Ex_In.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.Ex_In.setObjectName("Ex_In")
        self.RightLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Ex_In)
        self.line_3 = QtWidgets.QFrame(window)
        self.line_3.setMinimumSize(QtCore.QSize(30, 3))
        self.line_3.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.RightLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.TotalGames_label = QtWidgets.QLabel(window)
        self.TotalGames_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(15)
        self.TotalGames_label.setFont(font)
        self.TotalGames_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.TotalGames_label.setFrameShape(QtWidgets.QFrame.Box)
        self.TotalGames_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalGames_label.setObjectName("TotalGames_label")
        self.RightLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.TotalGames_label
        )
        self.TotalGames = QtWidgets.QLabel(window)
        font.setPointSize(16)
        self.TotalGames.setFont(font)
        self.TotalGames.setStyleSheet("color:rgb(255, 255, 255);")
        self.TotalGames.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.TotalGames.setObjectName("TotalGames")
        self.RightLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.TotalGames)
        self.line_4 = QtWidgets.QFrame(window)
        self.line_4.setMinimumSize(QtCore.QSize(100, 3))
        self.line_4.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.RightLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.IconSize_label = QtWidgets.QLabel(window)
        self.IconSize_label.setMinimumSize(QtCore.QSize(190, 40))
        font.setPointSize(13)
        self.IconSize_label.setFont(font)
        self.IconSize_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.IconSize_label.setFrameShape(QtWidgets.QFrame.Box)
        self.IconSize_label.setAlignment(QtCore.Qt.AlignCenter)
        self.IconSize_label.setObjectName("IconSize_label")
        self.RightLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.IconSize_label
        )
        self.IconSize = QtWidgets.QLabel(window)
        font.setPointSize(16)
        self.IconSize.setFont(font)
        self.IconSize.setStyleSheet("color:rgb(255, 255, 255);")
        self.IconSize.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.IconSize.setObjectName("IconSize")
        self.RightLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.IconSize)
        self.line_5 = QtWidgets.QFrame(window)
        self.line_5.setMinimumSize(QtCore.QSize(100, 3))
        self.line_5.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.RightLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_5)

        self.Select_btn = QtWidgets.QPushButton(window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Select_btn.sizePolicy().hasHeightForWidth())

        self.Select_btn.setSizePolicy(sizePolicy)
        self.Select_btn.setMinimumSize(QtCore.QSize(190, 0))
        font.setPointSize(20)
        self.Select_btn.setFont(font)
        self.Select_btn.setStyleSheet("color:rgb(255, 255, 255);")
        self.Select_btn.setObjectName("Select_btn")
        self.Select_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.RightLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Select_btn)
        self.GameTitles = QtWidgets.QComboBox(window)

        sizePolicy.setHeightForWidth(self.GameTitles.sizePolicy().hasHeightForWidth())
        self.GameTitles.setSizePolicy(sizePolicy)
        self.GameTitles.setMinimumSize(QtCore.QSize(0, 30))
        font.setPointSize(15)
        self.GameTitles.setFont(font)
        self.GameTitles.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GameTitles.setDuplicatesEnabled(True)
        self.GameTitles.setStyleSheet("color: rgb(0, 0, 0);")
        self.GameTitles.setObjectName("GameTitles")
        font.setPointSize(12)
        self.RightLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.GameTitles)

        font.setPointSize(15)
        self.bg_change_browse_btnLayout = QtWidgets.QFormLayout()
        self.bg_change_browse_btnLayout.setContentsMargins(200, 0, 200, -1)
        self.bg_change_browse_btnLayout.setObjectName("bg_change_browse_btnLayout")
        self.bg_change_browse_btn = QtWidgets.QPushButton(window)
        self.bg_change_browse_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.bg_change_browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bg_change_browse_btn.setStyleSheet("color:rgb(255, 255, 255);")
        self.bg_change_browse_btn.setObjectName("bg_change_browse_btn")
        self.bg_change_browse_btnLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.bg_change_browse_btn
        )
        self.RightLayout.setLayout(
            12, QtWidgets.QFormLayout.FieldRole, self.bg_change_browse_btnLayout
        )
        self.bg_change_browse_btn.setFont(font)

        font.setPointSize(12)
        self.Logs = QtWidgets.QTextEdit(window)
        self.Logs.setReadOnly(True)
        self.Logs.setObjectName("Logs")
        self.RightLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.Logs)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.RightLayout)
        self.BottomLayout = QtWidgets.QVBoxLayout()
        self.BottomLayout.setContentsMargins(20, 10, 20, 0)
        self.BottomLayout.setObjectName("BottomLayout")
        self.line_6 = QtWidgets.QFrame(window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setMinimumSize(QtCore.QSize(4000, 0))
        self.line_6.setStyleSheet(
            f"background-image: url({self.pref_location}/White.@OfficialAhmed0);"
        )
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.BottomLayout.addWidget(self.line_6)
        self.CreditsLayout = QtWidgets.QVBoxLayout()
        self.CreditsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.CreditsLayout.setContentsMargins(500, 0, 0, -1)
        self.CreditsLayout.setSpacing(5)
        self.CreditsLayout.setObjectName("CreditsLayout")
        self.Title_label_2 = QtWidgets.QLabel(window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Title_label_2.sizePolicy().hasHeightForWidth()
        )
        self.Title_label_2.setSizePolicy(sizePolicy)
        self.Title_label_2.setMinimumSize(QtCore.QSize(10, 0))
        self.Title_label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Title_label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Title_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Title_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Title_label_2.setLineWidth(1)
        self.Title_label_2.setOpenExternalLinks(True)
        self.Title_label_2.setObjectName("Title_label_2")
        self.CreditsLayout.addWidget(self.Title_label_2)
        self.SupportMe = QtWidgets.QLabel(window)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SupportMe.sizePolicy().hasHeightForWidth())
        self.SupportMe.setSizePolicy(sizePolicy)
        self.SupportMe.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SupportMe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SupportMe.setFrameShape(QtWidgets.QFrame.Box)
        self.SupportMe.setOpenExternalLinks(True)
        self.SupportMe.setObjectName("SupportMe")
        self.CreditsLayout.addWidget(self.SupportMe)
        self.BottomLayout.addLayout(self.CreditsLayout)
        self.formLayout.setLayout(
            3, QtWidgets.QFormLayout.SpanningRole, self.BottomLayout
        )

        # v4.01
        self.Icon.setStyleSheet("border-image: url(" + self.CUSA_img + self.game_icons[0] + ");")
        self.Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Icon.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Icon.setLineWidth(2)
        self.Icon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Icon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # buttons back-end
        self.ChangeIcon_btn.clicked.connect(self.BrowseIcon)
        self.Mask_btn.clicked.connect(self.Mask_maker)
        self.Next_btn.clicked.connect(self.Next)
        self.Prev_btn.clicked.connect(self.Prev)
        self.Submit_btn.clicked.connect(self.Resize_Upload)
        self.Select_btn.clicked.connect(self.Select)
        self.bg_change_browse_btn.clicked.connect(self.BrowseBg)

        # add items the number of games that are found without renaming them
        for _ in range(len(self.Games)):
            self.GameTitles.addItem("select")

        self.retranslateUi(window)
        self.GameTitles.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, IconsWindow):
        _translate = QtCore.QCoreApplication.translate
        IconsWindow.setWindowTitle(
            _translate(
                "IconsWindow",
                "Iconit v"
                + str(self.get_update_version())
                + " ("
                + str(self.get_update_release_date())
                + ")",
            )
        )
        self.Title_label.setText(_translate("IconsWindow", "Change Game Icon"))
        self.ChangeIcon_btn.setText(_translate("IconsWindow", "Change Icon..."))
        self.Mask_btn.setText(
            _translate("IconsWindow", "Mask maker...")
        )
        self.Prev_btn.setText(_translate("IconsWindow", "Previous"))
        self.Next_btn.setText(_translate("IconsWindow", "Next"))
        self.Submit_btn.setText(_translate("IconsWindow", "Resize && Upload"))
        self.GameTitle.setText(_translate("IconsWindow", "Game Title Here"))
        self.GameID_label.setText(_translate("IconsWindow", "Game ID:"))
        self.GameID.setText(_translate("IconsWindow", "TextLabel"))
        self.Ex_In_label.setText(_translate("IconsWindow", "External / Internal"))
        self.Ex_In.setText(_translate("IconsWindow", "TextLabel"))
        self.TotalGames_label.setText(_translate("IconsWindow", "Total Games"))
        self.TotalGames.setText(_translate("IconsWindow", "TextLabel"))
        self.IconSize_label.setText(
            _translate("IconsWindow", "Min. Icon Size(512x512)")
        )
        self.IconSize.setText(
            _translate("IconsWindow", "Current Icon size(512x512)")
        )
        self.Select_btn.setText(_translate("IconsWindow", "Select"))
        self.bg_change_browse_btn.setText(
            _translate("IconsWindow", "Change Game Pic...")
        )
        self.Logs.setHtml(
            _translate(
                "IconsWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">*Connected to PS4: '
                + self.IP
                + "*</span></p>\n"
                '<p align="center" style="-qt-paragraph-type:empty; margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;"><br /></p>\n',
            )
        )
        self.Title_label_2.setText(
            _translate(
                "IconsWindow",
                '<html><head/><body><p align="center"><a href="https://twitter.com/OfficialAhmed0"><span style="font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">Created By @OfficialAhmed0</span></a></p></body></html>',
            )
        )
        self.SupportMe.setText(
            _translate("IconsWindow",
                '<html><head/><body><p align="center"><a href=""><span style="font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">PayPal</span></a></p></body></html>',
            )
        )

        self.Next_btn.setText(_translate("IconsWindow", "Browse Icon ..."))
        self.Prev_btn.setText(_translate("IconsWindow", "Browse Icon ..."))
        self.GameTitle.setText(
            _translate("IconsWindow", self.Games[self.game_icons[self.img_counter]])
        )
        self.GameID.setText(_translate("IconsWindow", self.game_icons[self.img_counter]))
        self.TotalGames.setText(
            _translate(
                "IconsWindow",
                str(self.img_counter + 1) + "/" + str(len(self.Games)),
            )
        )

        # Keyboard recognition v4.07
        self.Next_btn.setShortcut("Right")
        self.Prev_btn.setShortcut("Left")
        self.Select_btn.setShortcut("return")

        for indx, current_game_id in enumerate(self.Games):
            self.GameTitles.setItemText(
                indx, _translate(
                    "IconsWindow",
                    f"{indx + 1}: {self.Games[self.game_icons[indx]]} [{current_game_id}]",
                ),
            )

        if len(self.sysGames) > 1:
            self.homebrewLabel.setText(
                _translate("IconsWindow", "System icon: Yes")
            )
            self.bg_change_browse_btn.hide()

        elif self.userHB == "True":
            if "CUSA" in self.game_icons[self.img_counter]:
                enabled = "No"
            else:
                enabled = "Yes"

            self.homebrewLabel.setText(
                _translate("IconsWindow", f"Homebrew icon: {enabled}")
            )
        else:
            self.homebrewLabel.setText(
                _translate("IconsWindow", "Homebrew icon: Turned off")
            )

        if self.Games[self.game_icons[self.img_counter]] in self.exGames:
            self.Ex_In.setText(_translate("IconsWindow", "External"))
        else:
            self.Ex_In.setText(_translate("IconsWindow", "Internal"))

        # Tool tips update v4.61
        self.TTTSS = "<p style='color:Black'>"  # TTTSS = ToolTipTagStyleStart
        self.TTTSE = "</p>"  # TTTSE = ToolTipTagStyleEnd

        self.Next_btn.setToolTip(self.TTTSS + "Next Game" + self.TTTSE)
        self.Prev_btn.setToolTip(self.TTTSS + "Previous Game" + self.TTTSE)
        self.ChangeIcon_btn.setToolTip(
            self.TTTSS + "Pick an Icon for the game" + self.TTTSE
        )
        self.Mask_btn.setToolTip(
            self.TTTSS + "Apply mask" + self.TTTSE
        )
        self.Submit_btn.setToolTip(
            self.TTTSS
            + "Upload the Icon and Pic after you change at least one of them"
            + self.TTTSE
        )
        self.Select_btn.setToolTip(
            self.TTTSS
            + "Click this to select the game from the games list"
            + self.TTTSE
        )
        self.Ex_In.setToolTip(
            self.TTTSS
            + "This is the location where the game is located on your PS4"
            + self.TTTSE
        )
        self.bg_change_browse_btn.setToolTip(
            self.TTTSS + "Pick a background to launch when the game starts" + self.TTTSE
        )
        self.GameTitle.setToolTip(
            self.TTTSS
            + "Some game titles are unknown because they're not legit (homebrews/PS2 converted games etc.)"
            + self.TTTSE
        )
        self.homebrewLabel.setToolTip(
            self.TTTSS
            + "Turned on = Homebrew will be visible and can be changed (turn it on/off from the settings)"
            + self.TTTSE
        )


