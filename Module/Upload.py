
from PIL import Image
from environment import Common
from traceback import extract_stack
import os, shutil, PIL, datetime
import Common.Uploader as Uploader

class Main(Common):

    def __init__(self) -> None:
        super().__init__()
        self.ftp = self.get_ftp()
        self.game_ids: dict = self.get_ids()
        self.pics_to_upload: list = []
        self.icons_to_upload: list = []
        self.current_game_id = self.get_current_game_id()
        self.browsed_pic_path = self.get_browsed_pic_path()
        self.browsed_icon_path = self.get_browsed_icon_path()
        
        self.game_icons = []

        self.uploader = Uploader.Main()


    def start_processing(self) -> None:
        """ take the user image, resize and duplicate it according to the mode selected """

        try:
            self.image = None

            self.Yes.setEnabled(False)
            self.No.setEnabled(False)

            match self.selected_mode:
                case "system apps":
                    self.generate_system_icons()
                case "game":
                    self.generate_game_icons()
                case "avatar":
                    self.generate_avatar_icons()

            self.progress_bar(self.ConversionBar, 100)

            self.send_generated_images()
            self.remove_generated_images()

            self.progress_bar(self.SendingBar, 100)

            self.No.hide()
            self.Yes.hide()
            self.Ok.raise_()

        except ConnectionResetError:
            self.ftp = self.get_ftp()
            self.ftp.connect(self.get_ip(), self.get_port())
            self.ftp.login("", "")
            self.set_ftp(self.ftp)

        except FileNotFoundError: pass

        except Exception as e:
            self.update_message(False, "Encountered a problem while resizing icon", extract_stack(), str(e) + f"{e} : ")
        
        finally:
            self.set_browsed_pic_path("")
            self.set_browsed_icon_path("")


    def get_timestamp(self) -> str:
        """ To avoid NameExists for the backup, rename it to current time """    

        date = datetime.datetime.now()
        time = date.time()

        return f"{date.day}_{date.month}_{time.hour}_{time.minute}-{time.microsecond}"


    def backup_icon(self) -> None:
        """ Copy icon from local cache for backup """ 

        icon_name = f"{self.current_game_id}.png"
        backup_icon_name = f"{self.get_timestamp()}.png"
        icon_path = f"{self.metadata_path}{self.selected_mode}\\{icon_name}"

        try:
            shutil.copyfile(icon_path, f"{self.backup_path}{backup_icon_name}")

        except Exception as e: 
            self.log_to_external_file(f"{e} | TRACEBACK {extract_stack()}", "Error")


    def generate_system_icons(self) -> None:
        """ Resize system icons and append them into the list for the uploading method """

        self.ftp.cwd(f"/{self.ps4_system_icons_dir}{self.current_game_id}/sce_sys")
        game_files = self.get_server_list(list="files")

        icon_name = "icon0.png"
        is_icon_4k = False
        self.icons_to_upload = [icon_name]

        if "icon0_4k.png" in game_files:
            icon_name = "icon0_4k.png"
            self.icons_to_upload.append(icon_name)
            is_icon_4k = True

        with open(f"{self.temp_path}Icons\\icon0.png", "wb") as picture:
            self.ftp.retrbinary("RETR " + icon_name, picture.write)

        self.backup_icon()
        self.progress_bar(self.ValidationBar, 100)

        if self.browsed_icon_path:
            icon = Image.open(self.browsed_icon_path)

            icon.resize(self.constant.get_ps4_icon_size(), PIL.Image.ANTIALIAS)
            icon.save(self.icons_cache_path + "icon0.png")
            self.progress_bar(self.ConversionBar, 50)
            
            if is_icon_4k:
                icon.resize(self.constant.get_ps4_4k_icon_size(), PIL.Image.ANTIALIAS)
                icon.save(self.icons_cache_path + "icon0_4k.png")


    def generate_game_icons(self) -> None:
        """ Resize game icons and append them into the list for the uploading method  """

        folder = ""
        if self.game_ids.get(self.current_game_id).get("location") == "External": 
            folder = "/external/"
        game_directory = f"{self.ps4_internal_icons_dir}{folder}{self.current_game_id}"
        
        self.ftp.cwd(f"/{game_directory}")

        self.game_icons = self.game_ids.get(self.current_game_id).get("icons")
        self.progress_bar(self.ValidationBar, 100)

        if self.browsed_pic_path or self.browsed_icon_path:
            
            # Backup changed images before modification
            self.backup_icon()

            if self.browsed_icon_path:
                icon = Image.open(self.browsed_icon_path)
                resized_icon = icon.resize(self.constant.get_ps4_icon_size(), PIL.Image.ANTIALIAS)

            if self.browsed_pic_path:
                pic = Image.open(self.browsed_pic_path)
                resized_pic = pic.resize(self.constant.get_ps4_pic_size(), PIL.Image.ANTIALIAS)

            progress = 0
            progress_weight = 100 // len(self.game_icons)

            for current_image in self.game_icons:
                
                icon_cache_path = f"{self.icons_cache_path}{current_image}"
                icon_cache_path_no_extension = icon_cache_path[:-4]

                ######################################################################
                # Check Icon or Pic has changed, then generate required NO. of icons
                ######################################################################
                if ".png" in current_image:

                    if self.browsed_icon_path and "icon" in current_image:
                        resized_icon.save(icon_cache_path)

                    if self.browsed_pic_path and 'pic' in current_image:
                        resized_pic.save(icon_cache_path)

                elif ".dds" in current_image:
                    # Creat a temp .png, then convert it to .dds

                    if self.browsed_icon_path and "icon" in current_image:
                        resized_icon.save(f"{icon_cache_path_no_extension}.png")
                        self.uploader.png_to_dds(f"{icon_cache_path_no_extension}.png", self.icons_cache_path)

                    if self.browsed_pic_path and 'pic' in current_image:
                        resized_pic.save(f"{icon_cache_path_no_extension}.png")
                        self.uploader.png_to_dds(f"{icon_cache_path_no_extension}.png", self.icons_cache_path)
                
                else:
                    # ignore other extensions

                    continue
                
                if self.browsed_icon_path and "icon" in current_image:
                    self.icons_to_upload.append(current_image)

                if self.browsed_pic_path and 'pic' in current_image:
                    self.pics_to_upload.append(current_image)

                progress += progress_weight
                self.progress_bar(self.ConversionBar, progress)
                

    def generate_avatar_icons(self):
        """ Resize avatar icons and append them into the list for the uploading method  """

        # FIXME: OLD IMPLEMENTATION. TO BE FIXED IN ANOTHER UPDATE. 

        sysProfileRoot = "system_data/priv/cache/profile/"
        try:
            """
            ###############################################################
            #######          Resize Icon and make copies
            ###############################################################
            """
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

        
            """
            ################################################################
            ###                     Convert PNG To DDS
            ################################################################
            
            """
            progress = 25
            progressed = 0

    
            for dds in required_dds:
                self.uploader.png_to_dds(
                    self.temp_path + dds + ".png",
                    self.temp_path,
                )

                progressed += progress
                os.remove(self.temp_path + dds + ".png")
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
            self.log_to_external_file(f"{e} | TRACEBACK {extract_stack()}", "Error")
        
        """
        ################################################################
        ###                     Upload icons
        ################################################################
        """
        self.ftp.cwd(sysProfileRoot + "/" + self.CurrentUser)
        with open(self.temp_path + "avatar.png", "rb") as save_file:
            self.ftp.storbinary("STOR " + "avatar.png", save_file, 1024)
            
        for avatar in required_dds:
            with open(self.temp_path + avatar + ".dds", "rb") as save_file:
                self.ftp.storbinary("STOR " + avatar + ".dds", save_file, 1024)


    def send_generated_images(self) -> None:
        self.sending_progress = 0
        self.sending_progress_weight = int(100 / (len(self.icons_to_upload) + len(self.pics_to_upload)))

        if self.icons_to_upload:
            self.send_icon_to_ps4()

        if self.pics_to_upload:
            self.send_pic_to_ps4()


    def send_pic_to_ps4(self) -> None:
        """ upload generated icons to ps4 """

        for pic in self.pics_to_upload:
            self.uploader.upload_to_server(f"{self.icons_cache_path}{pic}", pic)

            self.sending_progress += self.sending_progress_weight
            self.progress_bar(self.SendingBar, self.sending_progress)


    def send_icon_to_ps4(self) -> None:
        """ send icon to ps4, upon sucess copy icon0 for app preview """

        try:
            for icon in self.icons_to_upload:
                
                if self.uploader.upload_to_server(f"{self.icons_cache_path}{icon}", icon):
                    
                    if icon == "icon0.png":
                        self.uploader.update_local_icon(f"{self.icons_cache_path}{icon}", self.current_game_id)

                    self.sending_progress += self.sending_progress_weight
                    self.progress_bar(self.SendingBar, self.sending_progress)

                else:

                    self.update_message(False, "Sorry! an issue has occured, Sending has been canceled")
                    break

            self.update_message(True, "Successful!. Icons will take some time to change on PS4")
        
        except Exception as e:
            self.update_message(False, "Sorry! PS4 has denied the signal", extract_stack(), str(e))



    def update_message(self, is_sucess:bool, msg:str, traceback_stack:list = [], dev_msg:str= "", font_size:int= 10) -> None:

        color = self.constant.get_color("green")

        if not is_sucess:

            color = self.constant.get_color("red")
            self.log_to_external_file(f"{msg} | DEV {dev_msg} | TRACEBACK {traceback_stack}", "Error")
            msg += ". Read logs.txt"
        
        self.msg.setStyleSheet(f"font: {font_size}pt; color: {color};")
        self.msg.setText(msg)


    def remove_generated_images(self) -> None:
        """ Delete temp icons generated for the server """

        for file in os.listdir(self.icons_cache_path):

            if '.' in file:
                os.remove(f"{self.icons_cache_path}{file}")
        
        self.browsed_pic_path = ""
        self.browsed_icon_path = ""

