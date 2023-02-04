"""
    Common: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
    constant: class holds constant vars. Only getters
"""
import os, datetime
from ftplib import FTP
from Module.Settings import Main as Settings
from Module.Widget.Shared import Widget
from Module.Widget.Translate import Translate
from Module.Database.Generate import Game_database, System_database

class Common:
    """
        * A Bridge class to connect between multiple classes 'different window process'
        
        Class attributes accessable anywhere (SHARABLE ACCROSS CHILDS)
            - (Change attribute value) via setters
            - (Access attribute value) via direct call i.e. 'class_name.attr_name'
        
        init attributes are child specific.
        Childs of this class have a copy of those attributes (NOT SHARABLE ACCROSS CHILDS)
            - (Change attribute value) via self assignment & setters
            - (Access attribute value) via self call
    """

    #__________  if Settings.json not found use these _________#
    app_path = os.getcwd()
    default_settings = {"font":"Arial", "port":"21", "ip":"", "icons_path":app_path, "download_path":app_path, "homebrew":"False", "language":"English"}
    
    #__________  shared attrs _________#
    screen_w = 0
    screen_h = 0
    ui = None
    window = None

    # Store connection for GoldHen one connection 
    connection = None 

    all_game_ids = {}
    selected_mode = None

    current_game_id = ""
    browsed_icon_path = ""
    browsed_bg_img_path = ""

    upload_type = ""
    is_sys_icon = False

    def __init__(self) -> None:
        self.app_version = "5.11 BETA"
        self.app_release_date = "Feb 2nd, 2023"

        self.game = {}
        self.game_ids = {}
        self.system_apps_ids = {}
        self.external_game_ids = []
        self.screen_w = Common.screen_w
        self.screen_h = Common.screen_h

        self.app_root_path = f"{Common.app_path}\\"
        self.data_path = f"{self.app_root_path}Data\\"
        self.temp_path = f"{self.data_path}Cache\\"
        self.pref_path = f"{self.data_path}Preference\\"
        self.icons_cache_path = f"{self.temp_path}Icons\\"
        self.language_path = f"{self.data_path}Language\\"
        self.appmeta_path = f"{self.data_path}User\\appmeta\\"
        self.metadata_path = f"{self.temp_path}Icons\\metadata\\"
        self.game_cache_path = f"{self.metadata_path}game\\"
        self.system_apps_cache_path = f"{self.metadata_path}system\\"

        self.game_cache_file = f"{self.game_cache_path}games.json"
        self.game_database_file = f"{self.game_cache_path}Database.json"
        self.system_apps_database_file = f"{self.system_apps_cache_path}Database.json"
        self.system_apps_cache_file = f"{self.system_apps_cache_path}system_apps.json"
        self.undetected_games_file = f"{self.app_root_path}GAMES MADE CACHING SLOWER.txt"
        self.setting_path = ""

        self.ftp = FTP()
        self.html = html()
        self.widgets = Widget()
        self.constant = Constant()
        self.settings = Settings()
        self.settings.init(self.temp_path, self.language_path, self.default_settings, is_for_local_attr=True)
        self.game_database = Game_database(self.game_database_file)
        self.system_apps_database = System_database(self.system_apps_database_file)
        self.translation = Translate(self.language_path)

        self.ps4_system_icons_dir = self.constant.PS4_SYS_ICONS
        self.ps4_internal_icons_dir = self.constant.PS4_INT_ICONS
        self.ps4_external_icons_dir = self.constant.PS4_EXT_ICONS

        self.backup_path = f"{self.constant.ICONS_BACKUP_NAME}\\"

        self.settings_cache = self.settings.update_local_cache(self.temp_path)
        self.ip:str = self.settings_cache.get("ip")
        self.font:str = self.settings_cache.get("font")
        self.port:str = self.settings_cache.get("port")
        self.language:str = self.settings_cache.get("language")
        self.icons_path:str = self.settings_cache.get("icons_path")
        self.toggled_homebrew:str = self.settings_cache.get("homebrew")
        self.download_path:str = self.settings_cache.get("download_path")

        self.logging = self.html.internal_log_msg("ps4", self.ip, 12, "font-weight:600; font-style:italic;")


    def log_to_external_file(self, description:str, Type:str) -> None:
        """ Write info about the issue in an external file """
        data = lambda : f"{datetime.datetime.now()} | _DEV {Type.upper()}: {description}\n"

        try: error_file = open("Logs.txt", "a")
        except: error_file = open("Logs.txt", "w+")
        error_file.write(data())


    def get_server_list(self, list="directories") -> tuple:
        """ 
            This is a solution since PS4 ftp doesnt support nlst(). 
            list: files = name of files if any 
            list: directories = directories names if any 
        """
        result = []
    
        command = lambda line : result.append(line.split(" ")[-1])
        if list == "files":
            command = lambda line : result.append(line.split(" ")[-1]) if line[:2] == "-r" else None
        
        self.ftp.retrlines("LIST ", command)
        return tuple(result)


    def download_data_from_server(self, file_name, file_path_with_extension) -> bool:
        try:
            with open(file_path_with_extension, "wb") as downloaded_file:
                self.ftp.retrbinary("RETR " + file_name, downloaded_file.write, 5120)
                return True
        except:
            return False


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
        
    def set_browsed_pic_path(self, path:str) -> None:
        Common.browsed_bg_img_path = path

    def get_browsed_bg_img_path(self) -> str:
        return Common.browsed_bg_img_path

    def set_is_sys_icon(self, sys:bool) -> None:
        Common.is_sys_icon = sys

    def get_is_sys_icon(self) -> bool:
        return Common.is_sys_icon

    def set_upload_type(self, t:str) -> None:
        Common.upload_type = t

    def get_upload_type(self) -> str:
        return Common.upload_type

    def set_current_game_id(self, id:str) -> None:
        Common.current_game_id = id

    def get_current_game_id(self) -> str:
        return Common.current_game_id
        
    def set_browsed_icon_path(self, path:str) -> None:
        Common.browsed_icon_path = path

    def get_browsed_icon_path(self) -> str:
        return Common.browsed_icon_path

    def set_game_ids(self, ids:dict) -> None:
        Common.all_game_ids = ids

    def get_all_game_ids(self) -> dict:
        return Common.all_game_ids

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
        self.screen_w, Common.screen_w = w, w
        self.screen_h, Common.screen_h = h, h


