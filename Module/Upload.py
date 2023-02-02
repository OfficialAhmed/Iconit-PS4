
from environment import Common
import Interface.Alerts as Alerts

from PIL import Image
from PyQt5 import QtWidgets
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
        """ 
            A method could solve the need of an external program installation to convert png to dds 
            * Check on PS4 * 
        """
    
        subprocess.run(
            ["Data\\BIN\\texconv", "-f", "BC1_UNORM", input_dir, "-o", output_dir, "-y"]
        )


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


    def resize_upload(self):
        try:
            from time import perf_counter
            starting_time = time.perf_counter()

            self.image = None

            self.Yes.setEnabled(False)
            self.No.setEnabled(False)
            self.CheckingBar.setProperty("value", 10)
            img_dir = self.temp_path + "Icons\\"

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
                    IconName = [iconFound]

                    if "icon0_4k.png" in files_inside:
                        iconFound = "icon0_4k.png"
                        IconName.append(iconFound)
                        found_4k = True

                    self.CheckingBar.setProperty("value", 45)
                    with open(self.temp_path + "Icons\\icon0.png", "wb") as file:
                        self.ftp.retrbinary("RETR " + iconFound, file.write)

                    self.backup_icon(sys=True)
                    self.CheckingBar.setProperty("value", 100)

                    if self.browsed_icon_path != "" and self.browsed_icon_path != None:
                        self.ResizingBar.setProperty("value", 10)
                        Icon = Image.open(self.browsed_icon_path)

                        if found_4k:
                            minSize = 660
                            resizeIcon = Icon.resize(
                                (minSize, minSize), PIL.Image.ANTIALIAS
                            )
                            resizeIcon.save(img_dir + "icon0_4k.png")
                            self.ResizingBar.setProperty("value", 40)

                        self.ResizingBar.setProperty("value", 75)

                        minSize = 512
                        resizeIcon = Icon.resize(
                            (minSize, minSize), PIL.Image.ANTIALIAS
                        )
                        resizeIcon.save(img_dir + "icon0.png")
                        self.ResizingBar.setProperty("value", 100)
                else:
                    IconName = []  # Icon0, Icon0_X (dds and png extension)
                    BackgroundName = []  # Pic0, Pic1 (dds and png extension)
                    self.ftp.cwd("/")
                    try:
                        if self.game_ids.get(self.current_game_id).get("location") == "External":
                            self.ftp.cwd(f"{self.ps4_internal_icons_dir}/external/{self.current_game_id}")
                        else:
                            self.ftp.cwd(f"{self.ps4_internal_icons_dir}{self.current_game_id}")
                    except Exception as e:
                        self.window = QtWidgets.QDialog()
                        self.ui = Alerts.Ui()
                        self.ui.setupUi(self.window)
                        self.ui.alert(f"Couldn't change directory file DEV|{e}")
                        self.window.show()
                        self.CheckingBar.setProperty("value", 50)

                    # Check how many icons in Game directory
                    with open(
                        self.temp_path + "files_in_dir.dat", "w+", encoding="utf8"
                    ) as files_in_dir:
                        self.ftp.retrlines("LIST", files_in_dir.write)
                    self.CheckingBar.setProperty("value", 95)

                    with open(
                        self.temp_path + "files_in_dir.dat", "r", encoding="utf8"
                    ) as files_in_dir_4_pics:
                        # v4.65 new implementation for background image feature
                        content_in_file = files_in_dir_4_pics.read()
                        self.CheckingBar.setProperty("value", 100)
                        self.ResizingBar.setProperty("value", 1)
                        if self.browsed_icon_path != "" and self.browsed_icon_path != None:
                            self.backup_icon()

                            # Icon has been changed we need to resize and prepare for upload
                            Icon = Image.open(self.browsed_icon_path)
                            resizeIcon = Icon.resize((512, 512), PIL.Image.ANTIALIAS)

                            if "icon0.png" in content_in_file:
                                resizeIcon.save(img_dir + "icon0.png")
                                IconName.append("icon0.png")

                            if "icon0.dds" in content_in_file:
                                self.png_to_dds(
                                    img_dir + "icon0.png", img_dir
                                )
                                IconName.append("icon0.dds")
                            self.ResizingBar.setProperty("value", 10)

                            img_count = 22
                            if "icon0_21.png" in content_in_file:
                                img_count = 42

                            # Limit of icons 42
                            for through_20 in range(1, img_count):
                                if 10 + through_20 <= 44:
                                    self.ResizingBar.setProperty(
                                        "value", 20 + through_20
                                    )
                                if through_20 <= 9:
                                    search_png = "icon0_0" + str(through_20) + ".png"
                                    search_dds = "icon0_0" + str(through_20) + ".dds"

                                    if search_png in content_in_file:
                                        resizeIcon.save(img_dir + search_png)
                                        IconName.append(search_png)

                                    if search_dds in content_in_file:
                                        # if png exists override it no issue, otherwise
                                        # create a png, resize it and convert it to dds
                                        resizeIcon.save(img_dir + search_png)
                                        self.png_to_dds(
                                            img_dir + search_png, img_dir
                                        )
                                        IconName.append(search_dds)
                                else:
                                    search_png = "icon0_" + str(through_20) + ".png"
                                    search_dds = "icon0_" + str(through_20) + ".dds"

                                    if search_png in content_in_file:
                                        try:
                                            resizeIcon.save(img_dir + search_png)
                                            IconName.append(search_png)
                                        except Exception as e:
                                            self.log_to_external_file(str(e), "Warning")

                                    if search_dds in content_in_file:
                                        try:
                                            self.png_to_dds(
                                                img_dir + search_png,
                                                img_dir,
                                            )
                                            IconName.append(search_dds)
                                        except Exception as e:
                                            self.log_to_external_file(str(e), "Error")
                        self.ResizingBar.setProperty("value", 45)

                        if self.browsed_bg_img_path != "" and self.browsed_bg_img_path != None:
                            
                            ###################################################################################
                            ###   Background image has been changed we need to resize and prepare for upload
                            ###################################################################################

                            Background = Image.open(self.browsed_bg_img_path)
                            resizeBackground = Background.resize(
                                (1920, 1080), PIL.Image.ANTIALIAS
                            )
                            self.ResizingBar.setProperty("value", 50)

                            # v4.65 background pic0, pic1 implementaion
                            if "pic0.png" in content_in_file:
                                resizeBackground.save(img_dir + "pic0.png")
                                BackgroundName.append("pic0.png")
                            if "pic1.png" in content_in_file:
                                resizeBackground.save(img_dir + "pic1.png")
                                BackgroundName.append("pic1.png")
                            self.ResizingBar.setProperty("value", 75)

                            if "pic0.dds" in content_in_file:
                                self.png_to_dds(img_dir + "pic0.png", img_dir)
                                BackgroundName.append("pic0.dds")
                            if "pic1.dds" in content_in_file:
                                self.png_to_dds(img_dir + "pic1.png", img_dir)
                                BackgroundName.append("pic1.dds")

                            for bg in BackgroundName:
                                with open(img_dir + str(bg), "rb") as save_file:
                                    self.ftp.storbinary(
                                        "STOR " + str(bg), save_file, 1024
                                    )

                self.ResizingBar.setProperty("value", 100)
                self.UploadingBar.setProperty("value", 1)

                ######################################################################################
                ###    v4.65 added background (pic0, pic1) implementation and minimized the code
                ######################################################################################
                try:
                    for ic in IconName:
                        # upload the icons to PS4
                        with open(img_dir + str(ic), "rb") as save_file:
                            self.ftp.storbinary("STOR " + str(ic), save_file, 1024)

                        ########################################################################
                        ###         Store icons temp for in-app preview
                        ########################################################################
                        
                        if ic == "icon0.png" or ic == "icon0.PNG":
                            shutil.move(
                                img_dir + str(ic),
                                self.temp_path
                                + "Icons\metadata\\"
                                + self.selected_mode
                                + "\\"
                                + self.current_game_id
                                + ".png",
                            )

                    self.UploadingBar.setProperty("value", 100)
                    self.msg.setStyleSheet("font: 10pt; color: rgb(5, 255, 20);")
                    self.msg.setText("Success. Icons will take time to change in both the PS4 & Iconit")
             
                except Exception as e:
                    self.log_to_external_file(str(e), "Error")

                    self.UploadingBar.setProperty("value", 5)
                    self.msg.setStyleSheet("font: 10pt; color: rgb(250, 1, 1);")
                    self.msg.setText("Sorry! PS4 has denied the signal, enable Full R/W")

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
            icons = os.listdir(img_dir)
            for i in icons:
                if i != "Do Not put any file in here" or i != "metadata":
                    try:
                        os.remove(img_dir + i)
                    except Exception as e:
                        self.log_to_external_file(str(e), "Error")
            self.resize_upload()

        except Exception as e:
            self.log_to_external_file(str(e), "Error")

        finally:
            self.set_browsed_icon_path("")
            self.set_browsed_bg_img_path("")


    def log_to_external_file(self, description:str, Type:str) -> None:
        """ Write info about the issue in an external file """
        data = lambda : f"{datetime.datetime.now()} | _DEV {Type.upper()}: {description}\n"

        try: error_file = open("Logs.txt", "a")
        except: error_file = open("Logs.txt", "w")

        error_file.write(data())