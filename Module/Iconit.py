"""

    Methods for the main screen 'Iconit window'
    the class inherits 'Common'

"""
import string
import Interface.Icons as Icons
import Interface.Avatars as Avatars

from environment import Common

from PyQt5 import QtWidgets
from xml.dom import minidom

import os, json

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

        self.cached = ""
        self.ui = self.get_ui()
        self.window = self.get_window()
        self.selected_mode = self.get_selected_mode()
        self.pronunciation_file = self.constant.get_pronunciation_file_path()
        self.pronunciation_file_path = f"{self.temp_path}{self.pronunciation_file}"


    def refetch_shared_widgets(self) -> None:
        """ Fetch shared widgets. Cannot merge them into init function, since this class is initalized before the widgets. Call this method to fetch the widgets after init the UI """
        
        self.ip_input = self.widgets.get_ip_input()
        self.ip_label = self.widgets.get_ip_label()
        self.CacheBar = self.widgets.get_cache_bar()
        self.port_label = self.widgets.get_port_label()
        self.mode_label = self.widgets.get_mode_label()
        self.port_input = self.widgets.get_port_input()
        self.cache_label = self.widgets.get_cache_label()
        self.status_label = self.widgets.get_status_label()
        self.game_icon_radio = self.widgets.get_game_icon_radio()


    def check_ip_port(self) -> None:
        self.refetch_shared_widgets()

        try:
            self.ip = self.ip_input.text()
            self.port = self.port_input.text()
            
            self.set_ip_port(self.ip, self.port)
            self.settings.save_cache(ip = self.ip, port = self.port)

            is_valid = False
            if len(self.ip) > 8:
                for i in f"{self.ip}{self.port}":
                    if i.isalpha(): break
                else:
                    is_valid = True

            self.connect_ps4(is_valid)

        except Exception as e:
            self.log_to_external_file(str(e), "Warning")


    def change_state(self, connected: bool) -> None:
        translated_content: dict = self.translation.get_translation(self.language, "Iconit")

        labels = {
            self.ip_label: translated_content.get("IpLabel"),
            self.port_label: translated_content.get("PortLabel"),
            self.mode_label: translated_content.get("ModeLabel"),
            self.cache_label: translated_content.get("CacheLabel"),
        }

        success = self.constant.get_color("green")
        fail = self.constant.get_color("red")
        
        if connected: self.status_label.setText(self.html.span_tag(translated_content.get("StatusLabel_success"), success, 18))
        else: self.status_label.setText(self.html.span_tag(translated_content.get("StatusLabel_fail"), fail, 18))
            
        for label in labels:
            if connected: label.setText(self.html.span_tag(labels[label], success, 14))
            else: label.setText(self.html.span_tag(labels[label], fail, 14))


    def load_ignored_ids(self) -> list:
        """ get ignored cache from JSON """

        data = []
        file = self.mode.get(self.selected_mode).get("ignored file")
        try: 
            data = json.load(open(file)).get("ids")
        except: pass
        finally: return data


    def save_ignored_ids(self, ids:list) -> None:
        """ save ignored ids as JSON file """

        data = {"ids":ids}
        with open(self.mode.get(self.selected_mode).get("ignored file"), "w+") as file:
            json.dump(data, file)


    def save_cache(self) -> None:
        """ Save ids and titles locally as JSON """
        
        mode_info = self.mode.get(self.selected_mode)
        ids = mode_info.get("ids")

        if ids:
            with open(mode_info.get("cache file"), "w+", encoding="utf-8") as jsonFile:
                json.dump(ids, jsonFile)


    def get_cache(self) -> dict:
        """ Return the cached ids and titles if found """

        result = {}
        mode = self.mode.get(self.selected_mode)

        if mode:
            file = mode.get("cache file") 
            
            if os.path.isfile(file):
                try: result = json.load(open(file))
                except: pass
                
        return result
        

    def sort_ids_by_title(self):
        """ Sort by title in alphabetical order """

        ids:dict = self.mode.get(self.selected_mode).get("ids")

        match self.selected_mode:
            case "game":
                sorted_ids = dict(sorted(ids.items(), key=lambda data: data[1].get("title")))
            case "system apps":
                sorted_ids = dict(sorted(ids.items(), key=lambda data: data[1]))
                
        self.ids = sorted_ids
        self.mode.get(self.selected_mode)["ids"] = sorted_ids


    def get_title_from_server(self) -> str:
        """ 
            Grab the title of an id from pronuciation.xml file if found else its unknown 
            Worst-case O(n^2). The worst technique to fetch for titles (TOO SLOW)
        """

        title = "UNKNOWN TITLE"
        try:
            """
            ########################################################
                    Find English words from pronunciation file
            ########################################################
            """
            if self.download_data_from_server(self.pronunciation_file, self.pronunciation_file_path):
                tags = minidom.parse(self.pronunciation_file_path).getElementsByTagName("text")
                for name in tags:
                    title = name.firstChild.data
                    
                    english = True
                    for char in title:
                        if char not in self.english:
                            english = False
                            break

                    if english:
                        break

        except: pass
        finally:
            return title


    def connect_ps4(self, is_valid):
        

        if not is_valid:
            self.alerts.display("error", "invalid_ip_port")

        else:
            is_connected = False
            
            """
            ########################################################
                        Check PS4 Connection
            ########################################################
            """
            try:
                self.ftp.set_debuglevel(0)
                
                if len(self.port) < 1:
                    txt = "port is empty"
                    return
                
                self.ftp.connect(self.ip, int(self.port))
                self.ftp.login("", "")
                self.set_ftp(self.ftp)
                self.change_state(True)

                try:
                    self.ftp.cwd(self.ps4_internal_icons_dir)
                    self.ftp.cwd("/")
                    is_connected = True

                except:
                    txt = "are_you_sure"

            except TimeoutError: txt = "timeout"
            except ConnectionRefusedError: txt = "connection_refused"
            except Exception as e: txt = f"Error. DEV| {str(e)}"

            finally:

                if not is_connected:

                    self.alerts.display("error", txt)
                    self.change_state(False)

                    return

            self.status_label.setText(self.html.span_tag("Please wait...", "#f2ae30", 18))
            self.set_ui(self.ui)
            self.set_window(self.window)

            # Check selected mode
            if self.game_icon_radio.isChecked():
                self.set_selected_mode("game")
                self.selected_mode = "game"
                is_cached = Game().start_cache()
 
            elif self.SystemIconsRadio.isChecked():
                self.set_selected_mode("system apps")
                self.selected_mode = "system apps"
                is_cached = System().start_cache()
                
            else:
                self.set_selected_mode("avatar")
                self.selected_mode = "avatar"
                is_cached = Avatar().start_cache()

            self.selected_mode = self.get_selected_mode()

            if is_cached: 
                self.progress_bar(self.CacheBar, 100)
                self.render_window()
        

    def render_window(self) -> None:
        self.window = QtWidgets.QWidget()
        self.set_ui(self.ui)
        self.set_window(self.window)

        if self.selected_mode != "avatars":
            self.ui = Icons.Ui()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.ui = Avatars.Ui()
            self.ui.setupUi(self.window, self.userID, self.ip, self.port, self.w, self.h)
            self.window.show()



