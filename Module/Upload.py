
from environment import Common
import Interface.Alerts as Alerts
import ftplib
from PIL import Image
import time, os, shutil, PIL, subprocess, datetime

class Main(Common):
    def __init__(self) -> None:
        super().__init__()
        self.ftp = self.get_ftp()
        self.upload_type = self.get_upload_type()
        self.game_ids = self.get_all_game_ids()
        self.is_sys_icon = self.get_is_sys_icon()
        self.current_game_id = self.get_current_game_id()
        self.browsed_icon_path = self.get_browsed_icon_path()
        self.browsed_bg_img_path = self.get_browsed_bg_img_path()


    def png_to_dds(self, input_dir: str, output_dir: str) -> None:
        os.system(f"Data\\BIN\\texconv -f BC1_UNORM {input_dir} -o {output_dir} -y")


    def get_timestamp(self) -> str:
        date = datetime.datetime.now()
        time = date.time()

        return f"{time.minute}_{time.hour}_{date.day}_{date.month}-{time.microsecond}"


    def backup_icon(self):
        try:
            icon_name = f"{self.current_game_id}.png"
            backup_icon_name = f"{self.get_timestamp()}.png"

        except:
            os.mkdir(self.backup_path.replace("\\", ""))

        try:
            shutil.copyfile(
                f"{self.metadata_path}{self.selected_mode}\\{icon_name}",
                f"{self.backup_path}{backup_icon_name}"
            )
        except Exception as e:
            self.log_to_external_file(str(e), "Error")


    def generate_underscore_icons(self, resized_icon:Image, underscore_icons:list) -> None:
        for x in range(1, len(underscore_icons)+1):
            if x < 10:
                search_png = f"icon0_0{x}.png"
                search_dds = f"icon0_0{x}.dds"
            else:
                search_png = f"icon0_{x}.png"
                search_dds = f"icon0_{x}.dds"

            if search_png in self.game_files:
                resized_icon.save(self.icons_cache_path + search_png)
                self.icons_to_upload.append(search_png)

            if search_dds in self.game_files:
                resized_icon.save(self.icons_cache_path + search_png)
                self.png_to_dds(self.icons_cache_path + search_png, self.icons_cache_path)
                self.icons_to_upload.append(search_dds)


    def resize_icons(self):
        try:
            from time import perf_counter
            starting_time = time.perf_counter()

            self.image = None

            self.Yes.setEnabled(False)
            self.No.setEnabled(False)
            self.CheckingBar.setProperty("value", 10)

            if self.upload_type == "Iconit":
                if self.is_sys_icon:
                    ###################################################
                    ###
                    ### Critical method needs to be accurate 100%
                    ### messing up with PS4 sys files related to sys icons
                    ### Triple check everything here
                    ###
                    ###################################################

                    self.ftp.cwd(f"{self.ps4_system_icons_dir}{self.current_game_id}/sce_sys")
                    sce_sys_dir = []
                    self.ftp.retrlines("LIST ", sce_sys_dir.append)
                    files_inside = [x.split(" ")[-1] for x in sce_sys_dir]
                    self.CheckingBar.setProperty("value", 5)

                    iconFound = "icon0.png"
                    found_4k = False
                    self.icons_to_upload = [iconFound]

                    if "icon0_4k.png" in files_inside:
                        iconFound = "icon0_4k.png"
                        self.icons_to_upload.append(iconFound)
                        found_4k = True

                    self.CheckingBar.setProperty("value", 45)
                    with open(self.temp_path + "Icons\\icon0.png", "wb") as file:
                        self.ftp.retrbinary("RETR " + iconFound, file.write)

                    self.backup_icon(sys=True)
                    self.CheckingBar.setProperty("value", 100)

                    if self.browsed_icon_path != "" and self.browsed_icon_path != None:
                        self.ResizingBar.setProperty("value", 10)
                        icon = Image.open(self.browsed_icon_path)

                        if found_4k:
                            minSize = 660
                            resized_icon = icon.resize(
                                (minSize, minSize), PIL.Image.ANTIALIAS
                            )
                            resized_icon.save(self.icons_cache_path + "icon0_4k.png")
                            self.ResizingBar.setProperty("value", 40)

                        self.ResizingBar.setProperty("value", 75)

                        minSize = 512
                        resized_icon = icon.resize(
                            (minSize, minSize), PIL.Image.ANTIALIAS
                        )
                        resized_icon.save(self.icons_cache_path + "icon0.png")
                        self.ResizingBar.setProperty("value", 100)
                else: # Game icons

                    self.icons_to_upload = []  # Icon0, Icon0_X (dds and png extension)
                    self.pics_to_upload = []  # Pic0, Pic1 (dds and png extension)
                    game_directory = f"{self.ps4_internal_icons_dir}{self.current_game_id}"

                    if self.game_ids.get(self.current_game_id).get("location") == "External":
                        game_directory = f"{self.ps4_internal_icons_dir}/external/{self.current_game_id}"
                    
                    self.ftp.cwd(f"/{game_directory}")

                    self.CheckingBar.setProperty("value", 50)

                    self.game_files = self.get_server_list(list="files")

                    self.CheckingBar.setProperty("value", 100)
                    self.ResizingBar.setProperty("value", 1)

                    if self.browsed_icon_path:
                        #############################################################
                        ###   icon has been changed, generate the PNG & DDS
                        #############################################################
                        self.backup_icon()

                        icon = Image.open(self.browsed_icon_path)
                        resized_icon = icon.resize(self.constant.PS4_ICON_SIZE, PIL.Image.ANTIALIAS)
                        resized_icon.save(f"{self.icons_cache_path}icon0.png")

                        underscore_icons = []
                        for file in self.game_files:
             
                            if "icon0_" in file:
                                underscore_icons.append(file)

                            if file == "icon0.png":
                                resized_icon.save(f"{self.icons_cache_path}icon0.png")
                                self.icons_to_upload.append("icon0.png")

                            if file == "icon0.dds":
                                self.png_to_dds(f"{self.icons_cache_path}icon0.png", self.icons_cache_path)
                                self.icons_to_upload.append("icon0.dds")

                        if underscore_icons:
                            self.generate_underscore_icons(resized_icon, underscore_icons)

                    if self.browsed_bg_img_path:
                        #############################################################
                        ###   PIC has been changed, generate the PNG & DDS
                        #############################################################

                        Background = Image.open(self.browsed_bg_img_path)
                        resizeBackground = Background.resize(self.constant.PS4_PIC_SIZE, PIL.Image.ANTIALIAS)
                        self.ResizingBar.setProperty("value", 50)

                        # v4.65 background pic0, pic1 implementaion
                        if "pic0.png" in self.game_files:
                            resizeBackground.save(self.icons_cache_path + "pic0.png")
                            self.pics_to_upload.append("pic0.png")
                        if "pic1.png" in self.game_files:
                            resizeBackground.save(self.icons_cache_path + "pic1.png")
                            self.pics_to_upload.append("pic1.png")
                        self.ResizingBar.setProperty("value", 75)

                        if "pic0.dds" in self.game_files:
                            self.png_to_dds(self.icons_cache_path + "pic0.png", self.icons_cache_path)
                            self.pics_to_upload.append("pic0.dds")
                        if "pic1.dds" in self.game_files:
                            self.png_to_dds(self.icons_cache_path + "pic1.png", self.icons_cache_path)
                            self.pics_to_upload.append("pic1.dds")

                        for bg in self.pics_to_upload:
                            with open(self.icons_cache_path + str(bg), "rb") as save_file:
                                self.ftp.storbinary("STOR " + str(bg), save_file, 1024)

                self.ResizingBar.setProperty("value", 100)
                self.UploadingBar.setProperty("value", 1)

                self.send_icon_to_ps4()

                print(f"Total time took to upload: {time.perf_counter() - starting_time} seconds")
                self.No.hide()
                self.Yes.hide()
                self.Ok.raise_()

            elif self.upload_type == "Profileit":
                sysProfileRoot = "system_data/priv/cache/profile/"
                try:
                    ###############################################################
                    #######          Resize Icon and make copies
                    ###############################################################
                    required_dds = ("avatar64", "avatar128", "avatar260", "avatar440")
                    ResizeImg = Image.open(self.browsed_icon_path)
                    avatar = ResizeImg.resize((440, 440), PIL.Image.ANTIALIAS)
                    avatar.save(self.temp_path + "avatar.png")
                    self.CheckingBar.setProperty("value", 20)
                    progress = 20
                    progressed = 60
                    for dds in required_dds:
                        if "64" in dds:
                            avatar = ResizeImg.resize((64, 64), PIL.Image.ANTIALIAS)
                            avatar.save(self.temp_path + "avatar64.png")
                            self.CheckingBar.setProperty("value", 40)
                        else:
                            s = int(dds[-3:])
                            avatar = ResizeImg.resize((s, s), PIL.Image.ANTIALIAS)
                            avatar.save(self.temp_path + "avatar" + str(s) + ".png")
                            self.CheckingBar.setProperty("value", progressed)
                            progressed += 20
                    self.CheckingBar.setProperty("value", 100)
                except Exception as e:
                    self.log_to_external_file(str(e), "error")
                
                ################################################################
                ###                     Convert PNG To DDS
                ################################################################
               
                progress = 25
                progressed = 0

                try:
                    for dds in required_dds:
                        self.png_to_dds(
                            self.temp_path + dds + ".png",
                            self.temp_path,
                        )

                        for i in range(progressed, progress):
                            self.ResizingBar.setProperty("value", i)
                            time.sleep(0.01)
                        progressed += progress
                        os.remove(self.temp_path + dds + ".png")
                    self.ResizingBar.setProperty("value", 100)
                    self.msg.setStyleSheet(
                        "font: 10pt; color: rgb(5, 255, 20);"
                    )
                    self.msg.setText(
                        "Done. Give it some time & the avatar will change."
                    )
                    self.Ok.setEnabled(False)
                    self.Ok.raise_()
                    self.No.hide()
                    self.Yes.hide()

                except Exception as e:
                    self.log_to_external_file(str(e), "Error")


                ################################################################
                ###                     Upload icons
                ################################################################
                self.ftp.cwd(sysProfileRoot + "/" + self.CurrentUser)
                progress = 20
                progressed = 20
                with open(self.temp_path + "avatar.png", "rb") as save_file:
                    self.ftp.storbinary("STOR " + "avatar.png", save_file, 1024)
                    self.UploadingBar.setProperty("value", progressed)
                for avatar in required_dds:
                    with open(self.temp_path + avatar + ".dds", "rb") as save_file:
                        self.ftp.storbinary("STOR " + avatar + ".dds", save_file, 1024)
                    for i in range(progressed, progressed + progress + 1):
                        self.UploadingBar.setProperty("value", i)
                        time.sleep(0.01)
                    progressed += progress
                self.Ok.setEnabled(True)

        except FileNotFoundError:
            pass

        except FileExistsError:
            self.icons_to_upload = os.listdir(self.icons_cache_path)
            for i in self.icons_to_upload:
                try:
                    # os.remove(self.icons_cache_path + i)
                    shutil.rm(self.icons_cache_path + i)
                except Exception as e:
                    self.log_to_external_file(str(e), "Error")
            self.resize_icons()

        except Exception as e:
            self.log_to_external_file(str(e), "Error")

        finally:
            self.set_browsed_icon_path("")
            self.set_browsed_bg_img_path("")


    def send_icon_to_ps4(self):
        try:
            ########################################################################
            ###         Send icon and move a copy for in-app preview
            ########################################################################
            for icon in self.icons_to_upload:
                if self.upload_to_server(f"{self.icons_cache_path}{icon}", icon):
                    if icon.lower() == "icon0.png":
                        shutil.move(f"{self.icons_cache_path}{icon}",
                            f"{self.metadata_path}{self.selected_mode}\\{self.current_game_id}.png"
                        )

            self.UploadingBar.setProperty("value", 100)
            self.msg.setStyleSheet("font: 10pt; color: rgb(5, 255, 20);")
            self.msg.setText("Success. Icons will take time to change in both the PS4 & Iconit")
        
        except Exception as e:
            self.log_to_external_file(str(e), "Error")

            self.UploadingBar.setProperty("value", 5)
            self.msg.setStyleSheet("font: 10pt; color: rgb(250, 1, 1);")
            self.msg.setText("Sorry! PS4 has denied the signal, enable Full R/W")


    def upload_to_server(self, file, file_name) -> bool:
        try:
            with open(file, "rb") as binary_data:
                self.ftp.storbinary(f"STOR {file_name}", binary_data, 1024)
                return True
        except ftplib.error_perm as e:
            self.log_to_external_file(str(e), "Error")
            return False


    def log_to_external_file(self, description:str, Type:str) -> None:
        """ Write info about the issue in an external file """
        data = lambda : f"{datetime.datetime.now()} | _DEV {Type.upper()}: {description}\n"

        try: error_file = open("Logs.txt", "a")
        except: error_file = open("Logs.txt", "w")

        error_file.write(data())