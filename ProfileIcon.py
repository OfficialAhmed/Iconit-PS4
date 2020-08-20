from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Ui_ProfileIconWin(object):
    def setupUi(self, ProfileIconWin, allUsers, IP, Port):
        self.IP  = IP
        self.Port = Port
        self.appPath = str(os.getcwd())
        self.AppSettingDir = self.appPath + "\\Data\\"
        self.dataPath = ""
        for i in self.AppSettingDir:
            if i == "\\":
                self.dataPath += "/"
            else:
                self.dataPath += i

        #Default Directories for Browse window
        self.userFont = "Arial"
        self.userIPath = self.appPath
        self.userDPath = self.appPath
        try:
            with open(self.AppSettingDir + "prxUserMeta\\pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2: -1]
                self.userIPath = content[2][6: -1]
                self.userDPath = content[3][6: -1]
        except:
            pass
        self.user = allUsers
        self.numOfUsers = len(self.user)
        self.currentUserCounter = 0
        self.CheckAvatar = False
        self.avatar = False
        self.avatar = ""
        self.iconPath = ""
        self.originalAvatar = self.AppSettingDir + "prxUserMeta\MegaSRX\metaprodata\\" + self.user[self.currentUserCounter] + "Original.png"

        ProfileIconWin.setObjectName("ProfileIconWin")
        ProfileIconWin.resize(720, 520)
        ProfileIconWin.setMinimumSize(QtCore.QSize(720, 520))
        ProfileIconWin.setMaximumSize(QtCore.QSize(720, 520))
        ProfileIconWin.setWindowIcon(QtGui.QIcon(self.appPath + "\Data\Pref\ic1.@OfficialAhmed0"))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        self.Credit = QtWidgets.QLabel(ProfileIconWin)
        self.Credit.setGeometry(QtCore.QRect(40, 460, 101, 41))
        self.AccountID_label = QtWidgets.QLabel(ProfileIconWin)
        self.AccountID_label.setGeometry(QtCore.QRect(300, 150, 141, 51))
        self.AccountID_label.setFont(font)
        self.AccountID_label.setToolTip("")
        self.AccountID_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.AccountID_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AccountID_label.setObjectName("AccountID_label")
        self.TotalAccount_label = QtWidgets.QLabel(ProfileIconWin)
        self.TotalAccount_label.setGeometry(QtCore.QRect(300, 210, 181, 51))
        self.TotalAccount_label.setFont(font)
        self.TotalAccount_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.TotalAccount_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TotalAccount_label.setObjectName("TotalAccount_label")

        self.AccountName = QtWidgets.QLabel(ProfileIconWin)
        self.AccountName.setGeometry(QtCore.QRect(321, 91, 371, 41))
        self.AccountName.setFont(font)
        self.AccountName.setStyleSheet("color: rgb(255, 255, 255);")
        self.AccountName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AccountName.setObjectName("AccountName")

        self.WinTitle = QtWidgets.QLabel(ProfileIconWin)
        self.WinTitle.setGeometry(QtCore.QRect(30, 20, 321, 41))
        self.WinTitle.setFont(font)
        self.WinTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.WinTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.WinTitle.setObjectName("WinTitle")

        self.Next_btn = QtWidgets.QToolButton(ProfileIconWin)
        self.Next_btn.setGeometry(QtCore.QRect(210, 250, 61, 81))
        self.Next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Next_btn.setAutoRaise(True)
        self.Next_btn.setArrowType(QtCore.Qt.RightArrow)
        self.Next_btn.setObjectName("Next_btn")
        self.Prev_btn = QtWidgets.QToolButton(ProfileIconWin)
        self.Prev_btn.setGeometry(QtCore.QRect(30, 250, 61, 81))
        self.Prev_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Prev_btn.setAutoRaise(True)
        self.Prev_btn.setArrowType(QtCore.Qt.LeftArrow)
        self.Prev_btn.setObjectName("Prev_btn")

        self.Next_btn.clicked.connect(self.Next)
        self.Prev_btn.clicked.connect(self.Prev)

        self.TotalAccounts = QtWidgets.QLabel(ProfileIconWin)
        self.TotalAccounts.setGeometry(QtCore.QRect(450, 210, 241, 51))
        self.TotalAccounts.setFont(font)
        self.TotalAccounts.setToolTip("")
        self.TotalAccounts.setStyleSheet("color: rgb(255, 255, 255);")
        self.TotalAccounts.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalAccounts.setObjectName("TotalAccounts")

        self.AccountID = QtWidgets.QLabel(ProfileIconWin)
        self.AccountID.setGeometry(QtCore.QRect(450, 150, 241, 51))
        self.AccountID.setFont(font)
        self.AccountID.setStyleSheet("color: rgb(255, 255, 255);")
        self.AccountID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AccountID.setObjectName("AccountID")

        font.setPointSize(12)
        self.ResizeUpload_btn = QtWidgets.QPushButton(ProfileIconWin)
        self.ResizeUpload_btn.setGeometry(QtCore.QRect(29, 330, 243, 52))
        self.ResizeUpload_btn.setFont(font)
        self.ResizeUpload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResizeUpload_btn.setFlat(False)
        self.ResizeUpload_btn.setEnabled(False)
        self.ResizeUpload_btn.setObjectName("ResizeUpload_btn")
        self.ResizeUpload_btn.clicked.connect(self.resizeUpload)

        self.Change_btn = QtWidgets.QPushButton(ProfileIconWin)
        self.Change_btn.setGeometry(QtCore.QRect(29, 381, 122, 52))
        self.Change_btn.setFont(font)
        self.Change_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Change_btn.setFlat(False)
        self.Change_btn.setObjectName("Change_btn")
        self.Download_btn = QtWidgets.QPushButton(ProfileIconWin)
        self.Download_btn.setGeometry(QtCore.QRect(151, 381, 121, 52))
        self.Download_btn.setFont(font)
        self.Download_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_btn.setFlat(False)
        self.Download_btn.setObjectName("Download_btn")

        self.Change_btn.clicked.connect(self.Change)
        self.Download_btn.clicked.connect(self.Download)

        font.setPointSize(8)
        self.Credit.setFont(font)
        self.Credit.setStyleSheet("color: rgb(255, 255, 255);")
        self.Credit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Credit.setObjectName("Credit")
        self.line_2 = QtWidgets.QFrame(ProfileIconWin)
        self.line_2.setGeometry(QtCore.QRect(300, 190, 391, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ProfileIconWin)
        self.line_3.setGeometry(QtCore.QRect(300, 250, 391, 16))
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(ProfileIconWin)
        self.line_4.setGeometry(QtCore.QRect(0, 445, 741, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(ProfileIconWin)
        self.line_5.setGeometry(QtCore.QRect(0, 50, 741, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(True)
        
        font.setPointSize(10)
        self.Revert_btn = QtWidgets.QPushButton(ProfileIconWin)
        self.Revert_btn.setGeometry(QtCore.QRect(450, 400, 141, 31))
        self.Revert_btn.setFont(font)
        self.Revert_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Revert_btn.setObjectName("Revert_btn")
        self.Revert_btn.clicked.connect(self.Revert)

        self.OriginalProfileIcon_label = QtWidgets.QLabel(ProfileIconWin)
        self.OriginalProfileIcon_label.setGeometry(QtCore.QRect(450, 350, 201, 61))
        self.OriginalProfileIcon_label.setFont(font)
        self.OriginalProfileIcon_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.OriginalProfileIcon_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.OriginalProfileIcon_label.setObjectName("OriginalProfileIcon_label")
        self.DoYouWantThe_label = QtWidgets.QLabel(ProfileIconWin)
        self.DoYouWantThe_label.setGeometry(QtCore.QRect(450, 330, 251, 51))
        self.DoYouWantThe_label.setFont(font)
        self.DoYouWantThe_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.DoYouWantThe_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DoYouWantThe_label.setObjectName("DoYouWantThe_label")

        self.Background = QtWidgets.QGraphicsView(ProfileIconWin)
        self.Background.setGeometry(QtCore.QRect(0, -10, 801, 531))
        self.Background.setMinimumSize(QtCore.QSize(12, 12))
        self.Background.setStyleSheet("border-image: url("+ self.dataPath + "Pref//bgImageChange.@OfficialAhmed0);")
        self.Background.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Background.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Background.setObjectName("Background")

        self.ProfileIcon = QtWidgets.QGraphicsView(ProfileIconWin)
        self.ProfileIcon.setGeometry(QtCore.QRect(30, 80, 241, 251))
        self.ProfileIcon.setObjectName("ProfileIcon")
        self.ProfileIcon.setStyleSheet("border-image: url("+ self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + str(self.user[0]) + ".png);")
        self.Originalcon = QtWidgets.QGraphicsView(ProfileIconWin)
        self.Originalcon.setGeometry(QtCore.QRect(300, 270, 141, 161))
        self.Originalcon.setObjectName("Originalcon")
        #Get First/Last name for first profile
        self.name = ""
        with open(self.AppSettingDir + "prxUserMeta\MegaSRX\metaprodata\\" + self.user[self.currentUserCounter] + ".json") as file:
            reading = file.read()
            start = reading.find("firstName") + 12
            end = reading.find("lastName") - 3
            self.name += reading[start : end] + " "
            start = reading.find("lastName") + 11
            end = reading.find('"', start)
            self.name += reading[start : reading.find('"', start)]
        self.AccountName.setText(self.name)
        #Original Icon
        if os.path.isfile(self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + self.user[self.currentUserCounter] + "Original.png") :
            self.Originalcon.setStyleSheet("border-image: url("+ self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + self.user[self.currentUserCounter] + "Original.png);")
            self.DoYouWantThe_label.setText("Do you want the")
            self.OriginalProfileIcon_label.setText("original profile icon?")
            self.Revert_btn.setEnabled(True)

        else:
            #Couldn't get original image from Sony server while caching
            self.Originalcon.setStyleSheet("border-image: url("+ self.dataPath + "pref//error.@OfficialAhmed0);")
            self.DoYouWantThe_label.setText("Cannot find Original Profile icon.")
            self.OriginalProfileIcon_label.setText("Check Internet connection")
            self.Revert_btn.setEnabled(False)

        self.Credit.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.WinTitle.raise_()
        self.Next_btn.raise_()
        self.Prev_btn.raise_()
        self.AccountID.raise_()
        self.Change_btn.raise_()
        self.Revert_btn.raise_()
        self.AccountName.raise_()
        self.Download_btn.raise_()
        self.TotalAccounts.raise_()
        self.AccountID_label.raise_()
        self.ResizeUpload_btn.raise_()
        self.DoYouWantThe_label.raise_()
        self.TotalAccount_label.raise_()
        self.OriginalProfileIcon_label.raise_()

        self.retranslateUi(ProfileIconWin)
        QtCore.QMetaObject.connectSlotsByName(ProfileIconWin)

    def retranslateUi(self, ProfileIconWin):
        _translate = QtCore.QCoreApplication.translate
        ProfileIconWin.setWindowTitle(_translate("ProfileIconWin", "Iconit v4.01"))
        self.AccountID_label.setText(_translate("ProfileIconWin", "Account Id: "))
        self.TotalAccount_label.setText(_translate("ProfileIconWin", "Total Accounts: "))
        self.Next_btn.setText(_translate("ProfileIconWin", "..."))
        self.Prev_btn.setText(_translate("ProfileIconWin", "..."))
        self.ResizeUpload_btn.setText(_translate("ProfileIconWin", "Resize && upload"))
        self.Originalcon.setToolTip(_translate("ProfileIconWin", "This profile icon was chosen from PSN before jailbreaking the PS4"))
        self.Change_btn.setText(_translate("ProfileIconWin", "Change"))
        self.Download_btn.setText(_translate("ProfileIconWin", "Download"))
        self.WinTitle.setText(_translate("ProfileIconWin", "Change Profile Icon"))
        self.Credit.setToolTip(_translate("ProfileIconWin", "Any bugs Tweet me OfficialAhmed"))
        self.Credit.setText(_translate("ProfileIconWin", " @OfficialAhmed0"))
        self.Revert_btn.setText(_translate("ProfileIconWin", "Revert to original"))
        self.AccountID.setText(_translate("ProfileIconWin", self.user[0]))
        self.TotalAccounts.setText(_translate("ProfileIconWin", "1/4"))

    def Revert(self):
        self.CheckAvatar = True
        self.resizeUpload()
        self.CheckAvatar = False

    def getAccountName(self):
        name = ""
        file = open(self.AppSettingDir + "prxUserMeta\MegaSRX\metaprodata\\" + self.user[self.currentUserCounter] + ".json")
        reading = file.read()
        start = reading.find("firstName") + 12
        end = reading.find("lastName") - 3
        name += reading[start : end] + " "
        start = reading.find("lastName") + 11
        end = reading.find('"', start)
        name += reading[start : reading.find('"', start)]
        file.close()
        return name

    def UpdateInfo(self):
        if os.path.isfile(self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + self.user[self.currentUserCounter] + "Original.png") :
            self.Originalcon.setStyleSheet("border-image: url("+ self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + self.user[self.currentUserCounter] + "Original.png);")
            self.DoYouWantThe_label.setText("Do you want the")
            self.OriginalProfileIcon_label.setText("original profile icon?")
            self.Revert_btn.setEnabled(True)
            self.avatar = self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + self.user[self.currentUserCounter] + "Original.png"
        else:
            #Couldn't get original image from Sony server while caching
            self.Originalcon.setStyleSheet("border-image: url("+ self.dataPath + "pref//error.@OfficialAhmed0);")
            self.DoYouWantThe_label.setText("Cannot find Original Profile icon.")
            self.OriginalProfileIcon_label.setText("Check Internet connection")
            self.Revert_btn.setEnabled(False)
        self.ProfileIcon.setStyleSheet("border-image: url("+ self.dataPath + "prxUserMeta//MegaSRX//metaprodata//" + self.user[self.currentUserCounter] + ".png);")
        self.AccountID.setText(self.user[self.currentUserCounter])
        self.AccountName.setText(self.getAccountName())

    def Next(self):
        if self.currentUserCounter < self.numOfUsers-1:
            self.ResizeUpload_btn.setEnabled(False)
            self.currentUserCounter += 1
            #Original Icon
            self.UpdateInfo()
            #End of Original Icon
            self.TotalAccounts.setText(str(self.currentUserCounter + 1) + "/" + str(self.numOfUsers))

    def Prev(self):
        if self.currentUserCounter > 0 and self.currentUserCounter < self.numOfUsers:
            self.TotalAccounts.setText(str(self.currentUserCounter) + "/" + str(self.numOfUsers))
            self.currentUserCounter -= 1
            #Original Icon
            self.UpdateInfo()
            #End of Original Icon

    def Download(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.userDPath)
        path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Where to Download?", "MyProfileIcon.png", "PNG (*.png)", options=opt)
        if path:
            import shutil
            shutil.copyfile(self.AppSettingDir + "prxUserMeta\\MegaSRX\\metaprodata\\" + self.user[self.currentUserCounter] + ".png", path)

    def Change(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.userIPath)
        path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Pick an image greater than (440x440) ...", "", "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg);; icon(*.ico);; DDS(*.dds)", options=opt)
        if path:#not empty
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
                self.ProfileIcon.setStyleSheet("border-image: url("+ self.iconPath + ");")
                self.ResizeUpload_btn.setEnabled(True)
            else:
                self.Error("Invalid icon size")

    def resizeUpload(self):
        import Confirm, shutil
        self.ResizeUpload_btn.setEnabled(False)
        if self.CheckAvatar == False:
            self.avatar = self.iconPath
            shutil.copyfile(self.avatar, self.AppSettingDir + "prxUserMeta\MegaSRX\metaprodata\\" + self.user[self.currentUserCounter] + ".png")
        elif self.CheckAvatar == True:
            self.avatar = self.AppSettingDir + "prxUserMeta\MegaSRX\metaprodata\\" + self.user[self.currentUserCounter] + "Original.png"
            shutil.copyfile(self.avatar, self.AppSettingDir + "prxUserMeta\MegaSRX\metaprodata\\" + self.user[self.currentUserCounter] + ".png")
            
            path = ""
            for i in self.avatar:
                if i == "\\":
                    path += "/"
                else:
                    path += i
            self.ProfileIcon.setStyleSheet("border-image: url(" + path + ");")
        self.windo = QtWidgets.QWidget()
        self.ui = Confirm.Ui_ConfirmWindow()
        self.ui.setupUi(self.windo, self.avatar, self.IP, self.Port, "", "Profileit", "", self.user[self.currentUserCounter])
        self.windo.show()

    def Error(self, Type):
        import Message
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        self.ui.setupUi(self.window, Type)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileIconWin = QtWidgets.QWidget()
    ui = Ui_ProfileIconWin()
    ui.setupUi(ProfileIconWin)
    ProfileIconWin.show()
    sys.exit(app.exec_())
