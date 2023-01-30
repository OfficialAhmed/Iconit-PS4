from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os

class Main:
    """
        The only class from Module that doest inherit from (Common)
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
        """ Make attributes public for other classes """
        Main.userIp, self.userIp = Ip, Ip
        Main.userHB, self.userHB = HB, HB
        Main.userFont, self.userFont = Font, Font
        Main.userPort, self.userPort = Port, Port
        Main.userIPath, self.userIPath = IPath, IPath
        Main.userDPath, self.userDPath = DPath, DPath
        Main.pref_location, self.pref_location = pref, pref
        Main.application_location, self.application_location = loc, loc

    def reset_to_defaults(self):
        """ overwrite external file (pref.ini) by default settings """
        try:
            with open(f"{self.pref_location}pref.ini", "w+") as file:
                default_data = f"F:Arial\nP:21\nIP:\nIPath:{os.getcwd()}\nDPath:{os.getcwd()}\nHB:False"
                file.write(default_data)
            self.update_cache(self.pref_location)
            self.OptionsWin.close()
        except: pass

    def update_cache(self, pref_location) -> tuple:
        """ Update the class's cache from external file (pref.ini) & return attributes"""
        try:
            with open(f"{pref_location}pref.ini") as file:
                content = file.readlines()
                Main.userFont, self.userFont = content[0][2:-1], content[0][2:-1]
                Main.userPort, self.userPort = content[1][2:-1], content[1][2:-1]
                Main.userIp, self.userIp = content[2][3:-1], content[2][3:-1]
                Main.userIPath, self.userIPath = content[3][6:-1], content[3][6:-1]
                Main.userDPath, self.userDPath = content[4][6:-1], content[4][6:-1]
                Main.userHB, self.userHB = content[5][3:].strip(), content[5][3:].strip()
        except: pass
        finally: 
            return (
                self.userFont, 
                self.userPort, 
                self.userIp, 
                self.userIPath, 
                self.userDPath,
                self.userHB
            )

    def save_cache(self, font:str = "", icon_path:str = "", download_path:str = "", hb:str = "", port:str = "", ip:str = "") -> None:
        """ Cache information to external file pref.ini """

        if ip == "": ip = self.userIp
        if hb == "": hb = self.userHB
        if port == "": port = self.userPort
        if font == "": font = self.userFont
        if icon_path == "": icon_path = self.userIPath
        if download_path == "": download_path = self.userDPath

        with open(f"{self.pref_location}pref.ini", "w+") as file:
            default_data = f"F:{font}\nP:{port}\nIP:{ip}\nIPath:{icon_path}\nDPath:{download_path}\nHB:{hb}"
            file.write(default_data)
        self.update_cache(self.pref_location)

        # Sometimes saving without the window
        try: self.OptionsWin.close() 
        except: pass

    def get_path(self, type):
        """ Render browsing window to pick default paths """
        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.application_location)
        if type == "download":
            path = QtWidgets.QFileDialog.getExistingDirectory(
                None, "Default download folder...", self.application_location, options=opt
            )
            if path: self.DownloadPath.setText(path)
        else:
            path = QtWidgets.QFileDialog.getExistingDirectory(
                None, "Default icons folder...", self.application_location, options=opt
            )
            if path: self.IconPath.setText(path)