class Game(Main):
    """
    ########################################################
            Game icons caching technique  
    ########################################################
    """

    def __init__(self) -> None:
        super().__init__()
        self.ftp = self.get_ftp()
        self.refetch_shared_widgets()
        
        self.icon_name = "icon0.png"
        self.id_and_location = []
        self.english = f"{string.ascii_letters}{string.digits} "
        self.alphaNum = ("one",  "two",  "three", "four",  "five",  "six",  "seven", "eight", "nine", "™", "'", "!", "?")


    def fetch_game_title_from_db(self, game_id) -> bool:
        """ get game titles and ids from local json file """
        
        db = self.mode.get("game").get("database")
        respons = db.fetch_game_title(game_id)
        if respons[0] == True:
            self.ids[game_id]["title"] = respons[1]
            return True

        self.log_to_external_file(respons[1], "Wrning")
        return False


    def save_undetected_game(self, game_id):
        title = \
        "Hi this is Iconit I generated this file while I was reading the database\n" +\
        "The following game ids weren't found in the database, when caching them\n" +\
        "I decided to fetch the game from the PS4 directly, which was much slower.\n" +\
        "If you don't mind please share the game ids with @Officialahmed0\n" +\
        "so we can add them to the database.\n" +\
        "To make the caching faster for everyone. Thank you!" 

        txt = ""
        if os.path.isfile(self.undetected_games_file):
            file = open(self.undetected_games_file, "a")
            txt = f"{game_id}\n"
        else:
            file = open(self.undetected_games_file, "w")
            txt = f"{title}\n\n{game_id}\n"

        with file as f:
            f.write(txt)


    def filter_ids(self):
        """ filter out empty game folders and the homebrews """

        self.is_new_to_ignore = False
        self.is_external_found = False
        

        """
        #######################################################
                    Internal IDs validation
        #######################################################
        """
        # Fetch folder name with length 9 i.e.(CUSA12345)
        self.ftp.cwd(self.ps4_internal_icons_dir)
        internal_ids = [x for x in self.get_server_list() if len(x) == 9 or x == "external"]
        self.validate_ids(internal_ids, self.ps4_internal_icons_dir)


        """
        #######################################################
                    External IDs validation
        #######################################################
        """
        if self.is_external_found:
            
            self.ftp.cwd(f"/{self.ps4_external_icons_dir}")
            external_ids = [x for x in self.get_server_list() if len(x) == 9]
            self.validate_ids(external_ids, self.ps4_external_icons_dir)

        # End of filtering, update global ids

        self.set_ids(self.ids)

        if self.is_new_to_ignore :

            self.save_ignored_ids(self.ignored_ids)


    def validate_ids(self, ids, dir) -> None:
        """ check the ids for valid ones. invalid ids added to the ignored list for faster caching check"""

        for id in ids:

            if id == "external":

                self.is_external_found = True

            """
            #######################################################
                        Determine id location if its new
            #######################################################
            """
            # Check for new id
            if id not in self.ids and id not in self.ignored_ids and id != "external":

                self.ftp.cwd(f"/{dir}/{id}")
                game_files = self.get_server_list()
                
                # Valid id, if icon0 found
                if self.icon_name in game_files:
                    data = {"location":"Internal"}
                    if "external" in dir:
                        data = {"location":"External"}
                    
                    self.ids[id] = data
                    continue

                self.is_new_to_ignore = True
                self.ignored_ids.append(id)


    def start_cache(self) -> bool:

        try:
            self.change_state(True)
            self.ids = self.get_cache()
            self.ignored_ids = self.load_ignored_ids()

            self.filter_ids()
            
            progress = 0
            progress_weight = (100 / len(self.ids))

            is_new_game_found = False
            game_ids_with_hb = self.ids.copy()
            self.cached = os.listdir(self.mode.get("game").get("cache path"))


            for game_id in game_ids_with_hb:
                
                # Ignore homebrews
                if self.is_toggled_homebrew == "False":

                    if "CUSA" not in game_id:

                        self.ids.pop(game_id)
                        continue

                if self.ids.get(game_id).get("title") == None:
                    """
                    #######################################################
                        if the game was not found in the cache
                    #######################################################
                    """
                    is_new_game_found = True
                    game_location = self.ids.get(game_id).get("location")

                    current_directory = self.ps4_internal_icons_dir

                    if game_location == "External":
                        current_directory = self.ps4_external_icons_dir

                    self.ftp.cwd(f"/{current_directory}/{game_id}")
                    game_files = self.get_server_list()


                    """
                    #################################################################
                        Fetch title from local db, or from PS4, else UNKNOWN title
                    #################################################################
                    """
                    if not self.fetch_game_title_from_db(game_id):

                        self.save_undetected_game(game_id)
                        self.ids[game_id]["title"] = self.get_title_from_server()

                    current_id_icons = []

                    for icon in game_files:

                        if '.dds' in icon or '.png' in icon:
                        
                            if icon == self.icon_name:

                                # Download main icon
                                self.download_data_from_server(
                                    self.icon_name, 
                                    f"{self.mode.get('game').get('cache path')}{game_id}.png"
                                )
                            
                            # Cache icon name 
                            current_id_icons.append(icon)

                    self.ids[game_id]["icons"] = current_id_icons

                progress += progress_weight
                self.progress_bar(self.CacheBar, int(progress))
            
            self.set_ids(self.ids)

            if is_new_game_found:
                self.sort_ids_by_title()
                self.save_cache()

            return True

        except Exception as e:
            self.alerts.display("error", f"Error occured |_DEV {str(e)}")



