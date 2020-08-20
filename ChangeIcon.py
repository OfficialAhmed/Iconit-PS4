from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import Iconit_v3 as main
from PIL import Image
import os

class Ui_ChangeIconWindow(object):
    def setupUi(self, ChangeIconWindow, IP, Port, Games, uFont, uIPath, uDPath, userHB, exGames):
        #Settings
        self.userFont = uFont
        self.userIPath = uIPath
        self.userDPath = uDPath
        self.userHB = userHB

        self.exGames = exGames
        self.IP = IP
        self.Port = Port
        self.temp_path = main.temp_path
        self.img_dir = main.img_dir
        self.setting_path = main.setting_path
        self.Games = Games
        temp = self.temp_path + "MegaSRX\\metadata\\"
        self.CUSA_img = ""
        for i in temp:
            if i == "\\":
                self.CUSA_img += "/"
            else:
                self.CUSA_img += i

        #Get all icon names from local path
        dirs = os.listdir(temp)
        self.imgs = []
        for img in dirs:
            if "png" in img:
                self.imgs.append(img)

        self.changeIconPath = ""
        self.img_limit = len(self.imgs)
        self.img_counter = 0
        self.logging = "* Connected to PS4 : " + self.IP + "* "
        ChangeIconWindow.setObjectName("ChangeIconWindow")
        ChangeIconWindow.resize(966, 505)
        ChangeIconWindow.setMinimumSize(QtCore.QSize(966, 505))
        ChangeIconWindow.setMaximumSize(QtCore.QSize(966, 505))
        ChangeIconWindow.setWindowIcon(QtGui.QIcon(str(os.getcwd()) + "\Data\Pref\ic1.@OfficialAhmed0"))
        self.Icon = QtWidgets.QGraphicsView(ChangeIconWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.Icon.sizePolicy().hasHeightForWidth())
        self.Icon.setGeometry(QtCore.QRect(50, 50, 261, 261))
        self.Icon.setSizePolicy(sizePolicy)
        self.Icon.setMinimumSize(QtCore.QSize(261, 261))
        self.Icon.setMaximumSize(QtCore.QSize(261, 261))
        self.Icon.setBaseSize(QtCore.QSize(10, 10))
        self.Icon.setToolTip("Current Game Icon")
        self.Icon.setStyleSheet("border-image: url(" + self.CUSA_img + self.imgs[0] + ");")
        self.Icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Icon.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Icon.setLineWidth(2)
        self.Icon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Icon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Icon.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Icon.setSceneRect(QtCore.QRectF(0.0, 0.0, 10.0, 10.0))
        self.Icon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Icon.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.Icon.setObjectName("Icon")
        
        self.Background = QtWidgets.QGraphicsView(ChangeIconWindow)
        self.Background.setGeometry(QtCore.QRect(-30, -30, 1000, 540))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMinimumSize(QtCore.QSize(1000, 540))
        self.Background.setMaximumSize(QtCore.QSize(1000, 540))
        self.Background.setStyleSheet("border-image: url(" + self.setting_path +"/Data/Pref/bgImageChange.@OfficialAhmed0);")
        self.Background.setLineWidth(4)
        self.Background.setViewportUpdateMode(QtWidgets.QGraphicsView.NoViewportUpdate)
        self.Background.setObjectName("Background")
        
        font = QtGui.QFont()
        font.setFamily(self.userFont)
        font.setPointSize(12)
        
        self.ChangeIcon_btn = QtWidgets.QPushButton(ChangeIconWindow)
        self.ChangeIcon_btn.setGeometry(QtCore.QRect(49, 367, 120, 51))
        self.ChangeIcon_btn.setFont(font)
        self.ChangeIcon_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeIcon_btn.setObjectName("ChangeIcon_btn")
        self.ChangeIcon_btn.clicked.connect(self.BrowseIcon)

        self.DownloadIcon_btn = QtWidgets.QPushButton(ChangeIconWindow)
        self.DownloadIcon_btn.setGeometry(QtCore.QRect(172, 367, 140, 51))
        self.DownloadIcon_btn.setFont(font)
        self.DownloadIcon_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DownloadIcon_btn.setObjectName("DownloadIcon_btn")
        self.DownloadIcon_btn.clicked.connect(self.DownloadIcon)

        font.setPointSize(16)
        self.Title_label = QtWidgets.QLabel(ChangeIconWindow)
        self.Title_label.setGeometry(QtCore.QRect(50, 10, 281, 31))
        
        self.GameID_label = QtWidgets.QLabel(ChangeIconWindow)
        self.GameID_label.setGeometry(QtCore.QRect(380, 140, 281, 41))
        self.GameID_label.setFont(font)
        self.GameID_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.GameID_label.setObjectName("GameID_label")

        self.GameID = QtWidgets.QLabel(ChangeIconWindow)
        self.GameID.setGeometry(QtCore.QRect(800, 140, 281, 41))
        self.GameID.setFont(font)
        self.GameID.setStyleSheet("color: rgb(255, 255, 255);")
        self.GameID.setObjectName("GameID")
        
        self.Ex_In_label = QtWidgets.QLabel(ChangeIconWindow)
        self.Ex_In_label.setGeometry(QtCore.QRect(380, 180, 281, 41))
        self.Ex_In_label.setFont(font)
        self.Ex_In_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Ex_In_label.setObjectName("Ex_In")
        
        self.Ex_In = QtWidgets.QLabel(ChangeIconWindow)
        self.Ex_In.setGeometry(QtCore.QRect(750, 180, 170, 41))
        self.Ex_In.setFont(font)
        self.Ex_In.setStyleSheet("color: rgb(255, 255, 255);")
        self.Ex_In.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Ex_In.setObjectName("Ex_In")

        self.TotalGames_label = QtWidgets.QLabel(ChangeIconWindow)
        self.TotalGames_label.setGeometry(QtCore.QRect(380, 220, 281, 41))
        self.TotalGames_label.setFont(font)
        self.TotalGames_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.TotalGames_label.setObjectName("TotalGames_label")

        self.TotalGames = QtWidgets.QLabel(ChangeIconWindow)
        self.TotalGames.setGeometry(QtCore.QRect(840, 220, 80, 41))
        self.TotalGames.setFont(font)
        self.TotalGames.setStyleSheet("color: rgb(255, 255, 255);")
        self.TotalGames.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalGames.setObjectName("TotalGames")

        self.IconSize_label = QtWidgets.QLabel(ChangeIconWindow)
        self.IconSize_label.setGeometry(QtCore.QRect(380, 260, 381, 41))
        self.IconSize_label.setFont(font)
        self.IconSize_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.IconSize_label.setObjectName("IconSize_label")
        
        self.IconSize = QtWidgets.QLabel(ChangeIconWindow)
        self.IconSize.setGeometry(QtCore.QRect(640, 260, 280, 41))
        self.IconSize.setFont(font)
        self.IconSize.setStyleSheet("color: rgb(10, 255, 20);")
        self.IconSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IconSize.setObjectName("IconSize")

        font.setPointSize(14)

        self.AccountLabel = QtWidgets.QLabel(ChangeIconWindow)
        self.AccountLabel.setGeometry(QtCore.QRect(555, 10, 200, 31))
        self.AccountLabel.setFont(font)
        self.AccountLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.AccountLabel.setObjectName("AccountLabel")
        self.AccountName = QtWidgets.QLabel(ChangeIconWindow)
        self.AccountName.setGeometry(QtCore.QRect(700, 0, 291, 51))
        self.AccountName.setFont(font)
        self.AccountName.setStyleSheet("color: rgb(255, 255, 255);")
        self.AccountName.setObjectName("AccountName")

        font.setPointSize(18)
        self.Title_label.setFont(font)
        self.Title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_label.setObjectName("Title_label")
        self.Title_label_2 = QtWidgets.QLabel(ChangeIconWindow)
        self.Title_label_2.setGeometry(QtCore.QRect(60, 470, 281, 41))

        font.setBold(True)
        self.GameTitle = QtWidgets.QLabel(ChangeIconWindow)
        self.GameTitle.setGeometry(QtCore.QRect(370, 80, 340, 41))
        self.GameTitle.setFont(font)
        self.GameTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.GameTitle.setObjectName("GameTitle")

        font.setPointSize(8)
        self.Title_label_2.setFont(font)
        self.Title_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title_label_2.setObjectName("Title_label_2")
        
        self.Next_btn = QtWidgets.QToolButton(ChangeIconWindow)
        self.Next_btn.setGeometry(QtCore.QRect(260, 260, 51, 51))
        self.Next_btn.setMouseTracking(False)
        self.Next_btn.setStyleSheet("color: rgb(17, 50, 100);")
        self.Next_btn.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.Next_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Next_btn.setAutoRaise(True)
        self.Next_btn.setArrowType(QtCore.Qt.RightArrow)
        self.Next_btn.setObjectName("Next_btn")

        self.Next_btn.clicked.connect(self.Next)
       
        self.Prev_btn = QtWidgets.QToolButton(ChangeIconWindow)
        self.Prev_btn.setGeometry(QtCore.QRect(50, 260, 51, 51))
        self.Prev_btn.setToolTipDuration(-1)
        self.Prev_btn.setStyleSheet("color: rgb(19, 53, 100);")
        self.Prev_btn.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.Prev_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Prev_btn.setAutoRaise(True)
        self.Prev_btn.setArrowType(QtCore.Qt.LeftArrow)
        self.Prev_btn.setObjectName("Prev_btn")
        self.Prev_btn.clicked.connect(self.Prev)

        font.setPointSize(15)
        self.Submit_btn = QtWidgets.QPushButton(ChangeIconWindow)
        self.Submit_btn.setGeometry(QtCore.QRect(49, 310, 263, 51))
        self.Submit_btn.setFont(font)
        self.Submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Submit_btn.setStyleSheet("")
        self.Submit_btn.setObjectName("Submit_btn")
        self.Submit_btn.setDisabled(True)
        self.Submit_btn.clicked.connect(self.Resize_Upload)

        font.setPointSize(10)
        self.line = QtWidgets.QFrame(ChangeIconWindow)
        self.line.setGeometry(QtCore.QRect(380, 170, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ChangeIconWindow)
        self.line_2.setGeometry(QtCore.QRect(380, 210, 541, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ChangeIconWindow)
        self.line_3.setGeometry(QtCore.QRect(380, 250, 541, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(ChangeIconWindow)
        self.line_4.setGeometry(QtCore.QRect(380, 290, 541, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        
        self.AllGames_label = QtWidgets.QLabel(ChangeIconWindow)
        self.AllGames_label.setGeometry(QtCore.QRect(390, 320, 111, 41))

        self.GameTitles = QtWidgets.QComboBox(ChangeIconWindow)
        self.GameTitles.setGeometry(QtCore.QRect(490, 320, 341, 31))
        self.GameTitles.setFont(font)
        self.GameTitles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameTitles.setStyleSheet("")
        self.GameTitles.setEditable(False)
        self.GameTitles.setMaxVisibleItems(200000)
        self.GameTitles.setMaxCount(200000)
        self.GameTitles.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.GameTitles.setFrame(False)
        self.GameTitles.setObjectName("GameTitles")
        #add items the number of how many games are found 
        for number_of_games in range(len(self.Games)):
            self.GameTitles.addItem("select")

        self.Logs = QtWidgets.QTextEdit(ChangeIconWindow)
        self.Logs.setGeometry(QtCore.QRect(650, 450, 291, 51))

        font.setPointSize(14)
        self.AllGames_label.setFont(font)
        self.AllGames_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.AllGames_label.setObjectName("AllGames_label")
        
        self.Select_btn = QtWidgets.QPushButton(ChangeIconWindow)
        self.Select_btn.setGeometry(QtCore.QRect(830, 319, 61, 33))
        self.Select_btn.clicked.connect(self.Select)

        font.setPointSize(10)
        font.setBold(True)
        self.Select_btn.setFont(font)
        self.Select_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Select_btn.setStyleSheet("")
        self.Select_btn.setObjectName("Select_btn")
        
        self.Logs.setFont(font)
        self.Logs.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.Logs.setFrameShape(QtWidgets.QFrame.Box)
        self.Logs.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Logs.setReadOnly(True)
        self.Logs.setHtml("<p align=\"center\"><span style=\" font-size:9pt;\">"+ self.logging +"</span></p>")
        self.Logs.setObjectName("Logs")
        self.Logs_label = QtWidgets.QLabel(ChangeIconWindow)
        self.Logs_label.setGeometry(QtCore.QRect(600, 450, 51, 41))
        font.setPointSize(14)
        self.Logs_label.setFont(font)
        self.Logs_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Logs_label.setObjectName("Logs_label")
        self.Background.raise_()
        self.Icon.raise_()
        self.ChangeIcon_btn.raise_()
        self.DownloadIcon_btn.raise_()
        self.Title_label.raise_()
        self.Title_label_2.raise_()
        self.Submit_btn.raise_()
        self.Prev_btn.raise_()
        self.Next_btn.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.GameTitle.raise_()
        self.GameID.raise_()
        self.GameID_label.raise_()
        self.Ex_In.raise_()
        self.Ex_In_label.raise_()
        self.TotalGames.raise_()
        self.TotalGames_label.raise_()
        self.IconSize.raise_()
        self.IconSize_label.raise_()
        self.AccountLabel.raise_()
        self.AccountName.raise_()
        self.AllGames_label.raise_()
        self.Select_btn.raise_()
        self.GameTitles.raise_()
        self.Logs.raise_()
        self.Logs_label.raise_()

        self.retranslateUi(ChangeIconWindow)
        self.GameTitles.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ChangeIconWindow)

    def retranslateUi(self, ChangeIconWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangeIconWindow.setWindowTitle(_translate("ChangeIconWindow", "Iconit v4.01"))
        self.ChangeIcon_btn.setText(_translate("ChangeIconWindow", "Change Icon..."))
        self.DownloadIcon_btn.setText(_translate("ChangeIconWindow", "Download Icon..."))
        self.Title_label.setText(_translate("ChangeIconWindow", "Change Game Icon"))
        self.Title_label_2.setText(_translate("ChangeIconWindow", "Created by @OfficialAhmed0"))
        self.Next_btn.setToolTip(_translate("ChangeIconWindow", "Next Game Icon"))
        self.Next_btn.setText(_translate("ChangeIconWindow", "Browse Icon ..."))
        self.Prev_btn.setToolTip(_translate("ChangeIconWindow", "Previous Game Icon"))
        self.Prev_btn.setText(_translate("ChangeIconWindow", "Browse Icon ..."))
        self.Submit_btn.setText(_translate("ChangeIconWindow", "Resize && Upload"))
        self.GameTitle.setText(_translate("ChangeIconWindow", self.Games[self.imgs[self.img_counter][:-4]]))
        self.GameID_label.setText(_translate("ChangeIconWindow", "Game ID:"))
        self.GameID.setText(_translate("ChangeIconWindow", self.imgs[self.img_counter][:-4]))
        self.Ex_In_label.setText(_translate("ChangeIconWindow", "External / Internal:"))
        self.TotalGames_label.setText(_translate("ChangeIconWindow", "Total Games:"))
        self.TotalGames.setText(_translate("ChangeIconWindow", str(self.img_counter + 1) + "/" + str(len(self.Games))))
        self.IconSize_label.setText(_translate("ChangeIconWindow", "Min. icon size(512x512):"))
        self.IconSize.setText(_translate("ChangeIconWindow", "Current Icon size(512x512)"))
        self.AccountLabel.setText(_translate("ChangeIconWindow", "Homebrew Icon: "))
        self.AllGames_label.setText(_translate("ChangeIconWindow", "All Games"))
        self.Select_btn.setText(_translate("ChangeIconWindow", "Select"))
        self.Logs_label.setText(_translate("ChangeIconWindow", "Logs"))

        for i in range(len(self.Games)):
            self.GameTitles.setItemText(i, _translate("ChangeIconWindow", " "*15 + self.Games[self.imgs[i][:-4]]))

        if self.userHB == "True":
            self.AccountName.setText(_translate("ChangeIconWindow", "No"))
        else:
            self.AccountName.setText(_translate("ChangeIconWindow", "Turned off"))

        if self.Games[self.imgs[self.img_counter][:-4]] in self.exGames:
            self.Ex_In.setText(_translate("ChangeIconWindow", "External"))
        else:
            self.Ex_In.setText(_translate("ChangeIconWindow", "Internal"))

    def UpdateLogs(self):
        self.Logs.setHtml("<p align=\"center\"><span style=\" font-size:9pt;\">"+ self.logging +"</span></p>")
        self.Logs.moveCursor(QtGui.QTextCursor.End)

    def UpdateInfo(self, CustomImgSelected = False):
        self.Submit_btn.setDisabled(True)
        current_img_path = self.CUSA_img + self.imgs[self.img_counter]
        GameTitle = self.Games[self.imgs[self.img_counter][:-4]]

        self.Icon.setStyleSheet("border-image: url(" + current_img_path + ");")
        self.GameTitle.setText(GameTitle)
        self.GameID.setText(self.imgs[self.img_counter][:-4])
        self.CheckImg(current_img_path)

        #If Custom image selected by choosing image manually
        if CustomImgSelected:
            self.TotalGames.setText(str(self.GameTitles.currentIndex()+1) + "/" + str(len(self.Games)))
        else:
            self.TotalGames.setText(str(self.img_counter + 1) + "/" + str(len(self.Games)))
        #Check homebrew
        if self.userHB == "True":
            if "CUSA" in self.imgs[self.img_counter][:-4]:
                self.AccountName.setText("No")
            else:
                self.AccountName.setText("Yes")
        #Change External or Internal
        if self.imgs[self.img_counter][:-4] in self.exGames:
            self.Ex_In.setText("External")
        else:
            self.Ex_In.setText("Internal")

    def Next(self):
        if self.img_counter < self.img_limit-1:
            self.img_counter += 1
            if self.img_counter < self.img_limit and self.img_counter >= 0:
                self.UpdateInfo()

    def Prev(self):
        if self.img_counter > 0 and self.img_counter <= self.img_limit:
            self.img_counter -= 1
            self.UpdateInfo()

    def Select(self):
        selected_Game = self.GameTitles.currentText()[15:]
        self.img_counter = self.GameTitles.currentIndex()
        self.UpdateInfo(CustomImgSelected = True)
        
    def CheckImg(self, path):
        icon = Image.open(path)
        size = icon.size
        if size[0] == 512 and size[1] == 512:
            self.IconSize.setStyleSheet("color: rgb(10, 255, 20);")
            self.IconSize.setText("Current Icon size(" + str(size[0]) + "x" + str(size[1]) + ")")
        elif (size[0] and size[1] > 512) or (size[0] == 512 and size[1] > 512) or (size[0] > 512 and size[1] == 512):
            self.IconSize.setStyleSheet("color: rgb(250, 150, 0);")
            self.IconSize.setText("Current Icon size(" + str(size[0]) + "x" + str(size[1]) + ")")
            self.logging += "  (" + str(size[0]) + "x" + str(size[1]) + ") Image can be resized |"
            self.UpdateLogs()
        else:
            self.IconSize.setStyleSheet("color: rgb(255, 10, 20);")
            self.IconSize.setText("Current Icon size(" + str(size[0]) + "x" + str(size[1]) + ")")
            self.Submit_btn.setDisabled(True)
            self.logging += "  (" + str(size[0]) + "x" + str(size[1]) + ") Image cannot be resized |"
            self.UpdateLogs()

    def BrowseIcon(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.userIPath)

        img, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Choose the icon to upload", "", "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg);; icon(*.ico)", options=options)
        if img:
            self.Submit_btn.setDisabled(False)
            self.Icon.setStyleSheet("border-image: url(" + img + ");")
            self.CheckImg(img)
            self.changeIconPath = img

    def DownloadIcon(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.userDPath)

        path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Where to Download?", "Icon.png", "PNG (*.png)", options=options)
        if path:
            try:
                import shutil
                shutil.copy(self.CUSA_img + self.imgs[self.img_counter], path)
                self.logging += "Downloaded " + self.Games[self.imgs[self.img_counter][:-4]] + " Icon | "
                self.UpdateLogs()
            except Exception as e:
                self.logging += "Error while Downloading " + self.Games[self.imgs[self.img_counter][:-4]] + " " + str(e) + " | "
                self.UpdateLogs()

    def Resize_Upload(self):
        import Confirm
        self.Submit_btn.setEnabled(False)
        Current_CUSA = self.imgs[self.img_counter][:-4]
        self.windo = QtWidgets.QWidget()
        self.ui = Confirm.Ui_ConfirmWindow()
        self.ui.setupUi(self.windo, self.changeIconPath, self.IP, self.Port, Current_CUSA, "Iconit", self.exGames, None)
        self.windo.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangeIconWindow = QtWidgets.QWidget()
    ui = Ui_ChangeIconWindow()
    ui.setupUi(ChangeIconWindow)
    ChangeIconWindow.show()
    sys.exit(app.exec_())
