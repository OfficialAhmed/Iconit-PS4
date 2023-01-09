"""
    The only class from Module that doest inherit from Common
    So we can call methods from Common without polymorphism
"""

from PyQt5 import QtWidgets

import os

class Main():
    def __init__(self) -> None:
        self.appPath = str(os.getcwd())
        self.tempPath = self.appPath + "\Data\prxUserMeta\\"
        
        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIp = ""
        self.userIPath = self.appPath
        self.userDPath = self.appPath
        self.userHB = "False"

    def get_cache(self) -> tuple:
        try:
            with open("Data/Pref/pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2:-1]
                self.userPort = content[1][2:-1]
                self.userIp = content[2][3:-1]
                self.userIPath = content[3][6:-1]
                self.userDPath = content[4][6:-1]
                self.userHB = content[5][3:].strip()

        except:
            pass

        finally:
            return (
                self.userFont, 
                self.userPort, 
                self.userIp, 
                self.userIPath, 
                self.userDPath,
                self.userHB
            )

    def ResetDefaults(self):
        try:
            with open("Data/Pref/pref.ini", "w+") as file:
                file.write("Set to default")
        except:
            pass

    def SaveOptions(self):
        Font = self.Font.currentText()
        IconPath = self.IconPath.text()
        DownloadPath = self.DownloadPath.text()
        ShowHB = str(self.Yes.isChecked())
        Port = self.Port.text()
        IP = self.IP.text()

        if len(Port) == 0:
            Port = self.userPort
        if len(IP) == 0:
            IP = self.userIp
        if len(IconPath) == 0:
            IconPath = self.userIPath
        if len(DownloadPath) == 0:
            DownloadPath = self.userDPath

        with open("Data/Pref/pref.ini", "w+") as file:
            file.write(
                "F:"
                + Font
                + "\nP:"
                + str(Port)
                + "\nIP:"
                + IP
                + "\nIPath:"
                + IconPath
                + "\nDPath:"
                + DownloadPath
                + "\nHB:"
                + ShowHB
            )
        self.OptionsWin.close()

    def GetDownloadPath(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.appPath)
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Default Download Directory...", self.appPath, options=opt
        )
        if path:
            self.DownloadPath.setText(path)

    def GetIconPath(self):
        from PyQt5.QtWidgets import QFileDialog, QDialog

        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.appPath)
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Default Icon Directory...", self.appPath, options=opt
        )
        if path:
            self.IconPath.setText(path)
