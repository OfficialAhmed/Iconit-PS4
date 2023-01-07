from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ctypes
import json
from environment import Environment
myappid = "mycompany.myproduct.subproduct.version"  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Ui_ChangeAvatarWin(Environment):
    def __init__(self) -> None:
        super().__init__()
        
    def setupUi(self, ChangeAvatarWin, allUsers, IP, Port, w, h):
        self.ver = self.get_update_version()
        self.screenWidth = w
        self.screenHeight = h

        self.IP = IP
        self.Port = Port
        self.appPath = str(os.getcwd())
        self.AppSettingDir = self.appPath + "\\Data\\"
        self.dataPath = ""
        for i in self.AppSettingDir:
            if i == "\\":
                self.dataPath += "/"
            else:
                self.dataPath += i

        # Default Directories for Browse window
        self.userFont = "Arial"
        self.userIPath = self.appPath
        self.userDPath = self.appPath
        try:
            with open(self.AppSettingDir + "Pref\\pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2:-1]
                self.userIPath = content[2][6:-1]
                self.userDPath = content[3][6:-1]
        except Exception as e:
            self.logIt(str(e), "Warning")

        self.user = allUsers
        self.numOfUsers = len(self.user)
        self.currentUserCounter = 0
        self.CheckAvatar = False
        self.avatar = False
        self.avatar = ""
        self.iconPath = ""
        self.originalAvatar = (
            self.AppSettingDir
            + "prxUserMeta\MegaSRX\metaprodata\\"
            + self.user[self.currentUserCounter]
            + "Original.png"
        )

        # v4.05 new UI
        ChangeAvatarWin.setObjectName("ChangeAvatarWin")
        ChangeAvatarWin.resize(1080, 720)
        ChangeAvatarWin.setWindowIcon(
            QtGui.QIcon(self.appPath + "\Data\Pref\ic1.@OfficialAhmed0")
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChangeAvatarWin.sizePolicy().hasHeightForWidth())
        ChangeAvatarWin.setSizePolicy(sizePolicy)
        ChangeAvatarWin.setMinimumSize(QtCore.QSize(900, 670))
        self.formLayout = QtWidgets.QFormLayout(ChangeAvatarWin)
        self.formLayout.setObjectName("formLayout")
        self.TopLayout = QtWidgets.QFormLayout()
        self.TopLayout.setContentsMargins(10, 20, 10, -1)
        self.TopLayout.setObjectName("TopLayout")
        self.WinTitle = QtWidgets.QLabel(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WinTitle.sizePolicy().hasHeightForWidth())
        self.WinTitle.setSizePolicy(sizePolicy)
        self.WinTitle.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.WinTitle.setFont(font)
        self.WinTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.WinTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.WinTitle.setObjectName("WinTitle")
        self.TopLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.WinTitle)
        self.line_2 = QtWidgets.QFrame(ChangeAvatarWin)
        self.line_2.setMinimumSize(QtCore.QSize(4000, 1))
        self.line_2.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.AppSettingDir + "Pref\\White.@OfficialAhmed0")
            + ");"
        )
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.TopLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_2)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.TopLayout)
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.setContentsMargins(10, 30, -1, 10)
        self.LeftLayout.setSpacing(5)
        self.LeftLayout.setObjectName("LeftLayout")
        self.ChangeAvatar = QtWidgets.QGraphicsView(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChangeAvatar.sizePolicy().hasHeightForWidth())
        self.ChangeAvatar.setSizePolicy(sizePolicy)
        self.ChangeAvatar.setMinimumSize(QtCore.QSize(300, 340))
        self.ChangeAvatar.setStyleSheet(
            "border-image: url("
            + self.dataPath
            + "prxUserMeta//MegaSRX//metaprodata//"
            + str(self.user[0])
            + ".png);"
        )
        self.ChangeAvatar.setObjectName("ChangeAvatar")
        self.LeftLayout.addWidget(self.ChangeAvatar)
        self.Change_DownloadBtnLayout = QtWidgets.QFormLayout()
        self.Change_DownloadBtnLayout.setContentsMargins(-1, -1, -1, 0)
        self.Change_DownloadBtnLayout.setVerticalSpacing(3)
        self.Change_DownloadBtnLayout.setObjectName("Change_DownloadBtnLayout")
        self.Change_btn = QtWidgets.QPushButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Change_btn.sizePolicy().hasHeightForWidth())
        self.Change_btn.setSizePolicy(sizePolicy)
        self.Change_btn.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Change_btn.setFont(font)
        self.Change_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Change_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Change_btn.setObjectName("Change_btn")
        self.Change_DownloadBtnLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.Change_btn
        )
        self.Download_btn = QtWidgets.QPushButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Download_btn.sizePolicy().hasHeightForWidth())
        self.Download_btn.setSizePolicy(sizePolicy)
        self.Download_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Download_btn.setFont(font)
        self.Download_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Download_btn.setObjectName("Download_btn")
        self.Change_DownloadBtnLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.Download_btn
        )
        self.Prev_btn = QtWidgets.QToolButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Prev_btn.sizePolicy().hasHeightForWidth())
        self.Prev_btn.setSizePolicy(sizePolicy)
        self.Prev_btn.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Prev_btn.setFont(font)
        self.Prev_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_btn.setAutoFillBackground(False)
        self.Prev_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Prev_btn.setArrowType(QtCore.Qt.LeftArrow)
        self.Prev_btn.setObjectName("Prev_btn")
        self.Change_DownloadBtnLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.Prev_btn
        )
        self.Next_btn = QtWidgets.QToolButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Next_btn.sizePolicy().hasHeightForWidth())
        self.Next_btn.setSizePolicy(sizePolicy)
        self.Next_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Next_btn.setFont(font)
        self.Next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Next_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Next_btn.setAutoRaise(False)
        self.Next_btn.setArrowType(QtCore.Qt.RightArrow)
        self.Next_btn.setObjectName("Next_btn")
        self.Change_DownloadBtnLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.Next_btn
        )
        self.LeftLayout.addLayout(self.Change_DownloadBtnLayout)
        self.ResizeUpload_btn = QtWidgets.QPushButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ResizeUpload_btn.sizePolicy().hasHeightForWidth()
        )
        self.ResizeUpload_btn.setSizePolicy(sizePolicy)
        self.ResizeUpload_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ResizeUpload_btn.setFont(font)
        self.ResizeUpload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResizeUpload_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.ResizeUpload_btn.setObjectName("ResizeUpload_btn")
        self.LeftLayout.addWidget(self.ResizeUpload_btn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.LeftLayout)
        self.RightLayout = QtWidgets.QFormLayout()
        self.RightLayout.setContentsMargins(10, 60, 20, -1)
        self.RightLayout.setObjectName("RightLayout")
        self.AccountName = QtWidgets.QLabel(ChangeAvatarWin)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.AccountName.setFont(font)
        self.AccountName.setStyleSheet("color:rgb(255,255,255);")
        self.AccountName.setFrameShape(QtWidgets.QFrame.Box)
        self.AccountName.setAlignment(QtCore.Qt.AlignCenter)
        self.AccountName.setObjectName("AccountName")
        self.RightLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.AccountName
        )
        self.AccountID_label = QtWidgets.QLabel(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.AccountID_label.sizePolicy().hasHeightForWidth()
        )
        self.AccountID_label.setSizePolicy(sizePolicy)
        self.AccountID_label.setMinimumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.AccountID_label.setFont(font)
        self.AccountID_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.AccountID_label.setFrameShape(QtWidgets.QFrame.Box)
        self.AccountID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.AccountID_label.setObjectName("AccountID_label")
        self.RightLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.AccountID_label
        )
        self.AccountID = QtWidgets.QLabel(ChangeAvatarWin)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AccountID.setFont(font)
        self.AccountID.setStyleSheet("color:rgb(255, 255, 255);")
        self.AccountID.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.AccountID.setObjectName("AccountID")
        self.RightLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AccountID)
        self.line_3 = QtWidgets.QFrame(ChangeAvatarWin)
        self.line_3.setMinimumSize(QtCore.QSize(30, 3))
        self.line_3.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.AppSettingDir + "Pref\\White.@OfficialAhmed0")
            + ");"
        )
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.RightLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.TotalAccount_label = QtWidgets.QLabel(ChangeAvatarWin)
        self.TotalAccount_label.setMinimumSize(QtCore.QSize(190, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TotalAccount_label.setFont(font)
        self.TotalAccount_label.setStyleSheet("color:rgb(255, 255, 255);")
        self.TotalAccount_label.setFrameShape(QtWidgets.QFrame.Box)
        self.TotalAccount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalAccount_label.setObjectName("TotalAccount_label")
        self.RightLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.TotalAccount_label
        )
        self.TotalAccounts = QtWidgets.QLabel(ChangeAvatarWin)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TotalAccounts.setFont(font)
        self.TotalAccounts.setStyleSheet("color:rgb(255, 255, 255);")
        self.TotalAccounts.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.TotalAccounts.setObjectName("TotalAccounts")
        self.RightLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.TotalAccounts
        )
        self.line_4 = QtWidgets.QFrame(ChangeAvatarWin)
        self.line_4.setMinimumSize(QtCore.QSize(100, 3))
        self.line_4.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.AppSettingDir + "Pref\\White.@OfficialAhmed0")
            + ");"
        )
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.RightLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(0, 20, 10, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Originalcon = QtWidgets.QGraphicsView(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Originalcon.sizePolicy().hasHeightForWidth())
        self.Originalcon.setSizePolicy(sizePolicy)
        self.Originalcon.setMinimumSize(QtCore.QSize(0, 265))
        self.Originalcon.setStyleSheet(
            "border-image: url("
            + self.convert2Url(self.AppSettingDir + "Pref\\White.@OfficialAhmed0")
            + ");"
        )
        self.Originalcon.setObjectName("Originalcon")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.Originalcon
        )
        self.RightLayout.setLayout(
            5, QtWidgets.QFormLayout.LabelRole, self.formLayout_2
        )
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, 70, -1, -1)
        self.formLayout_3.setHorizontalSpacing(4)
        self.formLayout_3.setVerticalSpacing(5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.firstName_label = QtWidgets.QLabel(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.firstName_label.sizePolicy().hasHeightForWidth()
        )
        self.firstName_label.setSizePolicy(sizePolicy)
        self.firstName_label.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firstName_label.setFont(font)
        self.firstName_label.setStyleSheet("color : rgb(255, 255, 255);")
        self.firstName_label.setObjectName("firstName_label")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.firstName_label
        )
        self.firstName = QtWidgets.QLineEdit(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstName.sizePolicy().hasHeightForWidth())
        font.setPointSize(13)
        self.firstName.setFont(font)
        self.firstName.setStyleSheet("color:rgb(255, 255, 255);")
        self.firstName.setSizePolicy(sizePolicy)
        self.firstName.setMinimumSize(QtCore.QSize(0, 30))
        self.firstName.setMaxLength(12)
        self.firstName.setAlignment(QtCore.Qt.AlignCenter)
        self.firstName.setClearButtonEnabled(True)
        self.firstName.setObjectName("firstName")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstName)
        self.lastName_label = QtWidgets.QLabel(ChangeAvatarWin)
        self.lastName_label.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lastName_label.setFont(font)
        self.lastName_label.setStyleSheet("color : rgb(255, 255, 255);")
        self.lastName_label.setObjectName("lastName_label")
        self.formLayout_3.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lastName_label
        )
        self.lastName = QtWidgets.QLineEdit(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastName.sizePolicy().hasHeightForWidth())
        font.setPointSize(13)
        self.lastName.setFont(font)
        self.lastName.setStyleSheet("color:rgb(255, 255, 255);")
        self.lastName.setSizePolicy(sizePolicy)
        self.lastName.setMinimumSize(QtCore.QSize(0, 30))
        self.lastName.setMaxLength(12)
        self.lastName.setAlignment(QtCore.Qt.AlignCenter)
        self.lastName.setClearButtonEnabled(True)
        self.lastName.setObjectName("lastName")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastName)
        self.label1 = QtWidgets.QLabel(ChangeAvatarWin)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:rgb(255, 255, 255);")
        self.label1.setObjectName("label1")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label1)
        self.label2 = QtWidgets.QLabel(ChangeAvatarWin)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color:rgb(255, 255, 255);")
        self.label2.setObjectName("label2")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label2)
        self.Revert_btn = QtWidgets.QPushButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Revert_btn.sizePolicy().hasHeightForWidth())
        self.Revert_btn.setSizePolicy(sizePolicy)
        self.Revert_btn.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Revert_btn.setFont(font)
        self.Revert_btn.setStyleSheet("color:rgb(255, 255, 255);")
        self.Revert_btn.setObjectName("Revert_btn")
        self.Revert_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.Revert_btn)
        self.Rename_btn = QtWidgets.QPushButton(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rename_btn.sizePolicy().hasHeightForWidth())
        self.Rename_btn.setSizePolicy(sizePolicy)
        self.Rename_btn.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Rename_btn.setFont(font)
        self.Rename_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Rename_btn.setStyleSheet("color:rgb(255, 255, 255);")
        self.Rename_btn.setObjectName("Rename_btn")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Rename_btn)
        self.line = QtWidgets.QFrame(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(50, 0))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.RightLayout.setLayout(
            5, QtWidgets.QFormLayout.FieldRole, self.formLayout_3
        )
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.RightLayout)
        self.BottomLayout = QtWidgets.QVBoxLayout()
        self.BottomLayout.setContentsMargins(20, 10, 20, 0)
        self.BottomLayout.setObjectName("BottomLayout")
        self.line_6 = QtWidgets.QFrame(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setMinimumSize(QtCore.QSize(4000, 0))
        self.line_6.setStyleSheet(
            "border-image:url("
            + self.convert2Url(self.AppSettingDir + "Pref\\White.@OfficialAhmed0")
            + ");"
        )
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.BottomLayout.addWidget(self.line_6)
        self.CreditsLayout = QtWidgets.QVBoxLayout()
        self.CreditsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.CreditsLayout.setContentsMargins(500, 20, 0, -1)
        self.CreditsLayout.setSpacing(5)
        self.CreditsLayout.setObjectName("CreditsLayout")
        self.Title_label_2 = QtWidgets.QLabel(ChangeAvatarWin)
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
        self.Title_label_2.setStyleSheet("")
        self.Title_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Title_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Title_label_2.setLineWidth(1)
        self.Title_label_2.setOpenExternalLinks(True)
        self.Title_label_2.setObjectName("Title_label_2")
        self.CreditsLayout.addWidget(self.Title_label_2)
        self.SupportMe = QtWidgets.QLabel(ChangeAvatarWin)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SupportMe.sizePolicy().hasHeightForWidth())
        self.SupportMe.setSizePolicy(sizePolicy)
        self.SupportMe.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SupportMe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SupportMe.setStyleSheet("")
        self.SupportMe.setFrameShape(QtWidgets.QFrame.Box)
        self.SupportMe.setOpenExternalLinks(True)
        self.SupportMe.setObjectName("SupportMe")
        self.CreditsLayout.addWidget(self.SupportMe)
        self.BottomLayout.addLayout(self.CreditsLayout)
        self.formLayout.setLayout(
            3, QtWidgets.QFormLayout.SpanningRole, self.BottomLayout
        )

        # Change bg accroding to user Resolution
        if self.screenWidth <= 1366:
            background = "SDbg.@OfficialAhmed0"
        elif self.screenWidth <= 1920:
            background = "HDbg.@OfficialAhmed0"
        elif self.screenWidth <= 2048:
            background = "2kbg.@OfficialAhmed0"
        else:
            background = "4kbg.@OfficialAhmed0"
        ChangeAvatarWin.setStyleSheet(
            "background-image: url("
            + self.convert2Url(self.AppSettingDir + "Pref\\" + background)
            + ");"
        )

        # Buttons back-end
        self.Next_btn.clicked.connect(self.Next)
        self.Prev_btn.clicked.connect(self.Prev)
        self.ResizeUpload_btn.clicked.connect(self.resizeUpload)
        self.Change_btn.clicked.connect(self.Change)
        self.Download_btn.clicked.connect(self.Download)
        self.Revert_btn.clicked.connect(self.Revert)
        self.Rename_btn.clicked.connect(self.RenameAccount)

        # Get First/Last name for first profile
        try:
            jsonFile = open(
                self.AppSettingDir
                + "prxUserMeta\MegaSRX\metaprodata\\"
                + self.user[self.currentUserCounter]
                + ".json",
                "r",
            )
            readJson = json.load(jsonFile)
            jsonFile.close()

            self.AccountName.setText(readJson["firstName"] + " " + readJson["lastName"])
        except Exception as e:
            self.logIt(str(e), "Warning")
        # Original Icon
        if os.path.isfile(
            self.dataPath
            + "prxUserMeta//MegaSRX//metaprodata//"
            + self.user[self.currentUserCounter]
            + "Original.png"
        ):
            self.Originalcon.setStyleSheet(
                "border-image: url("
                + self.dataPath
                + "prxUserMeta//MegaSRX//metaprodata//"
                + self.user[self.currentUserCounter]
                + "Original.png);"
            )
            self.label2.setText("Do you want the")
            self.label1.setText("original profile icon?")
            self.Revert_btn.setEnabled(True)

        else:
            # Couldn't get original image from Sony server while caching
            self.Originalcon.setStyleSheet(
                "border-image: url(" + self.dataPath + "pref//error.@OfficialAhmed0);"
            )
            self.label2.setText("Ops! This account doesn't have")
            self.label1.setText("an original avatar.")
            self.Revert_btn.setEnabled(False)

        self.retranslateUi(ChangeAvatarWin)
        QtCore.QMetaObject.connectSlotsByName(ChangeAvatarWin)

    def retranslateUi(self, ChangeAvatarWin):
        _translate = QtCore.QCoreApplication.translate
        ChangeAvatarWin.setWindowTitle(
            _translate(
                "ChangeAvatarWin",
                "Change Avatar / Iconit v"
                + str(self.ver)
                + " ("
                + str(self.get_update_release_date())
                + ")",
            )
        )
        self.WinTitle.setText(_translate("ChangeAvatarWin", "Change Avatar"))
        self.Change_btn.setText(_translate("ChangeAvatarWin", "Change Avatar"))
        self.Download_btn.setText(_translate("ChangeAvatarWin", "Download Avatar"))
        self.Prev_btn.setText(_translate("ChangeAvatarWin", "Previous"))
        self.Next_btn.setText(_translate("ChangeAvatarWin", "Next"))
        self.ResizeUpload_btn.setText(_translate("ChangeAvatarWin", "Resize && Upload"))
        self.AccountName.setText(_translate("ChangeAvatarWin", self.getAccountName()))
        self.AccountID_label.setText(_translate("ChangeAvatarWin", "AccountID:"))
        self.TotalAccount_label.setText(_translate("ChangeAvatarWin", "Total Accounts"))
        self.Revert_btn.setText(_translate("ChangeAvatarWin", "Revert to original"))
        self.label1.setText(
            _translate("ChangeAvatarWin", "This is the Original Avatar.")
        )
        self.label2.setText(
            _translate(
                "ChangeAvatarWin", "Do you want to revert back to original avatar?"
            )
        )
        self.firstName_label.setText(_translate("ChangeAvatarWin", "First name: "))
        self.firstName.setPlaceholderText(_translate("ChangeAvatarWin", ""))
        self.lastName_label.setText(_translate("ChangeAvatarWin", "Last name: "))
        self.lastName.setPlaceholderText(_translate("ChangeAvatarWin", ""))
        self.Rename_btn.setText(_translate("ChangeAvatarWin", "Rename account"))
        self.Title_label_2.setText(
            _translate(
                "ChangeAvatarWin",
                '<html><head/><body><p align="center"><a href="https://twitter.com/OfficialAhmed0"><span style=" font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">Created By @OfficialAhmed0</span></a></p></body></html>',
            )
        )
        self.SupportMe.setText(
            _translate(
                "ChangeAvatarWin",
                '<html><head/><body><p align="center"><a href="https://www.paypal.com/paypalme/Officialahmed0"><span style=" font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">Support me (PayPal)</span></a></p></body></html>',
            )
        )
        self.AccountID.setText(_translate("ChangeAvatarWin", self.user[0]))
        self.TotalAccounts.setText(_translate("ChangeAvatarWin", "1/4"))

        # Keyboard recognition v4.07
        self.Next_btn.setShortcut("Right")
        self.Prev_btn.setShortcut("Left")

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
            )

    def convert2Url(self, path):
        result = ""
        for i in path:
            if i == "\\":
                result += "/"
            else:
                result += i
        return result

    def RenameAccount(self):
        from ftplib import FTP

        ftp = FTP()
        try:
            fn = self.firstName.text()
            ln = self.lastName.text()
            if fn == "":
                fn = "Unknown"
            if ln == "":
                ln = "Username"
            file = (
                self.AppSettingDir
                + "prxUserMeta\\MegaSRX\\metaprodata\\"
                + self.user[self.currentUserCounter]
                + ".json"
            )
            ftp.set_debuglevel(2)
            ftp.connect(self.IP, int(self.Port))
            ftp.login("", "")
            ftp.cwd(
                "system_data/priv/cache/profile/" + self.user[self.currentUserCounter]
            )
            jsonFile = open(file, "r")
            json_object = json.load(jsonFile)

            json_object["firstName"] = fn
            json_object["lastName"] = ln
            jsonFile.close()

            jsonFile = open(file, "w+")
            json.dump(json_object, jsonFile)
            jsonFile.close()

            with open(file, "rb") as fakeOnlineFile:
                ftp.storlines("STOR online.json", fakeOnlineFile)
            self.Rename_btn.setStyleSheet("color:rgb(61, 226, 61);")
            self.Rename_btn.setText("Done (Restart required)")
            self.Rename_btn.setDisabled(True)
        except Exception as e:
            self.Rename_btn.setStyleSheet("color:rgb(226, 41, 41);")
            self.Rename_btn.setText("Error check logs file")
            self.logIt(str(e), "error")

    def Revert(self):
        self.CheckAvatar = True
        self.resizeUpload()
        self.CheckAvatar = False

    def getAccountName(self):
        name = ""
        try:
            jsonFile = open(
                self.AppSettingDir
                + "prxUserMeta\MegaSRX\metaprodata\\"
                + self.user[self.currentUserCounter]
                + ".json",
                "r",
            )
            readJson = json.load(jsonFile)
            jsonFile.close()

            name = readJson["firstName"] + " " + readJson["lastName"]
        except Exception as e:
            self.logIt(str(e), "Warning")
        return name

    def UpdateInfo(self):
        try:
            if os.path.isfile(
                self.dataPath
                + "prxUserMeta//MegaSRX//metaprodata//"
                + self.user[self.currentUserCounter]
                + "Original.png"
            ):
                self.Originalcon.setStyleSheet(
                    "border-image: url("
                    + self.dataPath
                    + "prxUserMeta//MegaSRX//metaprodata//"
                    + self.user[self.currentUserCounter]
                    + "Original.png);"
                )
                self.label1.setText("Do you want the")
                self.label2.setText("original profile icon?")
                self.Revert_btn.setEnabled(True)
                self.avatar = (
                    self.dataPath
                    + "prxUserMeta//MegaSRX//metaprodata//"
                    + self.user[self.currentUserCounter]
                    + "Original.png"
                )
            else:
                # Couldn't get original image from Sony server while caching
                self.Originalcon.setStyleSheet(
                    "border-image: url("
                    + self.dataPath
                    + "pref//error.@OfficialAhmed0);"
                )
                self.label1.setText("Ops! This account doesn't have")
                self.label2.setText("an original avatar.")
                self.Revert_btn.setEnabled(False)
            self.ChangeAvatar.setStyleSheet(
                "border-image: url("
                + self.dataPath
                + "prxUserMeta//MegaSRX//metaprodata//"
                + self.user[self.currentUserCounter]
                + ".png);"
            )
            self.AccountID.setText(self.user[self.currentUserCounter])
            self.AccountName.setText(self.getAccountName())
            self.firstName.setText("")
            self.lastName.setText("")
            self.Rename_btn.setStyleSheet("color:rgb(255, 255, 255);")
            self.Rename_btn.setText("Rename account")
        except Exception as e:
            self.logit(str(e), "error")

    def Next(self):
        if self.currentUserCounter < self.numOfUsers - 1:
            self.ResizeUpload_btn.setEnabled(False)
            self.Rename_btn.setDisabled(False)
            self.currentUserCounter += 1
            # Original Icon
            self.UpdateInfo()
            # End of Original Icon
            self.TotalAccounts.setText(
                str(self.currentUserCounter + 1) + "/" + str(self.numOfUsers)
            )

    def Prev(self):
        if self.currentUserCounter > 0 and self.currentUserCounter < self.numOfUsers:
            self.Rename_btn.setDisabled(False)
            self.TotalAccounts.setText(
                str(self.currentUserCounter) + "/" + str(self.numOfUsers)
            )
            self.currentUserCounter -= 1
            # Original Icon
            self.UpdateInfo()
            # End of Original Icon

    def Download(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        try:
            opt = QtWidgets.QFileDialog.Options()
            opt |= QtWidgets.QFileDialog.DontUseSheet
            dialog = QFileDialog()
            dialog.setOptions(opt)
            dialog.setDirectory(self.userDPath)
            path, _ = QtWidgets.QFileDialog.getSaveFileName(
                None,
                "Where to Download?",
                "MyChangeAvatar.png",
                "PNG (*.png)",
                options=opt,
            )
            if path:
                import shutil

                shutil.copyfile(
                    self.AppSettingDir
                    + "prxUserMeta\\MegaSRX\\metaprodata\\"
                    + self.user[self.currentUserCounter]
                    + ".png",
                    path,
                )
        except Exception as e:
            self.logit(str(e), "error")

    def Change(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        try:
            opt = QtWidgets.QFileDialog.Options()
            opt |= QtWidgets.QFileDialog.DontUseSheet
            dialog = QFileDialog()
            dialog.setOptions(opt)
            dialog.setDirectory(self.userIPath)
            path, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Pick an image greater than (440x440) ...",
                "",
                "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg);; icon(*.ico);; DDS(*.dds)",
                options=opt,
            )
            if path:  # not empty
                import PIL

                valid = False
                image = PIL.Image.open(path)

                if image.size[0] >= 440 or image.size[1] >= 440:
                    if image.size[0] >= 440:
                        if image.size[1] >= 440:
                            valid = True
                    elif image.size[1] >= 440:
                        if image.size[0] >= 440:
                            valid = True

                if valid:
                    self.iconPath = ""
                    for i in path:
                        if i == "\\":
                            self.iconPath += "/"
                        else:
                            self.iconPath += i
                    self.ChangeAvatar.setStyleSheet(
                        "border-image: url(" + self.iconPath + ");"
                    )
                    self.ResizeUpload_btn.setEnabled(True)
                else:
                    self.Error("Invalid icon size")
        except Exception as e:
            self.logit(str(e), "error")

    def resizeUpload(self):
        import Confirm
        import shutil

        try:
            self.ResizeUpload_btn.setEnabled(False)
            if self.CheckAvatar == False:
                self.avatar = self.iconPath
                shutil.copyfile(
                    self.avatar,
                    self.AppSettingDir
                    + "prxUserMeta\MegaSRX\metaprodata\\"
                    + self.user[self.currentUserCounter]
                    + ".png",
                )
            elif self.CheckAvatar == True:
                self.avatar = (
                    self.AppSettingDir
                    + "prxUserMeta\MegaSRX\metaprodata\\"
                    + self.user[self.currentUserCounter]
                    + "Original.png"
                )
                shutil.copyfile(
                    self.avatar,
                    self.AppSettingDir
                    + "prxUserMeta\MegaSRX\metaprodata\\"
                    + self.user[self.currentUserCounter]
                    + ".png",
                )

                path = ""
                for i in self.avatar:
                    if i == "\\":
                        path += "/"
                    else:
                        path += i
                self.ChangeAvatar.setStyleSheet("border-image: url(" + path + ");")

            self.windo = QtWidgets.QWidget()
            self.ui = Confirm.Ui_ConfirmWindow()
            self.ui.setupUi(
                self.windo,
                self.avatar,
                self.IP,
                self.Port,
                "",
                "Profileit",
                "",
                self.user[self.currentUserCounter],
            )
            self.windo.show()
        except Exception as e:
            self.logit(str(e), "error")

    def Error(self, Type):
        import Message

        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        self.ui.setupUi(self.window, Type)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ChangeAvatarWin = QtWidgets.QWidget()
    ui = Ui_ChangeAvatarWin()
    ui.setupUi(ChangeAvatarWin)
    ChangeAvatarWin.show()
    sys.exit(app.exec_())
