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
        
        self.icon_current_index = 0
        self.ui = self.get_ui()
        self.ids = self.get_ids()
        self.window = self.get_window()
        self.icons_limit = len(self.ids)


    def update_info(self, is_from_dropdown_list:bool = False):
        """ Update the UI icon and labels """

        self.SendBtn.setDisabled(True)
        self.current_game_id = self.icon_names[self.icon_current_index]

        icon_path = self.mode.get(self.get_selected_mode()).get('cache path')
        current_img_path = icon_path.replace('\\', '//') + f"{self.current_game_id}.png"

        game_num = f"{self.icon_current_index+1}/{self.icons_limit}"
        if is_from_dropdown_list:
            game_num = f"{self.GameTitles.currentIndex() + 1}/{self.icons_limit}"


        if self.selected_mode == "system":
            hb = "SYSTEM ICON: YES"

        elif self.is_toggled_homebrew == "True":
            hb = "HOMEBREW ICON: NO"
            if "CUSA" not in self.current_game_id:
                hb = "HOMEBREW ICON: YES"

        else:
            hb = "HOMEBREW ICON: TURNED OFF"


        location = self.ids.get(self.current_game_id).get("location").upper()
        self.HomebrewLabel.setText(hb)
        self.TotalGamesTxt.setText(game_num)
        self.IconLocationTxt.setText(location)
        self.GameIdTxt.setText(self.current_game_id)
        self.Icon.setStyleSheet(self.html.border_image(current_img_path))
        self.GameTitleLabel.setText(self.ids.get(self.current_game_id).get("title"))


    def change_icon_size_label(self, color="white", bg_image="", size="(512, 512)"):
        """ Determine the size of an icon for the label (icon dimensions)"""

        self.IconSizeTxt.setText(f"Current Icon dimension {size}")
        if bg_image != "":
            self.IconSizeTxt.setStyleSheet(f"{self.html.bg_image(bg_image)} color:{color}")
        else:
            self.IconSizeTxt.setStyleSheet(f"color: {color};")


    def bg_image_to_original(self):
        """ Reset the background to default """

        self.is_bg_image_changed = False 
        self.change_icon_size_label()
        self.change_bg()
        self.window.setStyleSheet(self.html.bg_image(f"{self.pref_path}{self.background}"))


    def change_bg(self):
        """ Change labels background for more visible user PIC0 """

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
        """ Render window browser for user icon path input """

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.icons_path)

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
                    self.set_browsed_pic_path(img)
                    self.change_bg()
                else:
                    self.logging += self.html.internal_log_msg("error", f"[Image heigh] {err}")
            else:
                self.logging += self.html.internal_log_msg("error", f"[Image width] {err}")
            self.update_internal_logs()


    def validate_icon(self, img_path):
        """ Read and check icon dimension before proceding """

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
        self.icon_current_index += 1

        # Go back to head, if tail's been reached
        if self.icon_current_index == self.icons_limit:
            self.icon_current_index = 0

        self.bg_image_to_original()
        self.update_info()


    def previous(self):
        # Go back to Tail, if head's been reached
        if self.icon_current_index == 0:
            self.icon_current_index = self.icons_limit - 1
        else:
            self.icon_current_index -= 1

        self.bg_image_to_original()
        self.update_info()


    def select(self):
        self.bg_image_to_original()
        self.icon_current_index = self.GameTitles.currentIndex()
        self.update_info(is_from_dropdown_list=True)


    def render_browse_icon_window(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.icons_path)

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
            self.validate_icon(img)
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
            self.set_browsed_pic_path("")

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