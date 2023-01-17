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
        self.icons_limit = len(self.all_icons)

    def UpdateInfo(self, CustomImgSelected=False):
        self.SubmitBtn.setDisabled(True)
        current_img_path = self.icon_path + self.icon_names[self.img_counter]

        if len(self.sysGames) == 0:
            game_title = self.game_info[self.icon_names[self.img_counter]]
        else:
            game_title = self.icons[self.icon_names[self.img_counter]]
        self.Icon.setStyleSheet("border-image: url(" + current_img_path + ");")

        self.GameTitleLabel.setText(game_title)
        self.GameIdTxt.setText(self.icon_names[self.img_counter])

        # If Custom image selected by choosing image manually
        if CustomImgSelected:
            self.TotalGamesTxt.setText(
                str(self.GameTitles.currentIndex() + 1) + "/" + str(len(self.icons))
            )
        else:
            self.TotalGamesTxt.setText(
                str(self.img_counter + 1) + "/" + str(len(self.icons))
            )

        # Check homebrew/Sys icon label
        if len(self.sysGames) > 1:
            self.HomebrewLabel.setText("System icon: Yes")

        elif self.userHB == "True":
            if "CUSA" in self.icon_names[self.img_counter]:
                self.HomebrewLabel.setText("Homebrew icon: No")
            else:
                self.HomebrewLabel.setText("Homebrew icon: Yes")

        # Change External or Internal
        if self.icon_names[self.img_counter] in self.exGames:
            self.IconLocationTxt.setText("External")
        else:
            self.IconLocationTxt.setText("Internal")

    def ChangeIconSizeLabel(self, color="white", bg_image="", size="(512, 512)"):
        self.IconSizeTxt.setText("Current Icon size" + size + "")
        if bg_image != "":
            self.IconSizeTxt.setStyleSheet(
                "background-image: url(" + bg_image + "); color:" + color
            )
        else:
            self.IconSizeTxt.setStyleSheet("color:" + color)

    def backgroundImage2Original(self):
        self.is_bg_image_changed = False  # Reset bg image
        self.ChangeIconSizeLabel()
        self.BackgroundChange()
        self.window.setStyleSheet(
            f"background-image: url({self.pref_path}/{self.background});"
        )

    def BackgroundChange(self):
        label_bg = (
            self.TitleLabel,
            self.GameIdLabel,
            self.HomebrewLabel,
            self.IconSizeLabel,
            self.TotalGamesLabel,
            self.GameTitleLabel,
            self.IconLocationLabel,
            self.GameTitles,
            self.GameTitleLabel,
            self.ChangeIconBtn,
            self.NextBtn,
            self.PreviousBtn,
            self.SelectBtn,
            self.SubmitBtn,
            self.MaskBtn,
            self.ChangeBgBtn,
            self.LogsTxt,
            self.IconSizeTxt,
            self.TotalGamesTxt,
            self.TwitterLink,
            self.PaypalLink,
        )

        # if bg image changed change labels bg to black
        style = "color:white"
        if self.is_bg_image_changed:
            style = f"background-image: url({self.pref_path}/Black.@OfficialAhmed0); color:white"

        for bg in label_bg:
            bg.setStyleSheet(style)

    def BrowseBg(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.userIPath)

        img, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose a picture to open when game launches",
            self.last_browse_path,
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg)",
            options=options,
        )

        if img:
            bg = Image.open(img)
            size = bg.size
            self.changeBgPath = ""

            StyleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px"><span style="font-size:10pt; color:#e83c3c">[Error] : '
            StyleTagEnd = "</span></p></body></html>"

            if size[0] >= 1920 and size[0] <= 2048:
                if size[1] >= 1080 and size[1] <= 2048:
                    self.SubmitBtn.setDisabled(False)
                    self.changeBgPath = img
                    self.window.setStyleSheet(f"background-image: url({img});")
                    self.is_bg_image_changed = True
                    self.BackgroundChange()
                else:
                    self.logging += (
                        StyleTagStart
                        + "Image height is too small or too large atleast (1920x1080) atmost (2048x2048)"
                        + StyleTagEnd
                    )
                    self.UpdateLogs()
            else:
                self.logging += (
                    StyleTagStart
                    + "Image width is too small or too large atleast (1920x1080) atmost (2048x2048)"
                    + StyleTagEnd
                )
                self.UpdateLogs()

    def Next(self):
        self.backgroundImage2Original()
        if self.img_counter < self.icons_limit - 1:
            self.img_counter += 1
            if self.img_counter < self.icons_limit and self.img_counter >= 0:
                self.UpdateInfo()

    def Prev(self):
        self.backgroundImage2Original()
        if self.img_counter > 0 and self.img_counter <= self.icons_limit:
            self.img_counter -= 1
            self.UpdateInfo()

    def Select(self):
        self.backgroundImage2Original()
        self.img_counter = self.GameTitles.currentIndex()
        self.UpdateInfo(CustomImgSelected=True)

    def CheckImg(self, path):
        icon = Image.open(path)
        size = icon.size
        logStyleStart = "<p align='center' style='margin:0px; -qt-block-indent:0; text-indent:0px'><span style='font-size:10pt; color:#ffaa00'>[Warning] : "
        logStyleEnd = "</span></p></body></html>"

        # check if bg image changed then change label of current size image accordingly
        if size[0] == 512 and size[1] == 512:
            if self.is_bg_image_changed == True:
                self.ChangeIconSizeLabel(
                    "#0aff14;", f"{self.pref_path}/Black.@OfficialAhmed0", str(icon.size)
                )
            else:
                self.ChangeIconSizeLabel("#0aff14;", size=str(icon.size))

        elif (
            (size[0] > 512 and size[1] > 512)
            or (size[0] == 512 and size[1] > 512)
            or (size[0] > 512 and size[1] == 512)
        ):
            if self.is_bg_image_changed == True:
                self.ChangeIconSizeLabel(
                    "#fa9600;", f"{self.pref_path}/Black.@OfficialAhmed0", str(icon.size)
                )
            else:
                self.ChangeIconSizeLabel("#fa9600;", size=str(icon.size))

            self.logging += (
                logStyleStart + "Image will be resized (Too large)" + logStyleEnd
            )
            self.UpdateLogs()
        else:
            if self.is_bg_image_changed == True:
                self.ChangeIconSizeLabel(
                    "#0aff14;", f"{self.pref_path}/Black.@OfficialAhmed0", str(icon.size)
                )
            else:
                self.ChangeIconSizeLabel("#fa0a14;", size=str(icon.size))

            self.SubmitBtn.setDisabled(True)
            self.logging += (
                logStyleStart
                + "Image cannot be used nor resized (Too Small)"
                + logStyleEnd
            )
            self.UpdateLogs()

    def BrowseIcon(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setDirectory(self.userIPath)
        self.changeIconPath = ""

        img, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose the icon to upload",
            self.last_browse_path,
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg);; icon(*.ico)",
            options=options,
        )
        if img:
            self.SubmitBtn.setDisabled(False)
            self.Icon.setStyleSheet("border-image: url(" + img + ");")
            self.CheckImg(img)
            self.changeIconPath = img
            self.last_browse_path = img

    def Mask_maker(self):
        self.SubmitBtn.setEnabled(False)
        self.window = QtWidgets.QWidget()
        self.ui = Mask.Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def Resize_Upload(self):
        if self.is_bg_image_changed == False:
            self.changeBgPath = ""

        self.SubmitBtn.setEnabled(False)
        Current_CUSA = self.icon_names[self.img_counter]
        self.windo = QtWidgets.QWidget()
        self.ui = Upload.Ui()
        self.ui.setupUi(
            self.windo,
            self.changeIconPath,
            Current_CUSA,
            "Iconit",
            self.exGames,
            None,
            self.changeBgPath,
            self.selected_mode,
            self.sysIconsAlgo,
        )
        self.windo.show()

        styleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style="font-size:10pt; '
        styleTagEnd = "</span></p>\n"
        self.logging += (
            styleTagStart
            + 'color:#55ff00;">[Success] : Auto Backup '
            + Current_CUSA
            + " success. Next time you change this icon, Iconit will overwrite it"
            + styleTagEnd
        )
        self.UpdateLogs()

    def UpdateLogs(self):
        self.LogsTxt.setHtml(
            '<p align="center" style=" margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">'
            + self.logging
            + "</span></p>\n"
        )
        self.LogsTxt.moveCursor(QtGui.QTextCursor.End)