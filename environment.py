"""
    Common: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
"""
from Module.Settings import Main as Settings

import os, datetime
from ftplib import FTP

class Common:
    def __init__(self) -> None:
        self.app_version = "5.05"
        self.app_release_date = "Jan 21st, 2023"

        self.screen_w = 0
        self.screen_h = 0

        self.ftp = FTP()
        self.working_dir = "user/appmeta"
        self.local_path = str(os.getcwd())
        self.local_path = self.local_path.replace("\\", "/")
        self.temp_path = self.local_path + "\Data\prxUserMeta\\"
        self.img_dir = self.local_path + "\\data\\User\\appmeta"

        self.sys_path = "system_ex/app"
        self.setting_path = ""

        self.IP = "not accepted"
        self.Port = 21

        self.all_CUSA = []
        self.all_CUSA_ex = []
        self.all_CUSA_sys = []
        self.Game = {}

        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIp = ""
        self.userIPath = self.local_path
        self.userDPath = self.local_path
        self.userHB = "False"
        self.settings = Settings()
    
    def get_update_release_date(self) -> None:
        return self.app_release_date

    def get_update_version(self) -> None:
        return self.app_version

    def set_screen_size(self, w, h) -> None:
        self.screen_w = w
        self.screen_h = h

    def playSound(self, path):
        try:
            import pygame

            pygame.mixer.init()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(loops=-1)
        except Exception as e:
            pass

    def logs(self, description, Type):
        try:
            error_file = open("Logs.txt", "a")
        except:
            error_file = open("Logs.txt", "w")

        if Type == "Warning":
            error_file.write(
                str(datetime.datetime.now())
                + " | "
                + "_DEV Warning: "
                + str(description)
                + "\n"
            )
        else:
            error_file.write(
                str(datetime.datetime.now())
                + " | "
                + "_DEV ERROR: "
                + str(description)
                + "\n"
            )

class html:
    def __init__(self) -> None:
        self.start = "<html><head/><body>"
        self.end = "</p></body></html>"

    def a_tag(self, href: str, txt: str, color: str, size: int, cstm_style: str = "", align: str = "center") -> str:
        ##############################################
        ####             HTML Link
        ##############################################
        return f'{self.start}<p align="{align};"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}">{txt}</span></a>{self.end}'

    def span_tag(self, txt: str, color: str, size: int, align="center", weight=700) -> str:
        ##############################################
        ####             HTML Text
        ##############################################
        return f'{self.start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color};">{txt}</span>{self.end}'

# class User_Prefrence(Environment):
#     # user settings and prefs here
#     def __init__(self) -> None:
#         super().__init__()


    