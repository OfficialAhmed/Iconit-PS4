from PyQt5 import QtCore, QtGui, QtWidgets
import PIL, os, sys
from PIL import Image
from ftplib import FTP

class Ui_ConfirmWindow(object):
    def setupUi(self, ConfirmWindow, changeIconPath, IP, Port, CUSA, ConfirmType, exGames, CurrentUser=None):
        ConfirmWindow.setObjectName("ConfirmWindow")
        ConfirmWindow.resize(378, 229)
        ConfirmWindow.setMinimumSize(QtCore.QSize(500, 500))
        ConfirmWindow.setMaximumSize(QtCore.QSize(500, 500))

        self.exGames = exGames
        self.IP = IP
        self.Port = Port
        self.CurrentUser = CurrentUser
        self.ftp = FTP()
        self.ConfirmType = ConfirmType
        self.working_dir = "user/appmeta"
        self.Current_CUSA = CUSA
        self.local_path = str(os.getcwd())
        self.temp_path = self.local_path + "\Data\prxUserMeta\\"
        self.changeIconPath = changeIconPath
        self.centralwidget = QtWidgets.QWidget(ConfirmWindow)
        self.centralwidget.setObjectName("ConfirmWindow")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setItalic(True)
        ConfirmWindow.setWindowIcon(QtGui.QIcon(self.local_path + "\Data\Pref\ic1.@OfficialAhmed0"))

        self.Yes = QtWidgets.QPushButton(ConfirmWindow)
        self.Yes.setGeometry(QtCore.QRect(155, 120, 100, 31))
        self.Yes.setFont(font)
        self.Yes.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.Yes.setObjectName("Yes")
        self.Yes.clicked.connect(self.Resize_Upload)
        
        self.Ok = QtWidgets.QPushButton(ConfirmWindow)
        self.Ok.setGeometry(QtCore.QRect(215, 120, 100, 31))
        self.Ok.setFont(font)
        self.Ok.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.Ok.setObjectName("Ok")
        self.Ok.clicked.connect(ConfirmWindow.close)

        self.No = QtWidgets.QPushButton(ConfirmWindow)
        self.No.setGeometry(QtCore.QRect(290, 120, 100, 31))
        self.No.setFont(font)
        self.No.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.No.setObjectName("No")
        self.No.clicked.connect(ConfirmWindow.close)

        self.line = QtWidgets.QFrame(ConfirmWindow)
        self.line.setGeometry(QtCore.QRect(10, 160, 480, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.CheckingBar = QtWidgets.QProgressBar(ConfirmWindow)
        self.CheckingBar.setGeometry(QtCore.QRect(220, 250, 170, 40))
        self.CheckingBar.setProperty("value", 0)
        self.CheckingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CheckingBar.setTextVisible(True)
        self.CheckingBar.setOrientation(QtCore.Qt.Horizontal)
        self.CheckingBar.setInvertedAppearance(False)
        self.CheckingBar.setObjectName("CheckingBar")
        self.ResizingBar = QtWidgets.QProgressBar(ConfirmWindow)
        self.ResizingBar.setGeometry(QtCore.QRect(220, 350, 170, 40))
        self.ResizingBar.setProperty("value", 0)
        self.ResizingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.ResizingBar.setTextVisible(True)
        self.ResizingBar.setObjectName("ResizingBar")
        self.UploadingBar = QtWidgets.QProgressBar(ConfirmWindow)
        self.UploadingBar.setGeometry(QtCore.QRect(220, 430, 170, 40))
        self.UploadingBar.setProperty("value", 0)
        self.UploadingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.UploadingBar.setTextVisible(True)
        self.UploadingBar.setObjectName("UploadingBar")
        self.graphicsView = QtWidgets.QGraphicsView(ConfirmWindow)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -10, 700, 700))
        self.graphicsView.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.graphicsView.setObjectName("graphicsView")

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)

        self.Checking = QtWidgets.QLabel(ConfirmWindow)
        self.Checking.setGeometry(QtCore.QRect(60, 255, 111, 31))
        self.Checking.setFont(font)
        self.Checking.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Checking.setAlignment(QtCore.Qt.AlignCenter)
        self.Checking.setObjectName("Checking")

        self.Resizing_label = QtWidgets.QLabel(ConfirmWindow)
        self.Resizing_label.setGeometry(QtCore.QRect(60, 355, 111, 31))
        self.Resizing_label.setFont(font)
        self.Resizing_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Resizing_label.setObjectName("Resizing_label")

        self.Uploading_label = QtWidgets.QLabel(ConfirmWindow)
        self.Uploading_label.setGeometry(QtCore.QRect(60, 440, 111, 31))
        self.Uploading_label.setFont(font)
        self.Uploading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Uploading_label.setObjectName("Uploading_label")

        self.Statement = QtWidgets.QLabel(ConfirmWindow)
        self.Statement.setGeometry(QtCore.QRect(20, 50, 470, 40))
        self.Statement.setFont(font)
        self.Statement.setStyleSheet("color: rgb(255, 255, 255);")
        self.Statement.setFrameShape(QtWidgets.QFrame.Box)
        self.Statement.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Statement.setAlignment(QtCore.Qt.AlignCenter)
        self.Statement.setObjectName("Statement")

        self.graphicsView.raise_()
        self.Yes.raise_()
        self.No.raise_()
        self.line.raise_()
        self.CheckingBar.raise_()
        self.ResizingBar.raise_()
        self.UploadingBar.raise_()
        self.Checking.raise_()
        self.Resizing_label.raise_()
        self.Uploading_label.raise_()
        self.Statement.raise_()
        self.retranslateUi(ConfirmWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfirmWindow)

    def retranslateUi(self, ConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfirmWindow.setWindowTitle(_translate("ConfirmWindow", "Confirm"))
        self.Yes.setText(_translate("ConfirmWindow", "Yes"))
        self.Ok.setText(_translate("ConfirmWindow", "Ok"))
        self.No.setText(_translate("ConfirmWindow", "No"))
        self.Checking.setText(_translate("ConfirmWindow", "Checking"))
        self.Resizing_label.setText(_translate("ConfirmWindow", "Resizing"))
        self.Uploading_label.setText(_translate("ConfirmWindow", "Uploading"))
        self.Statement.setText(_translate("ConfirmWindow", "Are sure you want to change the icon?"))

    def Resize_Upload(self):
        try:
            self.Yes.setEnabled(False)
            self.No.setEnabled(False)
            self.ftp.set_debuglevel(2)
            self.ftp.connect(self.IP, int(self.Port))
            self.ftp.login("", "")
            self.CheckingBar.setProperty("value", 10)
            if self.ConfirmType == "Iconit":
                files = []
                if self.Current_CUSA in self.exGames:
                    self.ftp.cwd(self.working_dir + "/external/" + self.Current_CUSA)
                else:
                    self.ftp.cwd(self.working_dir + "/" + self.Current_CUSA)

                self.CheckingBar.setProperty("value", 40)
                img_dir = self.temp_path + "MegaSRX\\"
                #Check how many icons in Game directory
                with open(self.temp_path + "files_in_dir.dat", "w+", encoding="utf8") as files_in_dir:
                    self.ftp.retrlines("LIST", files_in_dir.write)
                self.CheckingBar.setProperty("value", 85)

                Icon_dir = self.changeIconPath
                #Resize picture but don't save it yet
                picture = Image.open(Icon_dir) 
                resize = picture.resize((512, 512), PIL.Image.ANTIALIAS)
                self.CheckingBar.setProperty("value", 100)
                self.ResizingBar.setProperty("value", 1)
                with open(self.temp_path + "files_in_dir.dat", "r", encoding="utf8") as files_in_dir_4_pics:
                    content_in_file = files_in_dir_4_pics.read()
                    self.ResizingBar.setProperty("value", 20)

                    if "icon0.png" in content_in_file:
                        resize.save(img_dir + "icon0.png")
                        files.append("icon0.png")
                    if "icon0.dds" in content_in_file:
                        resize.save(img_dir + "icon00.png")
                        try:
                            os.rename(img_dir + "icon00.png", img_dir + "icon0.dds")
                        except FileExistsError:
                            os.remove(img_dir + "icon0.dds")
                            os.rename(img_dir + "icon00.png", img_dir + "icon0.dds")
                        files.append("icon0.dds")
                    self.ResizingBar.setProperty("value", 40)
                    img_count = 22
                    if "icon0_21.png" in content_in_file :
                        img_count = 42

                    #Limit of icons 42
                    for through_20 in range(1, img_count): 
                        if 40+through_20 <= 98:
                            self.ResizingBar.setProperty("value", 40+through_20)

                        if through_20 <= 9:
                            search_png = ("icon0_0" + str(through_20) + ".png")
                            search_dds = ("icon0_0" + str(through_20) + ".dds")
                            copy_for_dds = ("icon0_0" + str(through_20) + ".TIFF")
                            
                            if search_png in content_in_file:
                                resize.save(img_dir + search_png)               
                                files.append(search_png)
                                
                            if search_dds in content_in_file:
                                resize.save(img_dir + copy_for_dds)   
                                os.rename(img_dir + copy_for_dds, img_dir + search_dds)
                                files.append(search_dds)
                        else:
                            search_png = ("icon0_" + str(through_20) + ".png")
                            search_dds = ("icon0_" + str(through_20) + ".dds")
                            copy_for_dds = ("icon0_" + str(through_20) + ".TIFF")

                            if search_png in content_in_file:
                                try:
                                    resize.save(img_dir + search_png) 
                                    files.append(search_png)
                                except Exception as e:
                                    self.logIt(str(e), "Warning")

                            if search_dds in content_in_file:
                                try:
                                    os.rename(img_dir + copy_for_dds, img_dir + search_dds)
                                    files.append(search_dds)
                                except Exception as e:
                                    self.logIt(str(e), "Error")
                self.ResizingBar.setProperty("value", 98)
                with open(self.temp_path + "FoundImg.dat", "w+") as pictures:
                    for pic in files:
                        pictures.write(pic + ",")

                self.ResizingBar.setProperty("value", 100)
                self.UploadingBar.setProperty("value", 1)
                try:
                    import shutil
                    with open(self.temp_path + "FoundImg.dat", "r", encoding="utf8") as pictures:
                        read_pictures = pictures.read()[0:-1]
                        pic = read_pictures.split(",")
                        progress = int(100/len(pic))
                        progressed = 0
                        for i in pic:
                            with open(img_dir + str(i), "rb") as save_file:
                                self.ftp.storbinary("STOR " + str(i), save_file, 1024)
                            if i == "icon0.png" or i == "icon0.PNG":
                                shutil.move(img_dir + str(i), self.temp_path + "MegaSRX\metadata\\" + self.Current_CUSA + ".png")
                            progressed += progress
                            self.UploadingBar.setProperty("value", progressed)
                except Exception as e:
                    self.logIt(str(e), "Error")
                self.UploadingBar.setProperty("value", 100)

                self.Statement.setStyleSheet("font: 10pt; color: rgb(5, 255, 20);")
                self.Statement.setText("Done. Give it some time & the icon will change.")
                self.Ok.raise_()
                self.No.hide()
                self.Yes.hide()

            elif self.ConfirmType == "Profileit":
                sysProfileRoot = "system_data/priv/cache/profile/"
                temp_path = str(os.getcwd()) + "\Data\prxUserMeta\\"
                try:
                    #Resize Icon and make copies
                    required_dds = ("avatar64", "avatar128", "avatar260", "avatar440")
                    ResizeImg = Image.open(self.changeIconPath)
                    avatar = ResizeImg.resize((440, 440), PIL.Image.ANTIALIAS)
                    avatar.save(temp_path + "avatar.png")
                    self.CheckingBar.setProperty("value", 20)
                    progress = 20
                    progressed = 60
                    for dds in required_dds:
                        if "64" in dds:
                            avatar = ResizeImg.resize((64, 64), PIL.Image.ANTIALIAS)
                            avatar.save(temp_path + "avatar64.png")
                            self.CheckingBar.setProperty("value", 40)
                        else:
                            s = int(dds[-3:])
                            avatar = ResizeImg.resize((s, s), PIL.Image.ANTIALIAS)
                            avatar.save(temp_path + "avatar" + str(s) + ".png")
                            self.CheckingBar.setProperty("value", progressed)
                            progressed +=  20
                    self.CheckingBar.setProperty("value", 100)
                except Exception as e:
                    self.logIt(str(e), "error")

                #Convert PNG To DDS
                if os.path.isfile("C:\Program Files\ImageMagick-6.9.10-Q16\convert.exe"):
                    progress = 25
                    progressed = 0
                    
                    try:
                        from wand.image import Image as OpenThis 
                        import time
                        for dds in required_dds:
                            with OpenThis(filename = temp_path + dds + ".png") as Original:
                                Original.save(filename = temp_path + dds + ".dds")
                            for i in range(progressed, progress):
                                self.ResizingBar.setProperty("value", i)
                                time.sleep(0.01)
                            progressed += progress
                            os.remove(temp_path + dds + ".png")
                        self.ResizingBar.setProperty("value", 100)
                        self.Statement.setStyleSheet("font: 10pt; color: rgb(5, 255, 20);")
                        self.Statement.setText("Done. Give it some time & the avatar will change.")
                        self.Ok.setEnabled(False)
                        self.Ok.raise_()
                        self.No.hide()
                        self.Yes.hide()

                    except Exception as e:
                        self.logIt(str(e), "Error")(str(e))
                else:
                    import Message
                    self.window = QtWidgets.QDialog()
                    self.ui = Message.Ui_Message()
                    self.ui.setupUi(self.window, "Magick image not found")
                    self.window.show()

                #Upload
                self.ftp.cwd(sysProfileRoot + "/" + self.CurrentUser)
                progress = 20
                progressed = 20
                with open(temp_path + "avatar.png", "rb") as save_file:
                    self.ftp.storbinary("STOR " + "avatar.png", save_file, 1024)
                    self.UploadingBar.setProperty("value", progressed)
                for avatar in required_dds:
                    with open(temp_path + avatar + ".dds", "rb") as save_file:
                        self.ftp.storbinary("STOR " + avatar + ".dds", save_file, 1024)
                    for i in range(progressed,progressed + progress+1):
                        self.UploadingBar.setProperty("value", i)
                        time.sleep(0.01)
                    progressed += progress
                self.Ok.setEnabled(True)

        except FileNotFoundError:
            pass

        except FileExistsError:
            icons = os.listdir(img_dir)
            for i in icons:
                if i != "Do Not put any file in here" or i != "metadata":
                    try:
                        os.remove(img_dir + i)
                    except Exception as e:
                        self.logIt(str(e), "Error")(str(e))
            self.Resize_Upload()

        except Exception as e:
            self.logIt(str(e), "Error")(str(e))

    def logIt(self, description, Type):
        import datetime
        try:
            error_file = open("Logs.txt", "a")
        except:
            error_file = open("Logs.txt", "w")
        if Type == "Warning":
            error_file.write(str(datetime.datetime.now()) + " | " + "_DEV Warning: " + str(description) + "\n")
        else:
            error_file.write(str(datetime.datetime.now()) + " | " + "_DEV ERROR: " + str(description) + "\n")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfirmWindow = QtWidgets.QDialog()
    ui = Ui_ConfirmWindow()
    ui.setupUi(ConfirmWindow)
    ConfirmWindow.show()
    sys.exit(app.exec_())
