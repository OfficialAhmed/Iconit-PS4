"""

    Methods for the main screen 'Iconit window'
    the class inherits 'Common'

"""
import Interface.Icons as Icons
import Interface.Avatars as Avatars
import Interface.Alerts as Alerts
import Interface.Settings as Settings

from environment import Common

from PyQt5 import QtWidgets
from xml.dom import minidom  # XML parsing

import os, json

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

        self.icon_name = "icon0.png"
        self.file_name = self.constant.PS4_PRONOUNCIATION_FILE
        self.Eng1 = [chr(x) for x in range(ord("a"), ord("a") + 26)]  # a - z
        self.Eng2 = [chr(x) for x in range(ord("A"), ord("A") + 26)]  # A - Z
        self.Eng = self.Eng1 + self.Eng2
        self.Eng.append(" ")
        self.alphaNum = (
            "one", 
            "two", 
            "three",
            "four", 
            "five", 
            "six", 
            "seven",
            "eight",
            "nine",
            "™",
            "'",
            "!",
            "?",
        )

        self.cached = ""
        self.game_cache = {}
        self.unchecked_game_ids = []
        self.is_external_icons_found = False

    def open_options(self):
        self.window = QtWidgets.QDialog()
        self.ui = Settings.Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_about(self):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()
        self.ui.setupUi(self.window)
        self.ui.alert("About")
        self.window.show()

    def open_credits(self):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()
        self.ui.setupUi(self.window)
        self.ui.alert("CUSTOMspecial_thanks")
        self.window.show()

    def remove_cache(self):
        self.window = QtWidgets.QDialog()
        ui = Alerts.Ui()
        ui.setupUi(self.window)
        try:
            all = os.listdir(self.cache_path)
            for game in all:
                os.remove(f"{self.cache_path}{game}")
            ui.alert("CUSTOMdoneRmvCache")
        except PermissionError:
            ui.alert("PermissionDenied")
        except Exception as e:
            ui.alert(str(e))

        self.window.show()

    def check_ip_port(self) -> None:
        self.StatusLabel.setText(self.html.span_tag("Connecting...", "#f2ae30", 18))
        try:
            self.ip = self.IpInput.text()
            self.port = self.PortInput.text()
            
            self.settings.save_cache(ip = self.ip, port = self.port)
            self.set_ip_port(self.ip, self.port) 

            is_valid = False
            if len(self.ip) > 8:
                for i in f"{self.ip}{self.port}":
                    if i.isalpha():
                        break
                else:
                    is_valid = True
            self.connect_ps4(is_valid)

        except Exception as e:
            self.logs(str(e), "Warning")

    def change_colors(self, connected: bool) -> None:
        labels = {
            self.IpLabel: "PS4 IP",
            self.PortLabel: "PS4 Port",
            self.ModeLabel: "Mode",
            self.CacheLabel: "Cache",
        }

        success = "rgb(92, 213, 21)"
        fail = "rgb(255, 0, 0)"
        
        if connected:
            self.StatusLabel.setText(self.html.span_tag("Connected", success, 18))
        else:
            self.StatusLabel.setText(self.html.span_tag("Failed to connect", fail, 18))
            
        for l in labels:
            if connected:
                l.setText(self.html.span_tag(labels[l], success, 14))
            else:
                l.setText(self.html.span_tag(labels[l], fail, 14))

    def set_cache(self) -> None:
        if self.get_selected_mode() == "game":
            with open(self.game_cache_file, "w+") as jsonFile:
                json.dump(self.game_ids, jsonFile)

    def get_cache(self) -> dict:
        result = {}
        if os.path.isfile(self.game_cache_file):
            ReadJson = open(self.game_cache_file)
            result = json.load(ReadJson)
        return result

    def filter_game_ids(self):
        def get_game_id(line):
            """
            #######################################################
                read server directory line by line for ids
            #######################################################
            """
            
            is_accepted = True
            game_id = line.split(" ")[-1]

            if not bool(self.userHB):
                if "CUSA" not in game_id:
                    is_accepted = False
                    try:
                        self.game_cache.pop(game_id)
                    except:
                        pass

            if is_accepted:
                self.unchecked_game_ids.append(game_id)

        for dir in self.dirs:
            self.ftp.cwd(f"/{dir}")

            """
            #######################################################
                read server directory line by line for ids
            #######################################################
            """
            self.ftp.retrlines("LIST ", lambda line: get_game_id(line)
                if len(line.split(" ")[-1]) >= 8 
                and line[0].lower() == "d" 
                else None
            )
           
            """
            #######################################################
                check if id is valid folder, and append to list
            #######################################################
            """
            for id in self.unchecked_game_ids:
                self.ftp.cwd(f"/{dir}/{id}")
                game_files = self.get_server_directories()
                
                if self.constant.PS4_PRONOUNCIATION_FILE in game_files:
                    location = "External" if "external" in dir else "Internal"
                    self.game_ids.append((id, location))

            self.unchecked_game_ids.clear()
        self.set_game_ids(self.game_ids)

    def connect_ps4(self, is_valid):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()

        if is_valid:
            """
                    Naive Approach  ;)
                Solution for one connection only (GoldHen FTP)
                *Try to connect, otherwise, try to close the connection might not been closed properly before.
                *Never close connection until we move to the next window
                *Avoid reconnceting to step back to root dir, Change dir manually (/)
            """
            
            try:
                self.ftp.set_debuglevel(0)
                self.ftp.connect(self.ip, int(self.port))
                self.ftp.login("", "")
                self.ftp.getwelcome()
            except ConnectionRefusedError:
                self.change_colors(False)
                self.ui.setupUi(self.window)
                self.ui.alert("Cannot make connection with the given IP/Port. DEV| ConnectionRefusedError")
                self.window.show()
                return
            except Exception as e:
                self.ftp.close()
                self.logs(str(e), "Error")
                self.change_colors(False)
                self.ui.setupUi(self.window)
                self.ui.alert(f"Double check IP and PORT. DEV|{str(e)}")
                self.window.show()
                return

            ##############################################
            ###       User Picked Game Icon
            ###############################################
            self.StatusLabel.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
            if self.GameIconsRadio.isChecked():
                # v4.72 json for caching
                self.game_cache = self.get_cache()

                self.set_selected_mode("game")
                self.ftp.cwd(self.ps4_internal_icons_dir)
                if "external" not in self.get_server_directories():
                    self.dirs = (self.ps4_internal_icons_dir, )
                else:
                    self.is_external_icons_found = True
                    self.dirs = (self.ps4_internal_icons_dir, self.ps4_external_icons_dir)

                self.filter_game_ids()
                self.change_colors(True)
                self.cache_game_icon() 

            ##############################################
            ###       User picked Sys icons
            ###############################################
            elif self.SystemIconsRadio.isChecked():
                self.ftp.cwd("/")
                self.ftp.cwd(self.ps4_system_icons_dir)

                sys_files = self.self.get_server_directories()

                self.change_colors(True)

                for sys_game in sys_files:
                    if len(sys_game) == 9:
                        self.ftp.cwd(sys_game)
                        folders_inside = self.self.get_server_directories()
                        if "sce_sys" in folders_inside:
                            self.ftp.cwd("sce_sys")
                            files_inside = self.self.get_server_directories()
                            if "icon0.png" in files_inside:
                                self.sys_game_ids.append(sys_game)

                    self.ftp.cwd("/")
                    self.ftp.cwd(self.ps4_system_icons_dir)

                self.CacheSysIcon()
            ##############################################
            ###       User picked Avatar change
            ###############################################
            else:
                self.sysProfileRoot = "system_data/priv/cache/profile/"
                self.ftp.cwd("/")
                self.ftp.cwd(self.sysProfileRoot)
                self.userID = []

                self.change_colors(True)

                directories = []
                self.ftp.retrlines("LIST ", directories.append)

                with open(
                    self.temp_path + "directories in system.dat", "w+"
                ) as all_directories_in_system:
                    for line in directories:
                        all_directories_in_system.write(line + "\n")

                with open(self.temp_path + "directories in system.dat") as file:
                    lines = file.readlines()
                    for line in lines:
                        if "0x" in line:
                            account_index = line.index("0x")
                            self.userID.append(line[account_index:-1])
                self.cache_change_avatar()
        else:
            self.window = QtWidgets.QDialog()
            self.change_colors(False)
            self.ui.setupUi(self.window)
            self.ui.alert("Double check PS4 IP and Port\n Note: If you're using GoldHen FTP\n make sure you're not connected to the PS4 with a different app as it only allow one connection")
            self.window.show()

    def cache_change_avatar(self):
        ###############################################
        #            Prepare Avatars
        ################################################

        fileName = "online.json"
        dir = self.temp_path + "MegaSRX\metaprodata\\"
        # Remove old data
        if len(os.listdir(dir)) != 0:
            data = os.listdir(dir)
            try:
                for i in data:
                    os.remove(dir + i)
            except Exception as e:
                self.logs(str(e), "Warning")

        progress = int(100 / len(self.userID))
        progressed = 0
        self.CacheBar.setProperty("value", 1)

        for user in self.userID:
            self.ftp.cwd("/")
            self.ftp.cwd(self.sysProfileRoot + "/" + user)

            with open(dir + "\\" + user + ".png", "wb") as file:
                # cache avatar if available
                try:
                    self.ftp.retrbinary("RETR " + "avatar.png", file.write, 1024)
                except Exception as e:
                    self.logs(str(e), "Warning")
            with open(dir + "\\" + user + ".json", "wb") as file:
                # Fix (v4.07) make a fake one if online json not found
                # fix (json not found) v4.51
                try:
                    self.ftp.retrbinary("RETR " + fileName, file.write, 1024)
                except Exception as e:
                    print(str(e))

                    import json

                    data = {
                        "avatarUrl": "http://static-resource.np.community.playstation.net/a/vatar_xl/WWS_E/E0012_XL.png",
                        "firstName": "Unknown",
                        "lastName": "username",
                        "pictureUrl": "https://image.api.np.km.playstation.net/images/?format=png&w=440&h=440&image=https%3A%2F%2Fkfscdn.api.np.km.playstation.net%2F00000000000008%2F000000000000003.png&sign=blablabla019501",
                        "trophySummary": '{"level":1,"progress":0,"earnedTrophies":{"platinum":0,"gold":0,"silver":0,"bronze":0}}',
                        "isOfficiallyVerified": "true",
                        "aboutMe": "Temporary file created by Iconit app by @OfficialAhmed0",
                    }

                    with open(dir + "\\" + user + ".json", "w+") as jsonFile:
                        json.dump(data, jsonFile, indent=4)

                    with open(dir + "\\" + user + ".json", "rb") as json:
                        self.ftp.storbinary("STOR online.json", json, 1024)

            # Download original Profile Icon from Sony server
            import requests as req

            try:
                with open(dir + "\\" + user + ".json") as file:
                    # Extract Icon url from json file
                    read = file.read()
                    url = read[
                        read.find("avatarUrl")
                        + len("avatarUrl")
                        + 3 : read.find(".png")
                        + len(".png")
                    ]
                    cont = url.split("\/")
                    link = ""

                    for i in cont:
                        if i != "":
                            link += i + "//"
                    img = req.get(link[:-2])

                    with open(dir + "\\" + user + "Original.png", "wb") as origIcon:
                        origIcon.write(img.content)

            except Exception as e:
                self.logs(str(e), "Warning")

            for i in range(1, progress):
                self.CacheBar.setProperty("value", progressed + i)

            progressed += progress

        self.CacheBar.setProperty("value", 100)
        self.render_window("ChangeAvatar")

    def CacheSysIcon(self):

        ###############################################
        #            Sys Icons impl v4.72
        ################################################

        global all_CUSA_sys
        GameWeightInFraction = (1 / len(all_CUSA_sys)) * 100
        percentage = 0
        self.ftp.set_debuglevel(0)
        self.ftp.cwd("/")
        self.ftp.cwd(self.ps4_system_icons_dir)

        for sysIcon in all_CUSA_sys:
            self.ftp.cwd(sysIcon + "/sce_sys")
            inside_sce_sys = self.self.get_server_directories()
            icon_2_fetch = "icon0.png"

            # fetch 4k version if found
            if "icon0_4k.png" in inside_sce_sys:
                icon_2_fetch = "icon0_4k.png"

            self.fetch_data_from_server(
                icon_2_fetch,
                f"{self.temp_path}MegaSRX\metadata\\{sysIcon}.png",
            )
            if self.file_name in inside_sce_sys:
                self.fetch_data_from_server(self.file_name, self.temp_path + self.file_name)

                diff_titles = []  # all different titles for current fetched game
                file = minidom.parse(self.temp_path + self.file_name).getElementsByTagName(
                    "text"
                )

                for name in file:
                    diff_titles.append(name.firstChild.data)

                GameTitle = ""
                for title in diff_titles:
                    english = True

                    for alpha in self.alphaNum:
                        if alpha in title or alpha.title() in title:
                            GameTitle = title
                            self.game_cache[sysIcon] = GameTitle
                        else:
                            for char in title:
                                if char not in self.Eng:
                                    english = False
                                    break
                    if english:
                        GameTitle = title
                        self.game_cache[sysIcon] = GameTitle
            else:
                if "NPXS" in sysIcon:
                    self.game_cache[sysIcon] = 'Unknown system icon "Sony didn\'t provide one :)"'
                else:
                    self.game_cache[sysIcon] = f"Cannot find title for {sysIcon}"

            self.ftp.cwd("/")
            self.ftp.cwd(self.ps4_system_icons_dir)
            percentage += GameWeightInFraction
            self.CacheBar.setProperty(
                "value", str(percentage)[: str(percentage).index(".")]
            )

        try:
            self.render_window("GameIcon")
        except Exception as e:
            print(str(e))

    def merge_game_id_and_title(self) -> None:
        result = {}

        for id, location in self.game_ids:
            result[id] = {"title":self.game_cache.get(id), "location":location}

        self.game_ids = result
        self.set_game_ids(result)
        self.set_cache()

    def cache_game_icon(self):
        ################################################
        #   Internal/External HDD Game Icons
        ################################################

        try:
            self.cached = os.listdir(self.cache_path)
            numGames = len(self.game_ids + self.sys_game_ids)
            GameWeightInFraction = (1 / numGames) * 100
            percentage = 0

            for game_info in self.game_ids:
                game_id = game_info[0]
                game_location = game_info[1]

                current_directory = self.ps4_internal_icons_dir
                if game_location == "External":
                    current_directory = self.ps4_external_icons_dir

                self.ftp.cwd(f"/{current_directory}/{game_id}")
                files = self.get_server_directories()
                
                if game_id not in self.game_cache:
                    # BUG: overwriting the cache mess up the whole dataset
                    
                    """
                    ###################################################
                        Fetch Game Title from server if not in cache
                    ###################################################
                    """

                    if (self.file_name in files or self.icon_name in files):
                        if self.file_name in files:
                            self.fetch_data_from_server(self.file_name, f"{self.temp_path}{self.file_name}")
                        if self.icon_name in files:
                            self.fetch_data_from_server(self.icon_name, f"{self.cache_path}{game_id}.png",)
                        diff_titles = (
                            []
                        )  # all different titles for current fetched game

                        try:
                            files = minidom.parse(
                                self.temp_path + self.file_name
                            ).getElementsByTagName("text")

                            for name in files:
                                diff_titles.append(name.firstChild.data)
                        except Exception as e:
                                diff_titles.append("UNKNOWN TITLE")

                        GameTitle = ""
                        for title in diff_titles:
                            if self.file_name in files:
                                GameTitle = title
                                self.game_cache[game_id] = GameTitle
                            else:
                                GameTitle = "Unknown"
                                self.game_cache[game_id] = GameTitle
                                break
                            english = True

                            for char in title:
                                if char not in self.Eng:
                                    english = False
                                    break
                            if english:
                                GameTitle = title
                                self.game_cache[game_id] = GameTitle
                                break

                    percentage += GameWeightInFraction
                    self.CacheBar.setProperty("value", str(percentage)[: str(percentage).index(".")])

            self.merge_game_id_and_title()
            try:
                self.render_window("GameIcon")
            except Exception as e:
                print(str(e))
        except Exception as e:
            self.logs(e, "Error")
            self.change_colors(False)
            self.ui.setupUi(self.window, str(e))
            self.window.show()

    def fetch_data_from_server(self, file_name, file_path_with_extension):
        self.StatusLabel.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
        with open(file_path_with_extension, "wb") as downloaded_file:
            self.ftp.retrbinary("RETR " + file_name, downloaded_file.write)

    def render_window(self, win_type):
        self.window = QtWidgets.QWidget()

        if win_type == "GameIcon":
            # FIXME: CANNOT OPEN ICONS WINDOW
            # self.ui = Icons.Ui()
            # self.ui.setupUi(self.window)
            # self.window.show()
            pass
        else:
            self.ui = Avatars.Ui()
            self.ui.setupUi(self.window, self.userID, self.ip, self.port, self.w, self.h)
            self.window.show()
