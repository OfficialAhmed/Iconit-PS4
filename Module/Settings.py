"""
    The only class from Module that doest inherit from (Common)
    So we can call the methods from Common without polymorphism

    * local attributes can be called without inheritence
    * init custom method called only once to change class's local attr for any obj access
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import json

class Main:
    paths: dict = {}
    DEFAULT_SETTINGS: dict = {}
    local_settings_cache: dict = {}

    def __init__(self) -> None:
        self.init()
        

    def init(self, cache_path="", lang_path="", data = {}, is_for_local_attr=False) -> None:
        """ fetch paths from environment class. [Called once by environment on init only] """
        
        # sharable attr for other objects (child class)
        if is_for_local_attr:
            Main.paths["language_path"] = lang_path
            Main.paths["cache_path"] = cache_path
            Main.local_settings_cache = data
            Main.DEFAULT_SETTINGS = data

        self.path = Main.paths
        self.local_settings_cache = Main.local_settings_cache
        
        self.cache_path = self.path.get('cache_path')
        self.language_path = self.paths.get("language_path")


    def reset_to_defaults(self):
        """ overwrite external file (Settings.json) by default settings """

        try:
            with open(f"{self.cache_path}Settings.json", "w+") as file:
                json.dump(Main.DEFAULT_SETTINGS, file)

            self.update_local_cache(self.cache_path)
            self.OptionsWin.close()
        except: pass


    def update_local_cache(self, cache_path) -> dict:
        """ Update the class's cache from external file (Settings.json) & return attributes"""

        try:
            with open(f"{cache_path}Settings.json", encoding="utf-8") as file:
                Main.local_settings_cache = json.load(file)
                self.local_settings_cache = Main.local_settings_cache
        except: pass
        finally: 
            data = {
                "ip":self.local_settings_cache.get("ip"), 
                "font":self.local_settings_cache.get("font"), 
                "port":self.local_settings_cache.get("port"), 
                "homebrew":self.local_settings_cache.get("homebrew"), 
                "language":self.local_settings_cache.get("language"),
                "icons_path":self.local_settings_cache.get("icons_path"), 
                "download_path":self.local_settings_cache.get("download_path")            
            }
            return data


    def save_cache(self, font:str = "", icons_path:str = "", download_path:str = "", hb:str = "", port:str = "", ip:str = "", lang:str = "", window=False) -> None:
        """ Cache information to external file Settings.json """

        # update local cache before using it
        self.update_local_cache(self.cache_path)

        # replace empty parameters with the local cache
        if not ip: ip = self.local_settings_cache.get("ip")
        if not hb: hb = self.local_settings_cache.get("homebrew")
        if not port: port = self.local_settings_cache.get("port")
        if not font: font = self.local_settings_cache.get("font")
        if not icons_path: icons_path = self.local_settings_cache.get("icons_path")
        if not download_path: download_path = self.local_settings_cache.get("download_path")
        if not lang: lang = self.local_settings_cache.get("language")
    
        data = {"font":font, "port":port, "ip":ip, "icons_path":icons_path, "download_path": download_path, "homebrew":hb, "language":lang}
        with open(f"{self.cache_path}Settings.json", "w+") as file:
            json.dump(data, file)
        
        if window: 
            self.OptionsWin.close() 


    def render_path_window(self, type) -> None:
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