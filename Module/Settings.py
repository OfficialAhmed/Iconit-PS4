from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, json

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
    userLanguage = None

    temp_path = None
    application_location = None


    def __init__(self) -> None:
        app_path = os.getcwd()
        self.app_root_path = f"{app_path}\\"
        self.data_path = f"{self.app_root_path}Data\\"
        self.language_path = f"{self.data_path}Language\\"
        self.temp_path = f"{self.data_path}Cache\\"

        self.default_settings = {"font":"Arial", "port":"21", "ip":"", "icons_path":app_path, "download_path":app_path, "homebrew":"False", "language":"English"}


    def get_translation(self, lang:str, fetch:str) -> dict:
        """ Get info from tranlated json files. (lang):represent the json name to fetch data from """
        file = open(f"{self.language_path}{lang}.json", encoding="utf-8")
        read = json.load(file)
        return read.get(fetch)


    def set_defaults(self, Ip, HB, Font, Port, IPath, DPath, lang, cache_path, loc) -> None:
        """ Make attributes public for other classes """
        Main.userIp, self.userIp = Ip, Ip
        Main.userHB, self.userHB = HB, HB
        Main.userFont, self.userFont = Font, Font
        Main.userPort, self.userPort = Port, Port
        Main.userIPath, self.userIPath = IPath, IPath
        Main.userDPath, self.userDPath = DPath, DPath
        Main.userLanguage, self.userLanguage = lang, lang

        Main.temp_path, self.temp_path = cache_path, cache_path
        Main.application_location, self.application_location = loc, loc


    def reset_to_defaults(self):
        """ overwrite external file (Settings.json) by default settings """
        try:
            with open(f"{self.temp_path}Settings.json", "w+") as file:
                json.dump(self.default_settings, file)

            self.update_cache(self.temp_path)
            self.OptionsWin.close()
        except: pass


    def update_cache(self, cache_path) -> dict:
        """ Update the class's cache from external file (Settings.json) & return attributes"""

        try:
            with open(f"{cache_path}Settings.json", encoding="utf-8") as file:
                content: dict = json.load(file)
                ip = content.get("ip")
                font = content.get("font")
                port = content.get("port")
                homebrew = content.get("homebrew")
                language = content.get("language")
                icons_path = content.get("icons_path")
                donwload_path = content.get("donwload_path")

                Main.userIp, self.userIp = ip, ip
                Main.userFont, self.userFont = font, font
                Main.userPort, self.userPort = port, port
                Main.userHB, self.userHB = homebrew, homebrew
                Main.userLanguage, self.userLanguage = language, language
                Main.userIPath, self.userIPath = icons_path, icons_path
                Main.userDPath, self.userDPath = donwload_path, donwload_path
        except: pass
        finally: 
            data = {"font":self.userFont, "port":self.userPort, "ip":self.userIp, "icons_path":self.userIPath, "download_path":self.userDPath, "homebrew":self.userHB, "language":self.userLanguage}
            return data


    def save_cache(self, font:str = "", icons_path:str = "", download_path:str = "", hb:str = "", port:str = "", ip:str = "", lang:str = "") -> None:
        """ Cache information to external file Settings.json """

        if ip == "": ip = self.userIp
        if hb == "": hb = self.userHB
        if port == "": port = self.userPort
        if font == "": font = self.userFont
        if icons_path == "": icons_path = self.userIPath
        if download_path == "": download_path = self.userDPath
        if lang == "": lang = self.userLanguage
    
        data = {"font":font, "port":port, "ip":ip, "icons_path":icons_path, "download_path": download_path, "homebrew":hb, "language":lang}
        with open(f"{self.temp_path}Settings.json", "w+") as file:
            json.dump(data, file)
        
        self.update_cache(self.temp_path)

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