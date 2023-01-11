"""

    Methods for Changing Avatars
    the class inherits 'Environment'

"""

from environment import Common

from PyQt5 import QtWidgets
import json, os

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

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
        import Interface.Upload as Upload
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
            self.ui = Upload.Ui()
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
        import Interface.Alerts as Alerts

        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui_Message()
        self.ui.setupUi(self.window, Type)
        self.window.show()