class html:
    def __init__(self) -> None:
        self.__start = "<html><head/><body>"
        self.__end = "</p></body></html>"
        self.__constant = Constant()


    def p_tag(self, cstm_style, txt=None) -> str:
        """  generate Paragraph """
        return f'<p align="center" style="{cstm_style}">{txt}</p>'


    def a_tag(self, href:str, txt:str, color:str, size:int, cstm_style: str = "", align: str = "center", font="Arial") -> str:
        """  generate Link """
        return f'{self.__start}<p align="{align}"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}; font-family: {font}">{txt}</span></a>{self.__end}'
        

    def span_tag(self, txt:str, color:str, size:int, align:str = "center", weight = 700, font="Arial") -> str:
        """  generate Text """
        return f'{self.__start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color}; font-family: {font}">{txt}</span>{self.__end}'


    def tooltip_tag(self, txt:str) -> str:
        return f"<p style='color:Black'>{txt}</p>"


    def bg_image(self, url:str) -> str:
        return f"background-image: url({url});"


    def border_image(self, url:str) -> str:
        return f"border-image: url({url});"


    def internal_log_msg(self, state, msg, size=10, custome_style="") -> str:
        """ generate a logging line as <p> tag"""
        color = {
            "error":self.__constant.get_color("red"),
            "warning":self.__constant.get_color("orange"),
            "success":self.__constant.get_color("green"),
            "ps4":self.__constant.get_color("white")
        }

        style = f"margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:{size}pt; color:{color[state]}; {custome_style}"
        return self.p_tag(style, f"[{state.upper()}] : {msg}")


class Constant:
    """ Read-only class """

    PS4_PIC_SIZE = (1920, 1080)
    PS4_ICON_SIZE = (512, 512)
    PS4_INT_ICONS = "user/appmeta/"
    PS4_EXT_ICONS = "user/appmeta/external/"
    PS4_SYS_ICONS = "system_ex/app/"
    PS4_SYS_SCE = "sce_sys"
    PS4_PRONOUNCIATION_FILE = "pronunciation.xml"

    ICONS_BACKUP_NAME = "Backup"
    HASH_COLOR = {
        "red":"#e83c3c",
        "green":"#55ff00",
        "white":"#ffffff",
        "orange":"#ffaa00",
    }


    def __init__(self) -> None:
        # init the self parameter
        pass


    def __setattr__(self, __name: str, __value: any) -> None:
        raise AttributeError(f"READ-ONLY: Class 'Constant' allow getters only. Occured while trying to set [{__name}]")
        

    def get_color(self, x:str) -> str:
        return Constant.HASH_COLOR[x]
