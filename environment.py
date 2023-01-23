"""
    Common: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
    constant: class holds constant vars. Only getters
"""
from Module.Settings import Main as Settings
from Module.Widget.Shared import Widget
from ftplib import FTP

import os, datetime
import pygame

class Common:
    """
        * A Bridge class to connect between multiple ones
        
        Class attributes accessable anywhere (SHARABLE ACCROSS CHILDS)
            - (Change attribute value) via setters
            - (Access attribute value) via direct call i.e. 'class_name.attr_name'
        
        init attributes are child specific.
        Childs of this class have a copy of those attributes (NOT SHARABLE ACCROSS CHILDS)
            - (Change attribute value) via self assignment & setters
            - (Access attribute value) via self call
    """

    #__________  if pref.ini not found use these _________#
    userFont = "Arial"
    userPort = "21"
    userIp = "192.168.1.1"
    userIPath = os.getcwd()
    userDPath = os.getcwd()
    userHB = "False"
    
    #__________  shared attrs _________#
    IP = "not accepted"
    Port = 21
    screen_w = 0
    screen_h = 0
    ui = None
    window = None

    all_game_ids = {}
    selected_mode = None

    current_game_id = ""
    browsed_icon_path = ""
    browsed_bg_img_path = ""

    upload_type = ""
    is_sys_icon = False

    def __init__(self) -> None:
        self.app_version = "5.06"
        self.app_release_date = "Jan 24th, 2023"

        self.game = {}
        self.game_ids = []
        self.sys_game_ids = []
        self.external_game_ids = []

        self.IP = Common.IP
        self.Port = Common.Port
        self.userIp = Common.userIp
        self.userHB = Common.userHB
        self.userFont = Common.userFont
        self.userPort = Common.userPort
        self.userIPath = Common.userIPath
        self.userDPath = Common.userDPath
        
        self.screen_w = Common.screen_w
        self.screen_h = Common.screen_h

        self.ftp = FTP()
        self.html = html()
        self.widgets = Widget()
        self.constant = Constant()

        self.ps4_internal_icons_dir = self.constant.PS4_INT_ICONS
        self.ps4_external_icons_dir = self.constant.PS4_EXT_ICONS
        self.ps4_system_icons_dir = self.constant.PS4_SYS_ICONS

        self.app_root_path = f"{os.getcwd()}\\"
        self.pref_path = f"{self.app_root_path}Data\\Pref\\"
        self.temp_path = f"{self.app_root_path}Data\\Cache\\"
        self.metadata_path = f"{self.temp_path}Icons\\metadata\\"
        self.appmeta_path = f"{self.app_root_path}data\\User\\appmeta\\"
        self.cache_path = f"{self.metadata_path}game\\"
        self.setting_path = ""

        self.database_file = f"{self.temp_path}Title\\database.json"
        self.game_cache_file = f"{self.cache_path}games.json"
        self.logging = self.html.internal_log_msg("ps4", self.IP, 12, "font-weight:600; font-style:italic;")

        self.settings = Settings()
        self.update_pref()
        pygame.mixer.init()
   
    def get_window(self):
        return Common.window

    def set_window(self, ptr):
        Common.window = ptr

    def set_ui(self, ptr):
        Common.ui = ptr

    def get_ui(self):
        return Common.ui

    def get_server_directories(self) -> list:
        " This is a solution since PS4 ftp doesnt support nlst()."
        result = []
        self.ftp.retrlines("LIST ", lambda line : result.append(line.split(" ")[-1]))
        return result

    def download_data_from_server(self, file_name, file_path_with_extension) -> None:
        with open(file_path_with_extension, "wb") as downloaded_file:
            self.ftp.retrbinary("RETR " + file_name, downloaded_file.write)

    def set_browsed_bg_img_path(self, path:str):
        Common.browsed_bg_img_path = path

    def get_browsed_bg_img_path(self):
        return Common.browsed_bg_img_path

    def set_is_sys_icon(self, sys:bool):
        Common.is_sys_icon = sys

    def get_is_sys_icon(self):
        return Common.is_sys_icon

    def set_upload_type(self, t:str):
        Common.upload_type = t

    def get_upload_type(self):
        return Common.upload_type

    def set_current_game_id(self, id:str):
        Common.current_game_id = id

    def get_current_game_id(self):
        return Common.current_game_id
        
    def set_browsed_icon_path(self, path:str):
        Common.browsed_icon_path = path

    def get_browsed_icon_path(self):
        return Common.browsed_icon_path

    def set_game_ids(self, ids:dict):
        if ids:
            sorted_ids = sorted(ids.items(), key=lambda data: data[1].get("title"))
        Common.all_game_ids = dict(sorted_ids)

    def get_all_game_ids(self):
        return Common.all_game_ids

    def set_selected_mode(self, mode:str):
        Common.selected_mode = mode

    def get_selected_mode(self):
        return Common.selected_mode

    def update_pref(self):
        self.settings.set_defaults(
            self.userIp,
            self.userHB,
            self.userFont,
            self.userPort,
            self.userIPath,
            self.userDPath,
            self.pref_path,
            self.app_root_path
        )
        settings_cache = self.settings.update_cache(self.pref_path)

        font = settings_cache[0]
        port = settings_cache[1]
        ip = settings_cache[2]
        Ipath = settings_cache[3]
        Dpath = settings_cache[4]
        hb = settings_cache[5]
        self.set_user_pref(ip, port, font, Ipath, Dpath, hb)
        
    def set_ip_port(self, ip, port) -> None:
        """ Make Ip and Port sharable between classes """
        self.IP = ip
        self.Port = port
        Common.IP = ip
        Common.Port = port

    def get_ip(self):
        return Common.IP

    def get_port(self):
        return int(Common.Port)
        
    def set_screen_size(self, w, h) -> None:
        self.screen_w = w
        self.screen_h = h
        Common.screen_w = w
        Common.screen_h = h

    def set_user_pref(self, ip, port, font, i_path, d_path, hb):
        self.userIp = ip
        self.userHB = hb
        self.userFont = font
        self.userPort = port
        self.userIPath = i_path
        self.userDPath = d_path
        Common.userIp = ip
        Common.userHB = hb
        Common.userFont = font
        Common.userPort = port
        Common.userIPath = i_path
        Common.userDPath = d_path

    def play_sound(self, location, loop=False) -> None:
        try:
            pygame.mixer.music.load(location)
            if loop:
                pygame.mixer.music.play(loops=-1)
            else:
                pygame.mixer.music.play()
        except Exception as e:
            self.logs("Cannot run music and sounds", str(e))

    def logs(self, description, Type):
        try:
            error_file = open("Logs.txt", "a")
        except:
            error_file = open("Logs.txt", "w+")

        error_file.write(
            f"{str(datetime.datetime.now())}| _DEV {Type}: {str(description)} \n"
        )
    
