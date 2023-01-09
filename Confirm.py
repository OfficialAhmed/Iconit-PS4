from PyQt5 import QtCore, QtGui, QtWidgets
import PIL
import os
import sys
from PIL import Image
from ftplib import FTP
import Interface.Alerts as Alerts
import shutil


class Ui_ConfirmWindow(object):
    def setupUi(
        self,
        ConfirmWindow,
        changeIconPath,
        IP,
        Port,
        CUSA,
        ConfirmType,
        exGames,
        CurrentUser=None,
        changeBgPath=None,
        modeSelected="",
        sysIconsAlgo=False,
    ):
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
        self.changeBgPath = changeBgPath
        self.modeSelected = modeSelected
        self.sysIconsAlgo = sysIconsAlgo

        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui_Message()

        self.centralwidget = QtWidgets.QWidget(ConfirmWindow)
        self.centralwidget.setObjectName("ConfirmWindow")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setItalic(True)
        ConfirmWindow.setWindowIcon(
            QtGui.QIcon(self.local_path + "\Data\Pref\ic1.@OfficialAhmed0")
        )

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
        self.Checking.setText(_translate("ConfirmWindow", "Validation"))
        self.Resizing_label.setText(_translate("ConfirmWindow", "Convertion"))
        self.Uploading_label.setText(_translate("ConfirmWindow", "Sending"))

        styleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style="font-size:10pt; '
        styleTagEnd = "</span></p>\n"
        warning_message = f'{styleTagStart} color:#e83c3c">ATTENTION! This will overwrite the backup icon stored in (Your backup). {styleTagEnd}\n"Are sure you want to change the icon?"'
        
        self.Statement.setText(
            _translate("ConfirmWindow", warning_message)
        )

    def png2dds(self, input_dir, output_dir):
        # implementation added v4.51
        # convert legit png to dds using imageMagic lib (wand)
        if self.image != None:
            with self.image.Image(filename=input_dir) as img:
                img.compression = "dxt1"
                img.save(filename=output_dir)

    def backup(self, sys=False):
        ###################################################
        ###             backup impl. v4.72
        ###       Move icon to Your Backup folder
        ###################################################

        backup = []
        try:
            backup = os.listdir("Your Backup")
        except:
            os.mkdir("Your Backup")

        if self.Current_CUSA + ".png" in backup:
            try:
                os.remove("Your Backup\\" + self.Current_CUSA + ".png")
            except Exception as e:
                self.logIt(str(e), "Error")

        try:
            shutil.copyfile(
                "Data\prxUserMeta\MegaSRX\metadata\\"
                + self.modeSelected
                + "\\"
                + self.Current_CUSA
                + ".png",
                "Your Backup\\" + self.Current_CUSA + ".png",
            )

        except Exception as e:
            self.logIt(str(e), "Error")

    def Resize_Upload(self):
        try:
            self.image = None
            try:
                from wand import image
                import time

                self.image = image

            except Exception as e:
                self.logIt(
                    str(e)
                    + " | DEV module wand cannot be found, something related to imageMagic",
                    "Warning",
                )

            self.Yes.setEnabled(False)
            self.No.setEnabled(False)
            try:
                self.ftp.connect(self.IP, int(self.Port))
                self.ftp.login("", "")
            except:
                self.logIt(e, "Error")
                self.ui.setupUi(self.window, str(e))
                self.window.show()
            self.CheckingBar.setProperty("value", 10)
            img_dir = self.temp_path + "MegaSRX\\"

            if self.ConfirmType == "Iconit":
                if self.sysIconsAlgo:
                    ###################################################
                    ###
                    ### Critical method needs to be accurate 100%
                    ### messing up with PS4 sys files related to sys icons
                    ### Triple check everything here
                    ###
                    ###################################################

                    self.ftp.cwd("/")
                    self.ftp.cwd("system_ex/app/" + self.Current_CUSA + "/sce_sys")
                    sce_sys_dir = []
                    self.ftp.retrlines("LIST ", sce_sys_dir.append)
                    files_inside = [x.split(" ")[-1] for x in sce_sys_dir]
                    self.CheckingBar.setProperty("value", 5)

                    iconFound = "icon0.png"
                    found_4k = False
                    IconName = [iconFound]

                    if "icon0_4k.png" in files_inside:
                        iconFound = "icon0_4k.png"
                        IconName.append(iconFound)
                        found_4k = True

                    self.CheckingBar.setProperty("value", 45)
                    with open(self.temp_path + "MegaSRX\\icon0.png", "wb") as file:
                        self.ftp.retrbinary("RETR " + iconFound, file.write)

                    self.backup(sys=True)
                    self.CheckingBar.setProperty("value", 100)

                    if self.changeIconPath != "" and self.changeIconPath != None:
                        self.ResizingBar.setProperty("value", 10)
                        Icon = Image.open(self.changeIconPath)

                        if found_4k:
                            minSize = 660
                            resizeIcon = Icon.resize(
                                (minSize, minSize), PIL.Image.ANTIALIAS
                            )
                            resizeIcon.save(img_dir + "icon0_4k.png")
                            self.ResizingBar.setProperty("value", 40)

                        self.ResizingBar.setProperty("value", 75)

                        minSize = 512
                        resizeIcon = Icon.resize(
                            (minSize, minSize), PIL.Image.ANTIALIAS
                        )
                        resizeIcon.save(img_dir + "icon0.png")
                        self.ResizingBar.setProperty("value", 100)
                else:
                    IconName = []  # Icon0, Icon0_X (dds and png extension)
                    BackgroundName = []  # Pic0, Pic1 (dds and png extension)
                    self.ftp.cwd("/")
                    try:
                        if self.Current_CUSA in self.exGames:
                            self.ftp.cwd(
                                self.working_dir + "/external/" + self.Current_CUSA
                            )
                        else:
                            self.ftp.cwd(self.working_dir + "/" + self.Current_CUSA)
                    except:
                        import Interface.Alerts as Alerts

                        self.window = QtWidgets.QDialog()
                        self.ui = Alerts.Ui_Message()
                        self.ui.setupUi(
                            self.window,
                            "Cannot find this icon in your PS4. This might be from an older caching process please delete cache and recache again, other than that you may continue but this icon wont be changed.",
                        )
                        self.window.show()
                        self.CheckingBar.setProperty("value", 50)

                    # Check how many icons in Game directory
                    with open(
                        self.temp_path + "files_in_dir.dat", "w+", encoding="utf8"
                    ) as files_in_dir:
                        self.ftp.retrlines("LIST", files_in_dir.write)
                    self.CheckingBar.setProperty("value", 95)

                    # update v4.65 compatible compression type for PS4 .DDS = DXT1
                    with open(
                        self.temp_path + "files_in_dir.dat", "r", encoding="utf8"
                    ) as files_in_dir_4_pics:
                        # v4.65 new implementation for background image feature
                        content_in_file = files_in_dir_4_pics.read()
                        self.CheckingBar.setProperty("value", 100)
                        self.ResizingBar.setProperty("value", 1)
                        if self.changeIconPath != "" and self.changeIconPath != None:
                            self.backup()

                            # Icon has been changed we need to resize and prepare for upload
                            Icon = Image.open(self.changeIconPath)
                            resizeIcon = Icon.resize((512, 512), PIL.Image.ANTIALIAS)

                            if "icon0.png" in content_in_file:
                                resizeIcon.save(img_dir + "icon0.png")
                                IconName.append("icon0.png")

                            if "icon0.dds" in content_in_file:
                                self.png2dds(
                                    img_dir + "icon0.png", img_dir + "icon0.dds"
                                )
                                IconName.append("icon0.dds")
                            self.ResizingBar.setProperty("value", 10)

                            img_count = 22
                            if "icon0_21.png" in content_in_file:
                                img_count = 42

                            # Limit of icons 42
                            for through_20 in range(1, img_count):
                                if 10 + through_20 <= 44:
                                    self.ResizingBar.setProperty(
                                        "value", 20 + through_20
                                    )
                                if through_20 <= 9:
                                    search_png = "icon0_0" + str(through_20) + ".png"
                                    search_dds = "icon0_0" + str(through_20) + ".dds"

                                    if search_png in content_in_file:
                                        resizeIcon.save(img_dir + search_png)
                                        IconName.append(search_png)

                                    if search_dds in content_in_file:
                                        # if png exists override it no issue, otherwise
                                        # create a png, resize it and convert it to dds
                                        resizeIcon.save(img_dir + search_png)
                                        self.png2dds(
                                            img_dir + search_png, img_dir + search_dds
                                        )
                                        IconName.append(search_dds)
                                else:
                                    search_png = "icon0_" + str(through_20) + ".png"
                                    search_dds = "icon0_" + str(through_20) + ".dds"

                                    if search_png in content_in_file:
                                        try:
                                            resizeIcon.save(img_dir + search_png)
                                            IconName.append(search_png)
                                        except Exception as e:
                                            self.logIt(str(e), "Warning")

                                    if search_dds in content_in_file:
                                        try:
                                            self.png2dds(
                                                img_dir + search_png,
                                                img_dir + search_dds,
                                            )
                                            IconName.append(search_dds)
                                        except Exception as e:
                                            self.logIt(str(e), "Error")
                        self.ResizingBar.setProperty("value", 45)

                        if self.changeBgPath != "" and self.changeBgPath != None:
                            
                            ###################################################################################
                            ###   Background image has been changed we need to resize and prepare for upload
                            ###################################################################################

                            Background = Image.open(self.changeBgPath)
                            resizeBackground = Background.resize(
                                (1920, 1080), PIL.Image.ANTIALIAS
                            )
                            self.ResizingBar.setProperty("value", 50)

                            # v4.65 background pic0, pic1 implementaion
                            if "pic0.png" in content_in_file:
                                resizeBackground.save(img_dir + "pic0.png")
                                BackgroundName.append("pic0.png")
                            if "pic1.png" in content_in_file:
                                resizeBackground.save(img_dir + "pic1.png")
                                BackgroundName.append("pic1.png")
                            self.ResizingBar.setProperty("value", 75)

                            if "pic0.dds" in content_in_file:
                                self.png2dds(img_dir + "pic0.png", img_dir + "pic0.dds")
                                BackgroundName.append("pic0.dds")
                            if "pic1.dds" in content_in_file:
                                self.png2dds(img_dir + "pic1.png", img_dir + "pic1.dds")
                                BackgroundName.append("pic1.dds")

                            for bg in BackgroundName:
                                with open(img_dir + str(bg), "rb") as save_file:
                                    self.ftp.storbinary(
                                        "STOR " + str(bg), save_file, 1024
                                    )

                self.ResizingBar.setProperty("value", 100)
                self.UploadingBar.setProperty("value", 1)

                ######################################################################################
                ###    v4.65 added background (pic0, pic1) implementation and minimized the code
                ######################################################################################
                try:
                    for ic in IconName:
                        # upload the icons to PS4 system
                        with open(img_dir + str(ic), "rb") as save_file:
                            self.ftp.storbinary("STOR " + str(ic), save_file, 1024)

                        ########################################################################
                        ###         Store icons temp for in-app preview
                        ########################################################################
                        
                        if ic == "icon0.png" or ic == "icon0.PNG":
                            shutil.move(
                                img_dir + str(ic),
                                self.temp_path
                                + "MegaSRX\metadata\\"
                                + self.modeSelected
                                + "\\"
                                + self.Current_CUSA
                                + ".png",
                            )

                    self.UploadingBar.setProperty("value", 100)
                    self.Statement.setStyleSheet("font: 10pt; color: rgb(5, 255, 20);")
                    self.Statement.setText(
                        "You're all set. made with LOVE by @OfficialAhmed0"
                    )
                except Exception as e:
                    self.logIt(str(e), "Error")

                    self.UploadingBar.setProperty("value", 5)
                    self.Statement.setStyleSheet("font: 10pt; color: rgb(250, 1, 1);")
                    self.Statement.setText("Sorry! PS4 has denied the signal, enable Full R/W")

                self.No.hide()
                self.Yes.hide()
                self.Ok.raise_()
                styleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style="font-size:10pt; '
                styleTagEnd = "</span></p>\n"
                self.logging += (
                    styleTagStart
                    + 'color:#ffaa00">[Attention]: '
                    + "Image might take sometime to change in both PS4 and Iconit, but everything went good you dont have to reupload"
                    + styleTagEnd
                )
                self.UpdateLogs()

            elif self.ConfirmType == "Profileit":
                sysProfileRoot = "system_data/priv/cache/profile/"
                try:
                    ###############################################################
                    #######          Resize Icon and make copies
                    ###############################################################
                    required_dds = ("avatar64", "avatar128", "avatar260", "avatar440")
                    ResizeImg = Image.open(self.changeIconPath)
                    avatar = ResizeImg.resize((440, 440), PIL.Image.ANTIALIAS)
                    avatar.save(self.temp_path + "avatar.png")
                    self.CheckingBar.setProperty("value", 20)
                    progress = 20
                    progressed = 60
                    for dds in required_dds:
                        if "64" in dds:
                            avatar = ResizeImg.resize((64, 64), PIL.Image.ANTIALIAS)
                            avatar.save(self.temp_path + "avatar64.png")
                            self.CheckingBar.setProperty("value", 40)
                        else:
                            s = int(dds[-3:])
                            avatar = ResizeImg.resize((s, s), PIL.Image.ANTIALIAS)
                            avatar.save(self.temp_path + "avatar" + str(s) + ".png")
                            self.CheckingBar.setProperty("value", progressed)
                            progressed += 20
                    self.CheckingBar.setProperty("value", 100)
                except Exception as e:
                    self.logIt(str(e), "error")
                
                ################################################################
                ###                     Convert PNG To DDS
                ################################################################

                if os.path.isfile(
                    "C:\Program Files\ImageMagick-6.9.10-Q16\convert.exe"
                ) or os.path.isfile(
                    "C:\Program Files (x86)\ImageMagick-7.1.0-Q16\convert.exe"
                ):
                    progress = 25
                    progressed = 0

                    try:
                        for dds in required_dds:
                            # update v4.21 compatible compression type for PS4 .DDS = DXT1
                            self.png2dds(
                                self.temp_path + dds + ".png",
                                self.temp_path + dds + ".dds",
                            )

                            for i in range(progressed, progress):
                                self.ResizingBar.setProperty("value", i)
                                time.sleep(0.01)
                            progressed += progress
                            os.remove(self.temp_path + dds + ".png")
                        self.ResizingBar.setProperty("value", 100)
                        self.Statement.setStyleSheet(
                            "font: 10pt; color: rgb(5, 255, 20);"
                        )
                        self.Statement.setText(
                            "Done. Give it some time & the avatar will change."
                        )
                        self.Ok.setEnabled(False)
                        self.Ok.raise_()
                        self.No.hide()
                        self.Yes.hide()

                    except Exception as e:
                        self.logIt(str(e), "Error")
                else:
                    self.ui.setupUi(self.window, "Magick image not found")
                    self.window.show()

                ################################################################
                ###                     Upload icons
                ################################################################
                self.ftp.cwd(sysProfileRoot + "/" + self.CurrentUser)
                progress = 20
                progressed = 20
                with open(self.temp_path + "avatar.png", "rb") as save_file:
                    self.ftp.storbinary("STOR " + "avatar.png", save_file, 1024)
                    self.UploadingBar.setProperty("value", progressed)
                for avatar in required_dds:
                    with open(self.temp_path + avatar + ".dds", "rb") as save_file:
                        self.ftp.storbinary("STOR " + avatar + ".dds", save_file, 1024)
                    for i in range(progressed, progressed + progress + 1):
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
                        self.logIt(str(e), "Error")
            self.Resize_Upload()

        except Exception as e:
            self.logIt(str(e), "Error")

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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ConfirmWindow = QtWidgets.QDialog()
    ui = Ui_ConfirmWindow()
    ui.setupUi(ConfirmWindow)
    ConfirmWindow.show()
    sys.exit(app.exec_())
