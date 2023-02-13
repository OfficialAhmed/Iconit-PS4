
from PIL import Image
from environment import Common
from traceback import extract_stack
import time, os, shutil, PIL, datetime

class Main(Common):
    def __init__(self) -> None:
        super().__init__()
        self.ftp = self.get_ftp()
        self.game_ids = self.get_ids()
        self.pics_to_upload = None
        self.icons_to_upload = None
        self.current_game_id = self.get_current_game_id()
        self.browsed_pic_path = self.get_browsed_pic_path()
        self.browsed_icon_path = self.get_browsed_icon_path()


    def png_to_dds(self, png_dir: str, output_dir: str) -> None:
        """ 
            DDS conversion with DXT1 compression using 
            Microsoft corp. (texconv) LICENSED software under MIT license
        """

        os.system(f"Data\\BIN\\texconv -f BC1_UNORM {png_dir} -o {output_dir} -y")


    def get_timestamp(self) -> str:
        """ To avoid NameExists for the backup, rename it to current time """    

        date = datetime.datetime.now()
        time = date.time()
        return f"{date.day}_{date.month}_{time.hour}_{time.minute}-{time.microsecond}"


    def backup_icon(self):
        """ Copy icon from local cache for backup """ 

        icon_name = f"{self.current_game_id}.png"
        backup_icon_name = f"{self.get_timestamp()}.png"
        icon_path = f"{self.metadata_path}{self.selected_mode}\\{icon_name}"

        try:
            shutil.copyfile(icon_path, f"{self.backup_path}{backup_icon_name}")
        except Exception as e: 
            self.log_to_external_file(f"{e} | TRACEBACK {extract_stack()}", "Error")


    def generate_underscore_icons(self, resized_icon:Image, underscore_icons:list) -> None:
        """ if underscore icons found for the game, generate them from the resized icon """

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


    def generate_system_icons_to_upload(self):
        """ Resize system icons and append them into the list for the uploading method """

        self.CheckingBar.setProperty("value", 5)

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

        self.CheckingBar.setProperty("value", 100)

        if self.browsed_icon_path:
            self.ResizingBar.setProperty("value", 10)
            icon = Image.open(self.browsed_icon_path)

            icon.resize(self.constant.get_ps4_icon_size(), PIL.Image.ANTIALIAS)
            icon.save(self.icons_cache_path + "icon0.png")
            
            if is_icon_4k:
                icon.resize(self.constant.get_ps4_4k_icon_size(), PIL.Image.ANTIALIAS)
                icon.save(self.icons_cache_path + "icon0_4k.png")


    def generate_game_icons_to_upload(self):
        """ Resize game icons and append them into the list for the uploading method  """

        folder = ""
        if self.game_ids.get(self.current_game_id).get("location") == "External": 
            folder = "/external/"
        game_directory = f"{self.ps4_internal_icons_dir}{folder}{self.current_game_id}"
        
        self.ftp.cwd(f"/{game_directory}")
        self.game_files = self.get_server_list(list="files")

        self.CheckingBar.setProperty("value", 100)
        self.ResizingBar.setProperty("value", 1)

        if self.browsed_icon_path:
            """
            #############################################################
            ###   icon has been changed, generate the PNG & DDS
            #############################################################
            """
            self.backup_icon()

            icon = Image.open(self.browsed_icon_path)
            icon_path = f"{self.icons_cache_path}icon0.png"
            icon = icon.resize(self.constant.get_ps4_icon_size(), PIL.Image.ANTIALIAS)
            icon.save(icon_path)

            underscore_icons = []
            for picture in self.game_files:
                if "icon0_" in picture:
                    underscore_icons.append(picture)

                elif picture == "icon0.png":
                    icon.save(icon_path)

                elif picture == "icon0.dds":
                    self.png_to_dds(icon_path, self.icons_cache_path)

                else:
                    continue

                self.icons_to_upload.append(picture)

            if underscore_icons:
                self.generate_underscore_icons(icon, underscore_icons)

        if self.browsed_pic_path:
            """
            #############################################################
            ###   PIC has been changed, generate the PNG & DDS
            #############################################################
            """
            pic = Image.open(self.browsed_pic_path)
            resized_pic = pic.resize(self.constant.get_ps4_pic_size(), PIL.Image.ANTIALIAS)

            self.ResizingBar.setProperty("value", 75)

            for picture in self.game_files:
                if ".dds" in picture or ".png" in picture:
                    if picture == "pic0.png" or picture == "pic1.png":
                        resized_pic.save(f"{self.icons_cache_path}{picture}")
                        self.pics_to_upload.append(picture)

                    elif picture == "pic0.dds" or picture == "pic1.dds":
                        resized_pic.save(f"{self.icons_cache_path}{picture[:4]}.png")
                        self.png_to_dds(f"{self.icons_cache_path}{picture[:4]}.png", self.icons_cache_path)
                        self.pics_to_upload.append(picture)


    def generate_avatar_icons_to_upload(self):
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
            self.log_to_external_file(f"{e} | TRACEBACK {extract_stack()}", "Error")
        
        """
        ################################################################
        ###                     Upload icons
        ################################################################
        """
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


    def resize_icon(self):
        """ take the user image, resize and duplicate it according to the mode selected """

        try:
            self.image = None

            self.Yes.setEnabled(False)
            self.No.setEnabled(False)
            self.CheckingBar.setProperty("value", 10)

            match self.selected_mode:
                case "system apps":
                    self.generate_system_icons_to_upload()
                case "game":
                    self.generate_game_icons_to_upload()
                case "avatar":
                    self.generate_avatar_icons_to_upload()

            self.ResizingBar.setProperty("value", 100)
            self.UploadingBar.setProperty("value", 1)
            
            self.send_generated_images()
            self.remove_generated_images()

            self.UploadingBar.setProperty("value", 100)

            self.No.hide()
            self.Yes.hide()
            self.Ok.raise_()

        except FileNotFoundError: pass

        except Exception as e:
            self.update_message(False, "Encountered a problem while resizing icon", extract_stack(), str(e) + f"{e} : ")
        
        finally:
            self.set_browsed_pic_path("")
            self.set_browsed_icon_path("")


    def send_generated_images(self) -> None:
        if self.icons_to_upload:
            self.send_icon_to_ps4()

        if self.pics_to_upload:
            self.send_pic_to_ps4()


    def send_pic_to_ps4(self) -> None:
        """ upload generated icons to ps4 """
        for pic in self.pics_to_upload:
            self.upload_to_server(f"{self.icons_cache_path}{pic}", pic)


    def send_icon_to_ps4(self):
        """ send icon to ps4, upon sucess copy icon0 for app preview """
        try:
            for icon in self.icons_to_upload:
                if self.upload_to_server(f"{self.icons_cache_path}{icon}", icon):
                    if icon == "icon0.png":
                        shutil.move(f"{self.icons_cache_path}{icon}",
                            f"{self.metadata_path}{self.selected_mode}\\{self.current_game_id}.png"
                        )
                else:
                    self.update_message(False, "Sorry! an issue has occured, Sending has been canceled")
                    break

            self.UploadingBar.setProperty("value", 100)
            self.update_message(True, "Successful!. Icons will take some time to change on PS4")
        
        except Exception as e:
            self.update_message(False, "Sorry! PS4 has denied the signal", extract_stack(), str(e))


    def upload_to_server(self, file, file_name) -> bool:
        try:
            with open(file, "rb") as binary_data:
                self.ftp.storbinary(f"STOR {file_name}", binary_data, 1024)
                return True
        except:
            return False


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
            if os.path.isfile(file):
                os.remove(f"{self.icons_cache_path}{file}")