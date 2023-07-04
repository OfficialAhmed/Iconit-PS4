"""

    Methods for changing icons the class inherits the 'Environment'

"""

from environment import Common

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtGui
from PIL import Image

import Interface.Upload as Upload
import Interface.Mask as Mask
import Interface.Default_icons as Default_icons

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

        self.last_browsed_path = ""
        self.translated_content: dict = self.translation.get_translation(self.language, "Icons")
        self.translated_logs: dict = self.translated_content.get("Logs")


    def next(self) -> None:
        """ Go to next node on the list of icons """
        self.icon_current_index += 1

        # Go back to head, if tail's been reached
        if self.icon_current_index == self.icons_limit:
            self.icon_current_index = 0

        self.background_to_original()
        self.refresh_ui()


    def previous(self) -> None:
        """ Go to previous node on the list of icons """

        # Go back to Tail, if head's been reached
        if self.icon_current_index == 0:
            self.icon_current_index = self.icons_limit - 1
        else:
            self.icon_current_index -= 1

        self.background_to_original()
        self.refresh_ui()


    def select(self) -> None:
        self.background_to_original()
        self.icon_current_index = self.GameTitles.currentIndex()
        self.refresh_ui(is_from_dropdown_list=True)


    def change_dimensions_label(self, color="white", bg_image="", size="(512, 512)") -> None:
        """ Determine the size of an icon for the label (icon dimensions)"""

        self.IconSizeTxt.setText(f"{self.translated_content.get('IconSizeTxt')} {size}")
        style = f"color: {color};"  
        if bg_image != "":
            style = f"{self.html.bg_image(bg_image)} color:{color}"

        self.IconSizeTxt.setStyleSheet(style)


    def background_to_original(self) -> None:
        """ Reset the background to default """

        self.change_dimensions_label()
        self.change_label_background(is_default=True)
        self.window.setStyleSheet(self.html.bg_image(f"{self.pref_path}{self.background}"))


    def is_valid_image(self, image_type, image_path) -> bool:
        """ Read and check image dimensions before proceding """

        is_valid = False

        match image_type:
            case "icon":
                most_dimenstions = (1080, 720)
                least_dimensions = self.constant.get_ps4_icon_size()
                background = ""
                
            case "picture":
                most_dimenstions = (2040, 1920)
                least_dimensions = self.constant.get_ps4_pic_size()
                background = f"{self.pref_path}Black.@OfficialAhmed0"

        icon_dimensions = Image.open(image_path).size
        icon_x, icon_y = icon_dimensions[0], icon_dimensions[1]

        # Correct size
        if icon_dimensions == least_dimensions:
            self.change_dimensions_label(self.constant.get_color("green"), background, size=str(icon_dimensions))
            self.logging += self.html.internal_log_msg("success", self.translated_logs.get("CorrectDim"))
            is_valid = True
        
        # Less than the required [CANNOT BE RESIZED]
        elif icon_x < least_dimensions[0] or icon_y < least_dimensions[1]:
            self.change_dimensions_label(self.constant.get_color("red"), size = str(icon_dimensions))
            self.logging += self.html.internal_log_msg("error", self.translated_logs.get("SmallDim"))

        # Greater than the limit [CANNOT BE RESIZED]
        elif icon_x > most_dimenstions[0] or icon_y > most_dimenstions[1]:
            self.change_dimensions_label(self.constant.get_color("red"), size = str(icon_dimensions))
            self.logging += self.html.internal_log_msg("error", f"{self.translated_logs.get('ErrDim')} {most_dimenstions}")

        # Otherwise [CAN BE RESIZED]
        else:
            self.change_dimensions_label(self.constant.get_color("orange"), background, str(icon_dimensions))
            self.logging += self.html.internal_log_msg("warning", self.translated_logs.get('LargeDim'))
            is_valid = True

        self.update_internal_logs()
        return is_valid


    def refresh_ui(self, is_from_dropdown_list:bool = False) -> None:
        """ Update the UI icon and labels """

        # Get stored window, maybe upload window has been rendered before
        self.window = self.get_window()

        self.SendBtn.setDisabled(True)
        self.current_game_id = self.icon_names[self.icon_current_index]

        icon_path = self.mode.get(self.get_selected_mode()).get('cache path')
        current_icon_path = icon_path.replace('\\', '//') + f"{self.current_game_id}.png"

        icon_index = f"{self.icon_current_index+1}"
        if is_from_dropdown_list:
            icon_index = f"{self.GameTitles.currentIndex() + 1}"

        match self.selected_mode:

            case "game":

                if self.is_toggled_homebrew == "True":
                    hb_label = "HomebrewLabel_Y" if "CUSA" not in self.current_game_id else "HomebrewLabel_N"
                else:
                    hb_label = "HomebrewLabel_T"
                

                if self.ids.get(self.current_game_id).get("location").upper() == "INTERNAL":
                    icon_location = "In"
                else:
                    icon_location = "Ex"

                hb = self.translated_content.get(hb_label)
                location = self.translated_content.get(f"IconLocation_{icon_location}")

                self.IconLocationTxt.setText(location)
                self.GameTitleLabel.setText(self.ids.get(self.current_game_id).get("title"))


            case "system apps":
                hb = self.translated_content.get("HomebrewLabel_Sys")
                self.GameTitleLabel.setText(self.ids.get(self.current_game_id))

        self.HomebrewLabel.setText(hb)
        self.GameIdTxt.setText(self.current_game_id)
        self.TotalGamesTxt.setText(f"{icon_index}/{self.icons_limit}")
        self.Icon.setStyleSheet(self.html.border_image(current_icon_path))


    def change_icon(self):
        img = self.render_browser_window("CHOOSE AN ICON TO BE DISPLAYED ON THE XMB")

        if img:
            if self.is_valid_image("icon", img):
                self.SendBtn.setDisabled(False)
                self.Icon.setStyleSheet(self.html.border_image(img))
                self.set_browsed_icon_path(img)
            else:
                self.set_browsed_icon_path("")   


    def change_picture(self):
        img = self.render_browser_window("CHOOSE A PICTURE TO BE DISPLAYED WHEN GAME LAUNCHES")

        if img:
            self.background_to_original()
            if self.is_valid_image("picture", img):
                self.SendBtn.setDisabled(False)
                self.window.setStyleSheet(self.html.bg_image(img))
                self.change_label_background(is_default = False)
                self.set_browsed_pic_path(img)
            else:
                self.set_browsed_pic_path("") 


    def change_label_background(self, is_default:bool = True) -> None:
        """ Change labels' background for more visible user PIC0 """

        label_bg = (
            self.NextBtn,
            self.MaskBtn,
            self.LogsTxt,
            self.SendBtn,
            self.SelectBtn,
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
        if not is_default:
            path = f"{self.pref_path}Black.@OfficialAhmed0"
            style = f"{self.html.bg_image(path)} {style}"

        for bg in label_bg:
            bg.setStyleSheet(style)


    def render_mask_maker_window(self):
        self.SendBtn.setEnabled(False)
        self.window = QtWidgets.QDialog()
        self.ui = Mask.Ui()
        self.ui.setupUi(self.window)
        self.window.show()

        """ 
            overwrite the environment window, 
            to keep make Iconit window reusable
        """
        self.set_window(self.window)


    def render_set_default_icons_window(self):
        self.SendBtn.setEnabled(False)
        self.window = QtWidgets.QDialog()
        self.ui = Default_icons.Ui()
        self.ui.setupUi(self.window)
        self.window.show()
        
        self.set_window(self.window)


    def render_upload_window(self):
        self.background_to_original()
        self.SendBtn.setEnabled(False)

        self.set_current_game_id(self.current_game_id)
        
        self.window = QtWidgets.QWidget()
        self.ui = Upload.Ui()
        self.ui.setupUi(self.window)
        self.window.show()

        self.logging += self.html.internal_log_msg("success", f"{self.current_game_id} {self.translated_logs.get('BackupS')}.")
        self.update_internal_logs()


    def render_browser_window(self, window_title) -> str:
        """ Display window and return path of an object i.e. Image, Picture if user choose an object [RETURN ICON PATH]"""

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.icons_path)

        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            window_title,
            self.last_browsed_path,
            self.constant.get_icon_supported_format(),
            options=options,
        )

        return image_path


    def update_internal_logs(self):
        """ overwrite logs with the new lines """

        self.LogsTxt.setHtml(self.logging)
        self.LogsTxt.moveCursor(QtGui.QTextCursor.End)