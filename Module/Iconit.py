"""

    Methods for the main screen 'Iconit window'
    the class inherits 'Environment'

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

        self.file_name = "pronunciation.xml"
        self.icon_name = "icon0.png"
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

        self.modeSelected = ""
        self.cached = ""

    def open_options(self):
        self.window = QtWidgets.QDialog()
        self.ui = Settings.Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def about(self):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()
        self.ui.setupUi(self.window)
        self.ui.alert("About")
        self.window.show()

    def thanks_2(self):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()
        self.ui.setupUi(self.window)
        self.ui.alert("CUSTOMspecial_thanks")
        self.window.show()

    def remove_cache(self):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()
        cache_dir = "Data\prxUserMeta\MegaSRX\metadata\game"
        all = os.listdir(cache_dir)
        try:
            for i in all:
                os.remove(cache_dir + "\\" + i)
            self.ui.setupUi(self.window, "CUSTOMdoneRmvCache")
        except:
            self.ui.setupUi(self.window, "PermissionDenied")
        self.window.show()

    def Check_IPort(self) -> None:
        self.Status.setText(self.html.span_tag("Connecting...", "#f2ae30", 18))
        try:
            self.IP = self.IP_input.text()
            self.Port = self.Port_input.text()
            self.connection_history(mode="w")
            self.set_ip_port(self.IP, self.Port) 

            if len(self.IP) < 8:
                self.Connect_PS4(False)
            else:
                valid = True
                for i in self.IP + str(self.Port):
                    if i.isalpha():
                        valid = False
                        break
                self.Connect_PS4(valid)

        except Exception as e:
            self.logs(str(e), "Warning")

    def change_colors(self, Connected: bool) -> None:
        labels = {
            self.IP_Label: "PS4 IP",
            self.Port_Label: "PS4 Port",
            self.Change_label: "Mode",
            self.Cache_label: "Cache",
        }

        success = "rgb(92, 213, 21)"
        fail = "rgb(255, 0, 0)"
        
        if Connected:
            self.Status.setText(self.html.span_tag("Connected", success, 18))
        else:
            self.Status.setText(self.html.span_tag("Failed to connect", fail, 18))
            
        for l in labels:
            if Connected:
                l.setText(self.html.span_tag(labels[l], success, 14))
            else:
                l.setText(self.html.span_tag(labels[l], fail, 14))

    def connection_history(self, mode: str) -> None:
        ################################################################
        ###               Store IP and Port for next session
        ################################################################
        file_name = "connection_history.dat"
        if mode == "r":
            try:
                with open(f"{self.temp_path}\{file_name}", "r") as file:
                    line = file.readline().strip()
                    self.IP, self.Port = line.split(",")
                    self.IP_input.setText(self.IP)
                    self.Port_input.setText(self.Port)

            except Exception as e:
                self.logs(str(e), "Warning")
        else:
            with open(f"{self.temp_path}\{file_name}", "w+") as file:
                ip = self.IP_input.text()
                port = self.Port_input.text()
                file.write(f"{ip},{port}")

    def Connect_PS4(self, isvalid):
        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()

        if isvalid:
            """
                    Naive Approach  ;)
                Solution for one connection only (GoldHen FTP)
                *Try to connect, otherwise, try to close the connection might not been closed properly before.
                *Never close connection until we move to the next window
                *Avoid reconnceting to step back to root dir, Change dir manually (/)
            """
            
            try:
                self.ftp.set_debuglevel(0)
                self.ftp.connect(self.IP, int(self.Port))
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
                self.ui.alert(f"Cannot make connection with the given IP/Port. DEV|{str(e)}")
                self.window.show()
                return

            ##############################################
            ###       User Picked Game Icon
            ###############################################
            self.Status.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
            if self.GameIcon.isChecked():
                # v4.72 json for caching
                if os.path.isfile(self.info_json_path):
                    ReadJson = open(self.info_json_path)
                    self.Game = json.load(ReadJson)

                self.modeSelected = "game"
                self.iconDirs = [self.working_dir]
                self.ftp.cwd("/")
                self.ftp.cwd("user/appmeta")

                directories = []
                self.ftp.retrlines("LIST ", directories.append)
                for dir in directories:
                    if "external" in dir:
                        self.iconDirs.append(self.working_dir + "/external")
                        break
                self.change_colors(True)

                for dir in self.iconDirs:
                    self.ftp.cwd("/")
                    try:
                        self.ftp.cwd(dir)
                    except Exception as e:
                        self.logs(str(e), "Warning")
                    directories = []
                    self.ftp.retrlines("LIST ", directories.append)

                    game_ids = [line.split(" ")[-1] for line in directories]
                    all_Games = []

                    for game_id in game_ids:
                        if len(game_id) == len("CUSA00000"):
                            accept = True

                            """
                            If HB is on
                            check each game id for CUSA or NPXS(sys icons) only
                            """
                            if self.userHB != "True":
                                if "CUSA" not in game_id:
                                    accept = False
                                    try:
                                        self.Game.pop(game_id)
                                    except:
                                        pass

                            if accept:
                                if "external" in dir:
                                    all_Games.append(game_id)
                                    self.all_CUSA_sys.append(game_id)
                                else:
                                    all_Games.append(game_id)
                                    self.all_CUSA.append(game_id)
                self.cache_game_icon()

            ##############################################
            ###       User picked Sys icons
            ###############################################
            elif self.SystemIcon.isChecked():
                self.ftp.cwd("/")
                self.ftp.cwd(self.sys_path)

                sys_files = self.listDirs()

                self.change_colors(True)

                for sys_game in sys_files:
                    if len(sys_game) == len("CUSA00000"):
                        self.ftp.cwd(sys_game)
                        folders_inside = self.listDirs()
                        if "sce_sys" in folders_inside:
                            self.ftp.cwd("sce_sys")
                            files_inside = self.listDirs()
                            if "icon0.png" in files_inside:
                                self.all_CUSA_sys.append(sys_game)

                    self.ftp.cwd("/")
                    self.ftp.cwd(self.sys_path)

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
        self.OpenWindow("ChangeAvatar")

    def CacheSysIcon(self):

        ###############################################
        #            Sys Icons impl v4.72
        ################################################

        global all_CUSA_sys
        GameWeightInFraction = (1 / len(all_CUSA_sys)) * 100
        percentage = 0
        self.ftp.set_debuglevel(0)
        self.ftp.cwd("/")
        self.ftp.cwd(self.sys_path)

        for sysIcon in all_CUSA_sys:
            self.ftp.cwd(sysIcon + "/sce_sys")
            inside_sce_sys = self.listDirs()
            icon_2_fetch = "icon0.png"

            # fetch 4k version if found
            if "icon0_4k.png" in inside_sce_sys:
                icon_2_fetch = "icon0_4k.png"

            self.fetchData(
                icon_2_fetch,
                f"{self.temp_path}MegaSRX\metadata\\{sysIcon}.png",
            )
            if self.file_name in inside_sce_sys:
                self.fetchData(self.file_name, self.temp_path + self.file_name)

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
                            self.Game[sysIcon] = GameTitle
                        else:
                            for char in title:
                                if char not in self.Eng:
                                    english = False
                                    break
                    if english:
                        GameTitle = title
                        self.Game[sysIcon] = GameTitle
            else:
                if "NPXS" in sysIcon:
                    self.Game[sysIcon] = 'Unknown system icon "Sony didn\'t provide one :)"'
                else:
                    self.Game[sysIcon] = f"Cannot find title for {sysIcon}"

            self.ftp.cwd("/")
            self.ftp.cwd(self.sys_path)
            percentage += GameWeightInFraction
            self.CacheBar.setProperty(
                "value", str(percentage)[: str(percentage).index(".")]
            )

        try:
            self.OpenWindow("GameIcon")
        except Exception as e:
            print(str(e))

    def cache_game_icon(self):
        ################################################
        #   Internal/External HDD Game Icons
        ################################################

        try:
            self.cached = os.listdir(f"{self.temp_path}MegaSRX\metadata\\game")
            numGames = len(self.all_CUSA + self.all_CUSA_sys)
            GameWeightInFraction = (1 / numGames) * 100
            percentage = 0

            for dir in self.iconDirs:
                self.ftp.cwd("/")
                self.ftp.cwd(dir)
                counter = 0

                if "external" in dir:
                    currentDir = self.all_CUSA_sys
                else:
                    currentDir = self.all_CUSA

                for i in currentDir:
                    self.ftp.cwd(i)
                    gameId = currentDir[counter]

                    if gameId not in self.Game:
                        ######################################################
                        ###  Fetch icons only if its not it the cache => info.json
                        ###  impl. v4.72
                        ######################################################

                        files_in_dir = self.listDirs()

                        for content_in_file in files_in_dir:
                            if (
                                self.file_name in content_in_file
                                or self.icon_name in content_in_file
                            ):
                                if self.file_name in content_in_file:
                                    self.fetchData(
                                        self.file_name, self.temp_path + self.file_name
                                    )
                                if self.icon_name in content_in_file:
                                    self.fetchData(
                                        self.icon_name,
                                        f"{self.temp_path}MegaSRX\metadata\\game\\{gameId}.png",
                                    )
                                diff_titles = (
                                    []
                                )  # all different titles for current fetched game
                                try:
                                    file = minidom.parse(
                                        self.temp_path + self.file_name
                                    ).getElementsByTagName("text")

                                    for name in file:
                                        diff_titles.append(name.firstChild.data)
                                except Exception as e:
                                        diff_titles.append("UNKNOWN TITLE")

                                GameTitle = ""
                                for title in diff_titles:
                                    if self.file_name in files_in_dir:
                                        GameTitle = title
                                        self.Game[gameId] = GameTitle
                                    else:
                                        GameTitle = "Unknown"
                                        self.Game[gameId] = GameTitle
                                        break
                                    english = True

                                    for char in title:
                                        if char not in self.Eng:
                                            english = False
                                            break
                                    if english:
                                        GameTitle = title
                                        self.Game[gameId] = GameTitle
                                        break

                    # Get back to root directory
                    self.ftp.cwd("/")

                    if "external" in dir:
                        self.ftp.cwd(dir)
                    else:
                        self.ftp.cwd(self.working_dir)
                    counter += 1
                    percentage += GameWeightInFraction
                    self.CacheBar.setProperty(
                        "value", str(percentage)[: str(percentage).index(".")]
                    )
            try:
                self.OpenWindow("GameIcon")
            except Exception as e:
                print(str(e))
        except Exception as e:
            self.logs(e, "Error")
            self.change_colors(False)
            self.ui.setupUi(self.window, str(e))
            self.window.show()

    def listDirs(self):
        ######################################################
        ##     Equevalent of nlst() method
        ##     PS4 FTP doesn't support nlst             impl. v4.72
        ######################################################

        dir_with_info = []
        self.ftp.retrlines("LIST ", dir_with_info.append)

        directories = [x.split(" ")[-1] for x in dir_with_info]
        return directories

    def fetchData(self, file_name, file_path_with_extension):
        self.Status.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
        with open(
            file_path_with_extension,
            "wb",
        ) as downloaded_file:
            self.ftp.retrbinary("RETR " + file_name, downloaded_file.write)

    def OpenWindow(self, win_type):
        sorted_Games = {k: v for k, v in sorted(self.Game.items(), key=lambda item: item[1])}
        self.ftp.close()
        self.window = QtWidgets.QWidget()

        if win_type == "GameIcon":
            # store games in json for cache if not IconSys
            # if len(self.all_CUSA_sys) == 0:
            with open(
                self.info_json_path, "w+"
            ) as jsonFile:
                json.dump(sorted_Games, jsonFile)

            self.ui = Icons.Ui()
            self.ui.setupUi(
                self.window,
                sorted_Games,
                self.modeSelected,
            )
            self.window.show()
        else:
            self.ui = Avatars.Ui()
            self.ui.setupUi(self.window, self.userID, self.IP, self.Port, self.w, self.h)
            self.window.show()

