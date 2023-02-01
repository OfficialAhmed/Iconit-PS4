"""

    Methods for changing icons the class inherits the 'Environment'

"""

from environment import Common

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtGui
from PIL import Image

import Interface.Upload as Upload
import Interface.Mask as Mask

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

        # setStyleSheet Url works only with forward slash (/)
        self.pref_path = self.pref_path.replace("\\", "/")
        
        self.img_counter = 0
        self.game_ids = self.get_all_game_ids()
        self.icons_limit = len(self.game_ids)
        self.ui = self.get_ui()
        self.window = self.get_window()


    def update_info(self, is_from_dropdown_list:bool = False):
        self.SendBtn.setDisabled(True)
        self.current_game_id = self.icon_names[self.img_counter]
        current_img_path = f"{self.icon_path}{self.current_game_id}"
        game_title = self.game_ids.get(self.current_game_id).get("title")

        game_num = f"{self.img_counter+1}/{self.icons_limit}"
        if is_from_dropdown_list:
            game_num = f"{self.GameTitles.currentIndex() + 1}/{self.icons_limit}"

        loc = self.game_ids.get(self.current_game_id).get("location").upper()

        if len(self.sys_game_ids) > 1:
            hb = "SYSTEM ICON: YES"

        elif self.cached_toggled_homebrew == "True":
            if "CUSA" in self.current_game_id:
                hb = "HOMEBREW ICON: NO"
            else:
                hb = "HOMEBREW ICON: YES"
        else:
            hb = "HOMEBREW ICON: TURNED OFF"

        self.HomebrewLabel.setText(hb)
        self.IconLocationTxt.setText(loc)
        self.TotalGamesTxt.setText(game_num)
        self.GameTitleLabel.setText(game_title)
        self.GameIdTxt.setText(self.current_game_id)
        self.Icon.setStyleSheet(self.html.border_image(current_img_path))


    def change_icon_size_label(self, color="white", bg_image="", size="(512, 512)"):
        self.IconSizeTxt.setText(f"Current Icon dimension {size}")
        if bg_image != "":
            self.IconSizeTxt.setStyleSheet(f"{self.html.bg_image(bg_image)} color:{color}")
        else:
            self.IconSizeTxt.setStyleSheet(f"color: {color};")


    def bg_image_to_original(self):
        self.is_bg_image_changed = False  # Reset bg image
        self.change_icon_size_label()
        self.change_bg()
        self.window.setStyleSheet(self.html.bg_image(f"{self.pref_path}{self.background}"))


    def change_bg(self):
        label_bg = (
            self.NextBtn,
            self.MaskBtn,
            self.LogsTxt,
            self.SelectBtn,
            self.SendBtn,
            self.GameIdTxt,
            self.GameTitles,
            self.TitleLabel,
            self.PaypalLink,
            self.GameIdLabel,
            self.PreviousBtn,
            self.ChangeBgBtn,
            self.TwitterLink,
            self.IconSizeTxt,
            self.ChangeIconBtn,
            self.TotalGamesTxt,
            self.HomebrewLabel,
            self.IconSizeLabel,
            self.GameTitleLabel,
            self.TotalGamesLabel,
            self.IconLocationTxt,
            self.IconLocationLabel,
        )

        style = "color:white"
        if self.is_bg_image_changed:
            path = f"{self.pref_path}Black.@OfficialAhmed0"
            style = f"{self.html.bg_image(path)} {style}"

        for bg in label_bg:
            bg.setStyleSheet(style)


    def get_image_browser(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.cached_icons_path)

        img, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose a picture to open when game launches",
            self.last_browse_path,
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg)",
            options=options,
        )

        if img:
            size = Image.open(img).size
            self.browsed_bg_img_path = ""
            err = "is too small or too large atleast (1920x1080) atmost (2048x2048)"
            
            if size[0] >= 1920 and size[0] <= 2048:
                if size[1] >= 1080 and size[1] <= 2048:
                    self.SendBtn.setDisabled(False)
                    self.window.setStyleSheet(self.html.bg_image(img))
                    self.is_bg_image_changed = True
                    self.browsed_bg_img_path = img
                    self.set_browsed_bg_img_path(img)
                    self.change_bg()
                else:
                    self.logging += self.html.internal_log_msg("error", f"[Image heigh] {err}")
            else:
                self.logging += self.html.internal_log_msg("error", f"[Image width] {err}")
            self.update_internal_logs()


    def is_img_valid(self, img_path):
        required_dimension = self.constant.PS4_ICON_SIZE
        img_size = Image.open(img_path).size
        background = f"{self.pref_path}Black.@OfficialAhmed0"

        if img_size == required_dimension:
            if not self.is_bg_image_changed:
                background = ""
            self.change_icon_size_label(self.constant.get_color("green"), background, size=str(img_size))

        elif img_size[0] < required_dimension[0] or img_size[1] < required_dimension[1]:
            clr = self.constant.get_color("green")

            if not self.is_bg_image_changed:
                background = ""
                clr = self.constant.get_color("red")

            self.change_icon_size_label(clr, background, str(img_size))

            self.SendBtn.setDisabled(True)
            self.logging += self.html.internal_log_msg("error", "Image cannot be used nor resized (Too Small)")
            self.update_internal_logs()
        else:
            if not self.is_bg_image_changed:
                background = ""
            self.change_icon_size_label(self.constant.get_color("orange"), size=str(img_size))

            self.logging += self.html.internal_log_msg("warning", "Image will be resized (Too large)")
            self.update_internal_logs()


    def next(self):
        self.bg_image_to_original()
        self.img_counter += 1
        if self.img_counter == self.icons_limit:
            # Go back to head, if tail's been reached
            self.img_counter = 0
        self.update_info()


    def previous(self):
        self.bg_image_to_original()
        if self.img_counter == 0:
            # Go back to Tail, if head's been reached
            self.img_counter = self.icons_limit - 1
        else:
            self.img_counter -= 1
        self.update_info()


    def select(self):
        self.bg_image_to_original()
        self.img_counter = self.GameTitles.currentIndex()
        self.update_info(is_from_dropdown_list=True)


    def render_browse_icon_window(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.cached_icons_path)

        img, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose the icon to upload",
            self.last_browse_path,
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg);; icon(*.ico)",
            options=options,
        )
        if img:
            self.SendBtn.setDisabled(False)
            self.Icon.setStyleSheet(self.html.border_image(img))
            self.is_img_valid(img)
            self.browsed_icon_path = img
            self.last_browse_path = img

            self.set_browsed_icon_path(img)


    def render_mask_maker_window(self):
        self.SendBtn.setEnabled(False)
        self.window = QtWidgets.QWidget()
        self.ui = Mask.Ui()
        self.ui.setupUi(self.window)
        self.window.show()


    def render_upload_window(self):
        self.SendBtn.setEnabled(False)
        if self.is_bg_image_changed == False:
            self.browsed_bg_img_path = ""
            self.set_browsed_bg_img_path("")

        self.set_current_game_id(self.current_game_id)
        self.set_upload_type("Iconit")
        
        self.window = QtWidgets.QWidget()
        self.ui = Upload.Ui()
        self.ui.setupUi(self.window)
        self.window.show()

        self.logging += self.html.internal_log_msg("success", f"Auto Backup {self.current_game_id} success.")
        self.update_internal_logs()


    def update_internal_logs(self):
        """ overwrite logs with the new lines """
        self.LogsTxt.setHtml(self.logging)
        self.LogsTxt.moveCursor(QtGui.QTextCursor.End)