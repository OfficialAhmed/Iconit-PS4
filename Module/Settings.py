from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import json

class Main:
    """
        The only class from Module that doest inherit from (Common)
        So we can call the methods from Common without polymorphism

        * local attributes can be called without inheritence
    """

    paths: dict = {}
    default_settings: dict = {}
    DEFAULT_SETTINGS: dict = {}

    def __init__(self) -> None:
        """ init the self parameter only """
        self.init()
        

    def init(self):
        """ custom init callable manually """
        self.path = Main.paths
        self.default_settings = Main.default_settings
        
        self.data_path = f"{self.path.get('app_root_path')}Data\\"
        self.temp_path = self.path.get('temp_path')
        self.language_path = f"{self.data_path}Language\\"


    def set_paths(self, app_path, temp_path):
        """ fetch paths from environment class. [Called once by environment on init only] """
        Main.paths["app_root_path"] = app_path
        Main.paths["temp_path"] = temp_path


    def get_translation(self, lang:str, fetch:str) -> dict:
        """ Get info from tranlated json files. (lang):represent the json name to fetch data from """
        file = open(f"{self.language_path}{lang}.json", encoding="utf-8")
        read = json.load(file)
        return read.get(fetch)


    def set_defaults(self, data:dict) -> None:
        """ Make attributes public for child objects """
        Main.default_settings = data
        Main.DEFAULT_SETTINGS = data


    def reset_to_defaults(self):
        """ overwrite external file (Settings.json) by default settings """
        try:
            with open(f"{self.temp_path}Settings.json", "w+") as file:
                json.dump(Main.DEFAULT_SETTINGS, file)

            self.update_local_cache(self.temp_path)
            self.OptionsWin.close()
        except: pass


    def update_local_cache(self, cache_path) -> dict:
        """ Update the class's cache from external file (Settings.json) & return attributes"""

        try:
            with open(f"{cache_path}Settings.json", encoding="utf-8") as file:
                Main.default_settings = json.load(file)
                self.default_settings = Main.default_settings
        except: pass
        finally: 
            data = {
                "ip":self.default_settings.get("ip"), 
                "font":self.default_settings.get("font"), 
                "port":self.default_settings.get("port"), 
                "homebrew":self.default_settings.get("homebrew"), 
                "language":self.default_settings.get("language"),
                "icons_path":self.default_settings.get("icons_path"), 
                "download_path":self.default_settings.get("download_path")            
            }
            return data


    def save_cache(self, font:str = "", icons_path:str = "", download_path:str = "", hb:str = "", port:str = "", ip:str = "", lang:str = "") -> None:
        """ Cache information to external file Settings.json """

        # replace empty parameters with the local cache
        if not ip: ip = self.default_settings.get("ip")
        if not hb: hb = self.default_settings.get("homebrew")
        if not port: port = self.default_settings.get("port")
        if not font: font = self.default_settings.get("font")
        if not icons_path: icons_path = self.default_settings.get("icons_path")
        if not download_path: download_path = self.default_settings.get("download_path")
        if not lang: lang = self.default_settings.get("language")
    
        data = {"font":font, "port":port, "ip":ip, "icons_path":icons_path, "download_path": download_path, "homebrew":hb, "language":lang}
        with open(f"{self.temp_path}Settings.json", "w+") as file:
            json.dump(data, file)
        
        # Sometimes saving without the window
        try: self.OptionsWin.close() 
        except: pass


    def get_path(self, type):
        """ Render browsing window to pick default paths """
        opt = QtWidgets.QFileDialog.Options()
        opt |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(opt)
        dialog.setDirectory(self.path.get('app_root_path'))
        if type == "download":
            path = QtWidgets.QFileDialog.getExistingDirectory(
                None, "Default download folder...", self.path.get('app_root_path'), options=opt
            )
            if path: self.DownloadPath.setText(path)
        else:
            path = QtWidgets.QFileDialog.getExistingDirectory(
                None, "Default icons folder...", self.path.get('app_root_path'), options=opt
            )
            if path: self.IconPath.setText(path)