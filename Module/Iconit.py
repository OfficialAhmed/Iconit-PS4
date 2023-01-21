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
        self.id_and_location = []
        self.game_title_file_path = f"{self.temp_path}{self.constant.PS4_PRONOUNCIATION_FILE}"
        self.game_title_file = self.constant.PS4_PRONOUNCIATION_FILE
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
        self.unchecked_game_ids = []
        self.is_external_icons_found = True

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
                        self.game_ids.pop(game_id)
                    except:
                        pass

            if is_accepted:
                self.unchecked_game_ids.append(game_id)

        for dir in self.icon_directories:
            self.ftp.cwd(f"/{dir}")

            """
            #######################################################
                read server directory line by line for ids
            #######################################################
            """
            self.ftp.retrlines("LIST ", lambda line: get_game_id(line)
                if len(line.split(" ")[-1]) >= 8 
                and line[0].lower() == "d" 
                and line.split(" ")[-1] not in self.game_ids
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
                    self.game_ids[id] = {"location":location}

            self.unchecked_game_ids.clear()

    def connect_ps4(self, is_valid):
        self.ui = Alerts.Ui()
        self.window = QtWidgets.QDialog()
        self.StatusLabel.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))

        if is_valid:
            try:
                self.ftp.set_debuglevel(0)
                self.ftp.connect(self.ip, int(self.port))
                self.ftp.login("", "")
                self.ftp.getwelcome()
                self.change_colors(True)
            except ConnectionRefusedError:
                self.change_colors(False)
                self.ui.setupUi(self.window)
                self.ui.alert("Cannot make connection with the given IP/Port. DEV| ConnectionRefusedError")
                self.window.show()
                return
            except Exception as e:
                self.ftp.close()
                self.change_colors(False)
                self.logs(str(e), "Error")
                self.ui.setupUi(self.window)
                self.ui.alert(f"Double check IP and PORT. DEV|{str(e)}")
                self.window.show()
                return

            if self.GameIconsRadio.isChecked():
                """
                #####################################################
                            User Picked Game Icon
                #####################################################
                """
                self.set_selected_mode("game")
                
                self.game_ids = self.get_cache()
                self.ftp.cwd(self.ps4_internal_icons_dir)
                self.icon_directories = (self.ps4_internal_icons_dir, self.ps4_external_icons_dir)
                if "external" not in self.get_server_directories():
                    self.icon_directories = (self.ps4_internal_icons_dir, )
                    self.is_external_icons_found = False

                self.filter_game_ids()
                self.cache_game_icons() 

            elif self.SystemIconsRadio.isChecked():
                """
                #####################################################
                            User picked Sys icons
                #####################################################
                """
                self.set_selected_mode("system")
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

                self.cache_system_icons()
            else:
                """
                #####################################################
                            User picked Avatar change
                #####################################################
                """
                self.set_selected_mode("avatars")

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
                self.cache_avatar_icons()
        else:
            self.window = QtWidgets.QDialog()
            self.change_colors(False)
            self.ui.setupUi(self.window)
            self.ui.alert("Double check PS4 IP and Port\n Note: If you're using GoldHen FTP\n make sure you're not connected to the PS4 with a different app as it only allow one connection")
            self.window.show()

    def cache_avatar_icons(self):
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
        self.render_window()

    def cache_system_icons(self):

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

            self.download_data_from_server(
                icon_2_fetch,
                f"{self.temp_path}MegaSRX\metadata\\{sysIcon}.png",
            )
            if self.game_title_file in inside_sce_sys:
                self.download_data_from_server(self.game_title_file, self.temp_path + self.game_title_file)

                diff_titles = []  # all different titles for current fetched game
                file = minidom.parse(self.temp_path + self.game_title_file).getElementsByTagName(
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
            self.render_window()
        except Exception as e:
            print(str(e))

    def cache_game_icons(self):
        try:
            self.StatusLabel.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
            self.cached = os.listdir(self.cache_path)
            numGames = len(self.game_ids)
            GameWeightInFraction = (1 / numGames) * 100
            percentage = 0
            game_ids_with_hb = self.game_ids.copy()

            for game_id in game_ids_with_hb:
                if self.userHB == "False": 
                    #skip homebrew
                    if "CUSA" not in game_id:
                        self.game_ids.pop(game_id)
                        continue

                game_location = self.game_ids.get(game_id).get("location")
                
                current_directory = self.ps4_internal_icons_dir
                if game_location == "External":
                    current_directory = self.ps4_external_icons_dir

                self.ftp.cwd(f"/{current_directory}/{game_id}")
                files = self.get_server_directories()
                
                if self.game_ids.get(game_id).get("title") == None:
                    
                    """
                    #######################################################
                        Fetch Game Title from server if title not in cache
                    #######################################################
                    """

                    if (self.game_title_file in files or self.icon_name in files):
                        if self.game_title_file in files:
                            self.download_data_from_server(self.game_title_file, self.game_title_file_path)
                        if self.icon_name in files:
                            self.download_data_from_server(self.icon_name, f"{self.cache_path}{game_id}.png",)
                        diff_titles = (
                            []
                        ) 

                        try:
                            tags = minidom.parse(self.game_title_file_path).getElementsByTagName("text")
                            for name in tags:
                                diff_titles.append(name.firstChild.data)
                        except Exception as e:
                                diff_titles.append("UNKNOWN TITLE")

                        game_title = ""
                        for title in diff_titles:
                            if self.game_title_file in files:
                                game_title = title
                                self.game_ids[game_id]["title"] = game_title
                            else:
                                game_title = "Unknown"
                                self.game_ids[game_id]["title"] = game_title
                                break
                            english = True

                            for char in title:
                                if char not in self.Eng:
                                    english = False
                                    break

                            if english:
                                game_title = title
                                self.game_ids[game_id]["title"] = game_title
                                break

                    percentage += GameWeightInFraction
                    self.CacheBar.setProperty("value", str(percentage)[: str(percentage).index(".")])

            self.set_game_ids(self.game_ids)
            self.set_cache()

            try:
                self.render_window()
            except Exception as e:
                print(str(e))
        except Exception as e:
            self.logs(str(e), "Error")
            self.change_colors(False)
            self.ui.setupUi(self.window)
            self.ui.alert(f"_DEV|{str(e)}")
            self.window.show()

    def render_window(self):
        self.window = QtWidgets.QWidget()

        if self.selected_mode != "avatars":
            self.ui = Icons.Ui()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.ui = Avatars.Ui()
            self.ui.setupUi(self.window, self.userID, self.ip, self.port, self.w, self.h)
            self.window.show()