class html:
    def __init__(self) -> None:
        self.start = "<html><head/><body>"
        self.end = "</p></body></html>"
        self.constant = Constant()

    def p_tag(self, cstm_style, txt=None) -> str:
        """  generate Paragraph """
        return f'<p align="center" style="{cstm_style}">{txt}</p>'

    def a_tag(self, href:str, txt:str, color:str, size:int, cstm_style: str = "", align: str = "center", font="Arial") -> str:
        """  generate Link """
        return f'{self.start}<p align="{align}"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}; font-family: {font}">{txt}</span></a>{self.end}'
        
    def span_tag(self, txt:str, color:str, size:int, align:str = "center", weight = 700, font="Arial") -> str:
        """  generate Text """
        return f'{self.start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color}; font-family: {font}">{txt}</span>{self.end}'

    def tooltip_tag(self, txt:str) -> str:
        return f"<p style='color:Black'>{txt}</p>"

    def bg_image(self, url:str) -> str:
        return f"background-image: url({url});"

    def border_image(self, url:str) -> str:
        return f"border-image: url({url});"

    def internal_log_msg(self, state, msg, size=10, custome_style="") -> str:
        """ generate a logging line as <p> tag"""
        color = {
            "error":self.constant.get_color("red"),
            "warning":self.constant.get_color("orange"),
            "success":self.constant.get_color("green"),
            "ps4":self.constant.get_color("white")
        }

        style = f"margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:{size}pt; color:{color[state]}; {custome_style}"
        return self.p_tag(style, f"[{state.upper()}] : {msg}")

class Constant:
    """ Read-only class """

    PS4_INT_ICONS = "user/appmeta"
    PS4_EXT_ICONS = "user/appmeta/external"
    PS4_SYS_ICONS = "system_ex/app"
    PS4_ICON_SIZE = (512, 512)
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