class System(Main):
    """
    #######################################################
            System apps caching technique 
    #######################################################
    """

    def __init__(self) -> None:
        super().__init__()
        self.ftp = self.get_ftp()
        self.refetch_shared_widgets()
        

    def validate_ids(self, ids) -> bool:
        """ check if id valid, if not add it to the ignored list for faster caching process """
        
        is_new_id_found = False
        is_new_to_ignore = False
        ignored_ids = self.load_ignored_ids()
        
        progress = 0
        progress_weight = 100/len(ids)

        for id in ids:
            self.ftp.cwd(f"/{self.ps4_system_icons_dir}")
     
            """
            #######################################################
                    Determine if the ID is a new one
            #######################################################
            """
            if id not in self.system_apps_ids and id not in ignored_ids:
                # If sce_sys folder not found, goes to exception to ignore

                try: 
                    self.ftp.cwd(f"{id}/{self.constant.get_sce_folder_name()}")
                    app_files = self.get_server_list(list="files")

                    # if neither icon nor icon_4k was found, add to ignored ids
                    if "icon0_4k.png" in app_files: 
                        is_new_id_found = True
                        icon_name = "icon0_4k.png"
                        
                    elif "icon0.png" in app_files:
                        is_new_id_found = True
                        icon_name = "icon0.png"

                    else:
                        is_new_to_ignore = True
                        ignored_ids.append(id)
                        continue

                    # Try to get title from db, else from PS4
                    id_from_db = self.mode.get("system apps").get("database").get_id(id)
                    if id_from_db: self.system_apps_ids[id] = id_from_db
                    else: self.system_apps_ids[id] = self.get_title_from_server()

                    # Download icon from PS4
                    self.download_data_from_server(
                        icon_name, 
                        f"{self.mode.get('system apps').get('cache path')}{id}.png"
                    )

                except: 
                    is_new_to_ignore = True
                    ignored_ids.append(id)

            progress += progress_weight
            self.progress_bar(self.CacheBar, int(progress))

        if is_new_id_found: self.save_cache()
        if is_new_to_ignore: self.save_ignored_ids(ignored_ids)


    def start_cache(self) -> bool:
        """ Prepare a dict of app id as the key and the value of the title """

        try:
            self.system_apps_ids = self.get_cache()

            self.change_state(True)

            self.ftp.cwd(f"/{self.ps4_system_icons_dir}")
            app_ids_from_server = self.get_server_list(list="directories")

            self.validate_ids(app_ids_from_server)
            self.set_ids(self.system_apps_ids)
            
            return True

        except Exception as e:
            self.log_to_external_file(str(e), "Error")
            self.change_state(False)
            self.alerts.display("error", f"Error occured |_DEV {str(e)}")
            return False


class Avatar(Main):
    """
    ########################################################
        Class resposible for caching PS4 profile avatars 
        from PS4 'cache/profile' to 'Data' folder
    ########################################################
    """
    def __init__(self) -> None:
        super().__init__()

        self.sysProfileRoot = "system_data/priv/cache/profile/"
        self.ftp.cwd("/")
        self.ftp.cwd(self.sysProfileRoot)
        self.userID = []

        self.change_state(True)


    def start_cache(self) -> None:
        self.ids = self.get_cache()

        directories = []
        self.ftp.retrlines("LIST ", directories.append)

        with open(
            self.temp_path + "directories in system.dat", "w+", encoding="utf-8"
        ) as all_directories_in_system:
            for line in directories:
                all_directories_in_system.write(line + "\n")

        with open(self.temp_path + "directories in system.dat") as file:
            lines = file.readlines()
            for line in lines:
                if "0x" in line:
                    account_index = line.index("0x")
                    self.userID.append(line[account_index:-1])
