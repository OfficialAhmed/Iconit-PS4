from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os

class Main:
    """
        The only class from Module that doest inherit from Common
        So we can call the methods from Common without polymorphism

        * local attributes can be called without inheritence
    """
    userHB = None
    userIp = None
    userFont = None
    userPort = None
    userIPath = None
    userDPath = None

    pref_location = None
    application_location = None
    
    def set_defaults(self, Ip, HB, Font, Port, IPath, DPath, pref, loc) -> None:
        Main.userIp, self.userIp = Ip, Ip
        Main.userHB, self.userHB = HB, HB
        Main.userFont, self.userFont = Font, Font
        Main.userPort, self.userPort = Port, Port
        Main.userIPath, self.userIPath = IPath, IPath
        Main.userDPath, self.userDPath = DPath, DPath
        Main.pref_location, self.pref_location = pref, pref
        Main.application_location, self.application_location = loc, loc

    def get_cache(self, pref_location) -> tuple:
        """ Update local and global attributes from cached file"""
        try:
            with open(f"{pref_location}pref.ini") as file:
                content = file.readlines()
                Main.userFont, self.userFont = content[0][2:-1], content[0][2:-1]
                Main.userPort, self.userPort = content[1][2:-1], content[1][2:-1]
                Main.userIp, self.userIp = content[2][3:-1], content[2][3:-1]
                Main.userIPath, self.userIPath = content[3][6:-1], content[3][6:-1]
                Main.userDPath, self.userDPath = content[4][6:-1], content[4][6:-1]
                Main.userHB, self.userHB = content[5][3:].strip(), content[5][3:].strip()
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
            with open(f"{self.pref_location}pref.ini", "w+") as file:
                file.write(
                    f"F:Arial\nP:21\nIP:\nIPath:{os.getcwd()}\nDPath:{os.getcwd()}\nHB:False"
                )
            self.get_cache(self.pref_location)
        except:
            pass
        self.OptionsWin.close()

    def SaveOptions(self, font, icon_path, download_path, hb, port, ip):
        selected_font = font
        selected_icon_path = icon_path
        selected_download_path = download_path
        selected_hb = hb
        selected_port = port
        selected_ip = ip

        if len(selected_port) == 0:
            selected_port = self.userPort
        if len(selected_ip) == 0:
            selected_ip = self.userIp
        if len(selected_icon_path) == 0:
            selected_icon_path = self.userIPath
        if len(selected_download_path) == 0:
            selected_download_path = self.userDPath

        with open(f"{self.pref_location}pref.ini", "w+") as file:
            file.write(
                f"F:{selected_font}\nP:{selected_port}\nIP:{selected_ip}\nIPath:{selected_icon_path}\nDPath:{selected_download_path}\nHB:{selected_hb}"
            )
        self.OptionsWin.close()
        self.get_cache(self.pref_location)

    def GetDownloadPath(self):
        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.application_location)
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Default Download Directory...", self.application_location, options=opt
        )
        if path:
            self.DownloadPath.setText(path)

    def GetIconPath(self):
        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.application_location)
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Default Icon Directory...", self.application_location, options=opt
        )
        if path:
            self.IconPath.setText(path)
