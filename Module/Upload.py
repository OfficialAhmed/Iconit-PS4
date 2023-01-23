from environment import Common
import Interface.Alerts as Alerts

from PIL import Image
from PyQt5 import QtWidgets
import time, os, shutil, PIL

class Main(Common):
    def __init__(self) -> None:
        super().__init__()
        self.is_sys_icon = self.get_is_sys_icon()
        self.current_game_id = self.get_current_game_id()
        self.browsed_icon_path = self.get_browsed_icon_path()
        self.browsed_bg_img_path = self.get_browsed_bg_img_path()

        
    def png2dds(self, input_dir, output_dir) -> None:
        """ convert legit png to dds using imageMagic lib (wand) """
        if self.image != None:
            with self.image.Image(filename=input_dir) as img:
                img.compression = "dxt1"
                img.save(filename=output_dir)

    def backup(self):
        backup = []
        try:
            backup = os.listdir(self.constant.ICONS_BACKUP_NAME)
        except:
            os.mkdir(self.constant.ICONS_BACKUP_NAME)

        if self.current_game_id + ".png" in backup:
            try:
                os.remove(self.constant.ICONS_BACKUP_NAME + "\\" + self.current_game_id + ".png")
            except Exception as e:
                self.logIt(str(e), "Error")

        try:
            shutil.copyfile(
                "Data\Cache\Icons\metadata\\"
                + self.selected_mode
                + "\\"
                + self.current_game_id
                + ".png",
                self.constant.ICONS_BACKUP_NAME+"\\" + self.current_game_id + ".png",
            )

        except Exception as e:
            self.logIt(str(e), "Error")

    def Resize_Upload(self):
        try:
            self.image = None
            try:
                from wand import image

                self.image = image

            except Exception as e:
                self.logIt(
                    str(e)
                    + " | DEV module wand cannot be found, something related to imageMagic",
                    "Warning",
                )

            self.Yes.setEnabled(False)
            self.No.setEnabled(False)
            try:
                self.ftp.connect(self.IP, int(self.Port))
                self.ftp.login("", "")
            except Exception as e:
                self.logIt(str(e), "Error")
                self.ui.setupUi(self.window, str(e))
                self.window.show()
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

                    self.ftp.cwd("/")
                    self.ftp.cwd("system_ex/app/" + self.current_game_id + "/sce_sys")
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

                    self.backup(sys=True)
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
                        if self.current_game_id in self.external_game_ids:
                            self.ftp.cwd(f"{self.ps4_internal_icons_dir}/external/{self.current_game_id}")
                        else:
                            self.ftp.cwd(self.ps4_internal_icons_dir + "/" + self.current_game_id)
                    except:
                        self.window = QtWidgets.QDialog()
                        self.ui = Alerts.Ui()
                        self.ui.setupUi(
                            self.window,
                            "Cannot find this icon in your PS4. This might be from an older caching process please delete cache and recache again, other than that you may continue but this icon wont be changed."
                        )
                        self.window.show()
                        self.CheckingBar.setProperty("value", 50)

                    # Check how many icons in Game directory
                    with open(
                        self.temp_path + "files_in_dir.dat", "w+", encoding="utf8"
                    ) as files_in_dir:
                        self.ftp.retrlines("LIST", files_in_dir.write)
                    self.CheckingBar.setProperty("value", 95)

                    # update v4.65 compatible compression type for PS4 .DDS = DXT1
                    with open(
                        self.temp_path + "files_in_dir.dat", "r", encoding="utf8"
                    ) as files_in_dir_4_pics:
                        # v4.65 new implementation for background image feature
                        content_in_file = files_in_dir_4_pics.read()
                        self.CheckingBar.setProperty("value", 100)
                        self.ResizingBar.setProperty("value", 1)
                        if self.browsed_icon_path != "" and self.browsed_icon_path != None:
                            self.backup()

                            # Icon has been changed we need to resize and prepare for upload
                            Icon = Image.open(self.browsed_icon_path)
                            resizeIcon = Icon.resize((512, 512), PIL.Image.ANTIALIAS)

                            if "icon0.png" in content_in_file:
                                resizeIcon.save(img_dir + "icon0.png")
                                IconName.append("icon0.png")

                            if "icon0.dds" in content_in_file:
                                self.png2dds(
                                    img_dir + "icon0.png", img_dir + "icon0.dds"
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
                                        self.png2dds(
                                            img_dir + search_png, img_dir + search_dds
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
                                            self.logIt(str(e), "Warning")

                                    if search_dds in content_in_file:
                                        try:
                                            self.png2dds(
                                                img_dir + search_png,
                                                img_dir + search_dds,
                                            )
                                            IconName.append(search_dds)
                                        except Exception as e:
                                            self.logIt(str(e), "Error")
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
                                self.png2dds(img_dir + "pic0.png", img_dir + "pic0.dds")
                                BackgroundName.append("pic0.dds")
                            if "pic1.dds" in content_in_file:
                                self.png2dds(img_dir + "pic1.png", img_dir + "pic1.dds")
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
                    self.logIt(str(e), "Error")

                    self.UploadingBar.setProperty("value", 5)
                    self.msg.setStyleSheet("font: 10pt; color: rgb(250, 1, 1);")
                    self.msg.setText("Sorry! PS4 has denied the signal, enable Full R/W")

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
                    self.logIt(str(e), "error")
                
                ################################################################
                ###                     Convert PNG To DDS
                ################################################################

                if os.path.isfile(
                    "C:\Program Files\ImageMagick-6.9.10-Q16\convert.exe"
                ) or os.path.isfile(
                    "C:\Program Files (x86)\ImageMagick-7.1.0-Q16\convert.exe"
                ):
                    progress = 25
                    progressed = 0

                    try:
                        for dds in required_dds:
                            # update v4.21 compatible compression type for PS4 .DDS = DXT1
                            self.png2dds(
                                self.temp_path + dds + ".png",
                                self.temp_path + dds + ".dds",
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
                        self.logIt(str(e), "Error")
                else:
                    self.ui.setupUi(self.window, "Magick image not found")
                    self.window.show()

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
                        self.logIt(str(e), "Error")
            self.Resize_Upload()

        except Exception as e:
            self.logIt(str(e), "Error")

        finally:
            self.set_browsed_icon_path("")
            self.set_browsed_bg_img_path("")

    def logIt(self, description, Type):
        import datetime

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

