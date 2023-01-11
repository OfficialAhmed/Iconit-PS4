"""
    Common: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
"""
from Module.Settings import Main as Settings
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

    IP = "not accepted"
    Port = 21
    screen_w = 0
    screen_h = 0

    # default settings
    userFont = "Arial"
    userPort = "21"
    userIp = ""
    userIPath = os.getcwd()
    userDPath = os.getcwd()
    userHB = "False"
    
    def __init__(self) -> None:
        self.app_version = "5.05"
        self.app_release_date = "Jan 21st, 2023"

        self.all_CUSA = []
        self.all_CUSA_ex = []
        self.all_CUSA_sys = []
        self.Game = {}

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

        self.logging = (
            f'<p align="center" style=" margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">*Connected to PS4: {self.IP}*</span></p>\n'
        )

        self.ftp = FTP()
        self.working_dir = "user/appmeta"
        self.local_path = str(os.getcwd())
        self.local_path = self.local_path.replace("\\", "/")
        self.temp_path = self.local_path + "\Data\prxUserMeta\\"
        self.img_dir = self.local_path + "\\data\\User\\appmeta"
        self.info_json_path = self.local_path + "\Data\prxUserMeta\MegaSRX\metadata\game\info.json"
        self.pref_location = self.local_path + "/Data/Pref/"

        self.sys_path = "system_ex/app"
        self.setting_path = ""
        self.settings = Settings()
        self.settings.set_defaults(
            self.userIp,
            self.userHB,
            self.userFont,
            self.userPort,
            self.userIPath,
            self.userDPath,
            self.pref_location,
            self.local_path
        )

        pygame.mixer.init()

    def set_ip_port(self, ip, port) -> None:
        self.IP = ip
        self.Port = port
        Common.IP = ip
        Common.Port = port
        
    def set_screen_size(self, w, h) -> None:
        self.screen_w = w
        self.screen_h = h
        Common.screen_w = w
        Common.screen_h = h

    def set_user_prefrence(self, ip, port, font, i_path, d_path, hb):
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

    def get_update_release_date(self) -> None:
        return self.app_release_date

    def get_update_version(self) -> None:
        return self.app_version

    def play_sound(self, location, loop=False) -> None:
        try:
            pygame.mixer.music.load(location)
            if loop:
                pygame.mixer.music.play(loops=-1)
            else:
                pygame.mixer.music.play()
        except:
            pass

    def logs(self, description, Type):
        try:
            error_file = open("Logs.txt", "a")
        except:
            error_file = open("Logs.txt", "w")

        error_file.write(
            f"{str(datetime.datetime.now())}\
        | _DEV {Type}: {str(description)} \n"
        )
    
class html:
    def __init__(self) -> None:
        self.start = "<html><head/><body>"
        self.end = "</p></body></html>"

    def a_tag(self, href: str, txt: str, color: str, size: int, cstm_style: str = "", align: str = "center") -> str:
        ##############################################
        ####             HTML Link
        ##############################################
        return f'{self.start}<p align="{align}"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}">{txt}</span></a>{self.end}'

    def span_tag(self, txt: str, color: str, size: int, align: str = "center", weight = 700) -> str:
        ##############################################
        ####             HTML Text
        ##############################################
        return f'{self.start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color};">{txt}</span>{self.end}'