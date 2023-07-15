"""
    Common: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
    constant: class holds constant vars. Only getters
"""
from ftplib import FTP

import os, datetime, shutil, json
import concurrent.futures
import Module.Alerts as Alerts

from Module.Settings import Main as Settings
from Module.Widget.Shared import Widget

from Module.Widget.Translate import Translate
from Module.Database.Generate import Game_Database, System_Database

from Module.Constant.Html import Html
from Module.Constant.Constants import Constants as Constant


class Common:
    """
        * A Bridge class to connect between multiple classes 'different window process'
        
        Class attributes accessable anywhere `SHARABLE ACCROSS CHILDS`
            - (Change attribute value) via setters
            - (Access attribute value) via direct call i.e. 'class_name.attr_name'
        
        init attributes are child specific.
        Childs of this class have a copy of those attributes `NOT SHARABLE ACCROSS CHILDS`
            - (Change attribute value) via self assignment & setters
            - (Access attribute value) via self call
    """

    #__________  Settings.json default state _________  #
    app_path = os.getcwd()
    default_settings = {"font":"Arial", "port":"21", "ip":"", "icons_path":app_path, "download_path":app_path, "homebrew":"False", "language":"English"}
    

    #__________  shared attrs _________  #
    screen_w = 0
    screen_h = 0
    ui = None
    window = None


    #__________ Store connection for GoldHen one connection  _________________ #
    connection = None 
    selected_mode = None

    current_game_id = ""
    browsed_icon_path = ""
    browsed_pic_path = ""


    #__________ Common mask baker window widgets _________________ #
    state_widget = None
    upload_btn_widget = None


    #__________ Different modes mapping _________________ #
    mode:dict = {
        "game" : {
            "ids" : {},
            "ignore ids" : {},
            "ignored file" : f"{app_path}\\Data\\Cache\\Icons\\metadata\\game\\ignored.json",
            "cache path" : f"{app_path}\\Data\\Cache\\Icons\\metadata\\game" + "\\",
            "cache file" : f"{app_path}\\Data\\Cache\\Icons\\metadata\\game\\games.json",
            "default group path" : f"{app_path}\\Data\\Cache\\Groups\\Backup\\",
            "database" : Game_Database(f"{app_path}\\Data\\Cache\\Icons\\metadata\\game\\Database.json")
        },

        "system apps" : {
            "ids" : {},
            "ignore ids" : {},
            "ignored file" : f"{app_path}\\Data\\Cache\\Icons\\metadata\\system apps\\ignored.json",
            "cache path" : f"{app_path}\\Data\\Cache\\Icons\\metadata\\system apps" + "\\",
            "cache file" : f"{app_path}\\Data\\Cache\\Icons\\metadata\\system apps\\system_apps.json",
            "database" : System_Database(f"{app_path}\\Data\\Cache\\Icons\\metadata\\system apps\\Database.json")
        },

        "avatar" : {
            "ids" : {},
            "ignore ids" : {},
            "cache path" : "",
            "cache file" : "",
            "database" : ""
        }
    }


    def __init__(self) -> None:
        self.app_version = "5.13"
        self.app_release_date = "July 14th, 2023"

        self.external_game_ids = []
        self.screen_w = Common.screen_w
        self.screen_h = Common.screen_h
        
        self.app_root_path = f"{Common.app_path}" + "\\"
        self.data_path = f"{self.app_root_path}Data" + "\\"
        self.temp_path = f"{self.data_path}Cache" + "\\"
        self.groups_path = f"{self.temp_path}Groups" + "\\"
        self.groups_backup_path = f"{self.groups_path}Backup" + "\\"
        self.pref_path = f"{self.data_path}Preference" + "\\"
        self.icons_cache_path = f"{self.temp_path}Icons" + "\\"
        self.language_path = f"{self.data_path}Language" + "\\"
        self.appmeta_path = f"{self.data_path}User\\appmeta" + "\\"
        self.metadata_path = f"{self.temp_path}Icons\\metadata" + "\\"

        self.baked_path = f"{self.groups_path}Baked" + "\\"
        self.last_baked_group_file = f"{self.baked_path}last_process"
        self.default_group_file = f"{self.groups_path}Default.json"
        self.undetected_games_file = f"{self.app_root_path}GAMES MADE CACHING SLOWER.txt"
        self.setting_path = ""

        self.ftp:FTP = FTP()
        self.html:Html = Html()
        self.widgets:Widget = Widget()
        self.constant:Constant = Constant()
        self.settings:Settings = Settings()
        
        self.settings.init(self.temp_path, self.language_path, self.default_settings, is_for_local_attr=True)
        self.translation = Translate(self.language_path)


        self.ps4_system_icons_dir = self.constant.get_system_icons_path()
        self.ps4_internal_icons_dir = self.constant.get_internal_icons_path()
        self.ps4_external_icons_dir = self.constant.get_external_icons_path()

        self.backup_path = f"{self.constant.get_backup_folder_name()}" + "\\"
        
        self.settings_cache:dict = self.settings.update_local_cache(self.temp_path)
        self.ip:str = self.settings_cache.get("ip")
        self.font:str = self.settings_cache.get("font")
        self.port:str = self.settings_cache.get("port")
        self.language:str = self.settings_cache.get("language")
        self.icons_path:str = self.settings_cache.get("icons_path")
        self.is_toggled_homebrew:str = self.settings_cache.get("homebrew")
        self.download_path:str = self.settings_cache.get("download_path")

        self.alerts = Alerts.Main(self.translation, self.language)
        self.logging = self.html.internal_log_msg("ps4", self.ip, 12, "font-weight:600; font-style:italic;")


    def get_ps4_game_location(self, game_id:str) -> str:
        """ 
            if game exists internally return empty, else external
        """

        folder = ""
        if self.get_ids().get(game_id).get("location") == "External": 
            folder = "/external/"

        return f"{self.ps4_internal_icons_dir}{folder}{game_id}"
    

    def log_to_external_file(self, description:str, Type:str) -> None:
        """ 
            Write info about the issue to external file 
        """

        data = lambda : f"{datetime.datetime.now()} | _DEV {Type.upper()}: {description}\n"

        try: error_file = open("Logs.txt", "a")
        except: error_file = open("Logs.txt", "w+")
        error_file.write(data())


    def get_server_list(self, list:str = "directories") -> tuple:
        """ 
            This is a solution since PS4 ftp doesnt support nlst(). 
            * list: files = name of files if any 
            * list: directories = directories names if any 
        """
        result = []
        command = lambda line : result.append(line.split(" ")[-1])
        
        if list == "files":
            command = lambda line : result.append(line.split(" ")[-1]) if line[:2] == "-r" else None
        
        self.ftp.retrlines("LIST ", command)
        return tuple(result)


    def download_data_from_server(self, file_name:str, file_path_with_extension:str) -> bool:
        """
            download icons/xml etc from PS4
        """

        try:
            with open(file_path_with_extension, "wb") as downloaded_file:
                self.ftp.retrbinary("RETR " + file_name, downloaded_file.write, 5120)
                return True
            
        except:
            return False


    def progress_bar(self, bar, percentage:int) -> None:
        """ 
            Refresh the bar object by the passed percentage 
        """

        bar.setProperty("value", percentage)


    def backup_icons(self, src, dest, ids) -> None:
        """ 
            copy icons using threads 
        """

        store_icon = lambda id: shutil.copy(f"{src}{id}.png", f"{dest}\\{id}.png")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit each image as a separate task - if the icon not found in backup pass it to a thread to copy
            tasks = [executor.submit(store_icon, id) for id in ids if not os.path.exists(f"{dest}\\{id}.png")]
            
            # Wait for all tasks to complete on the thread
            concurrent.futures.wait(tasks)


    def read_json(self, json_path:str) -> dict:
        """
            Return JSON object as dictionary
            Takes only path as str, no streaming
        """

        return json.load(open(json_path))


    def get_language(self) -> str:
        return Common.language

    def set_language(self, lang) -> None:
        Common.language = lang

    def get_window(self):
        return Common.window

    def set_window(self, ptr) -> None:
        Common.window = ptr

    def set_ui(self, ptr) -> None:
        Common.ui = ptr

    def get_ui(self):
        return Common.ui

    def set_ftp(self, ptr) -> None:
        Common.connection = ptr

    def get_ftp(self):
        return Common.connection
        
    def set_current_game_id(self, id:str) -> None:
        Common.current_game_id = id

    def get_current_game_id(self) -> str:
        return Common.current_game_id

    def set_browsed_pic_path(self, path:str) -> None:
        Common.browsed_pic_path = path

    def get_browsed_pic_path(self) -> str:
        return Common.browsed_pic_path

    def set_browsed_icon_path(self, path:str) -> None:
        Common.browsed_icon_path = path

    def get_browsed_icon_path(self) -> str:
        return Common.browsed_icon_path

    def set_ids(self, ids:dict) -> None:
        Common.mode.get(self.get_selected_mode())["ids"] = ids

    def get_ids(self) -> dict:
        return Common.mode.get(self.get_selected_mode()).get("ids")

    def set_selected_mode(self, mode:str) -> None:
        Common.selected_mode = mode

    def get_selected_mode(self) -> str:
        return Common.selected_mode

    def set_ip_port(self, ip, port) -> None:
        Common.default_settings["ip"], self.ip = ip, ip
        Common.default_settings["port"], self.port = port, port

    def get_ip(self) -> str:
        return Common.default_settings.get("ip")

    def get_port(self) -> int:
        return int(Common.default_settings["port"])
        
    def set_screen_size(self, w, h) -> None:
        Common.screen_w = w
        Common.screen_h = h

    def set_state_widget(self, widget:Widget):
        Common.state_widget = widget

    def get_state_widget(self) -> Widget:
        return Common.state_widget

    def set_upload_btn_widget(self, widget:Widget):
        Common.upload_btn_widget = widget

    def get_upload_btn_widget(self) -> Widget:
        return Common.upload_btn_widget