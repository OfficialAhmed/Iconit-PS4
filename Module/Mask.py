from environment import Common

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image

import os
import shutil
import os

class Main(Common):
    def __init__(self) -> None:
        super().__init__()
                
        self.last_browse_path = ""
        self.game_icon_location = ""
        self.mask_is_changed = False
        self.is_preview_allowed = False
        self.game_icon_is_changed = False

    def browse_game_icon(self) -> None:
        self.game_icon_is_changed = False
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)

        icon_location, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose an image for the game icon",
            self.last_browse_path,
            "PNG(*.png);; jpg(*.jpg);; Jpeg(*.jpeg)",
            options=options,
        )

        if icon_location:
            self.last_browse_path = icon_location
            icon = Image.open(icon_location)

            if icon.size[0] >= 512 and icon.size[1] >= 512:
                self.bake_state.setText("Baking mask required")
                self.game_icon_view.setStyleSheet(f"border-image: url({icon_location});")
                self.game_icon_location = icon_location
                self.game_icon_is_changed = True
            else:
                self.bake_state.setText("Game Icon is too small min(512x512)")
        self.is_baking_valid()
                
    def browse_mask(self) -> None:
        self.mask_is_changed = False
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)

        mask_location, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose a mask for the icon",
            self.last_browse_path,
            "Zip(*.zip)",
            options=options,
        )

        if mask_location:
            self.last_browse_path = mask_location

            if os.path.getsize(mask_location) <= 120000: # 120Kb size limit for ZIP archives
                try:
                    shutil.unpack_archive(mask_location, self.temp_path, "zip")
                    if os.path.exists(f"{self.temp_path}\\mask.jpg"):
                        img_location = self.temp_path.replace('\\', '/')
                        self.mask_view.setStyleSheet(f"border-image: url({img_location}mask.jpg);")
                        self.mask_location = img_location
                        self.mask_is_changed = True
                    else:
                        self.bake_state.setText("Invalid mask file")
                        self.logs("Invalid mask file", "Error")

                except Exception as e:
                    self.logs(str(e), "Error")
            else:
                self.bake_state.setText("ZIP file too large")
        self.is_baking_valid()

    def is_baking_valid(self):
        if self.game_icon_is_changed and self.mask_is_changed:
            self.bake_btn.setEnabled(True)
        else:
            self.bake_btn.setEnabled(False)

    def bake_mask(self):
        xmb_icon_size = (512, 512)
        try:
            self.bake_progress.setValue(16)
            style = Image.open(f"{self.temp_path}mask-style.png")
            self.bake_progress.setValue(32)
            icon = Image.open(self.game_icon_location).resize(xmb_icon_size)
            self.bake_progress.setValue(48)
            cover = Image.open(f"{self.temp_path}mask.jpg").resize(xmb_icon_size).convert("L")
            self.bake_progress.setValue(64)
            mask = style.copy()
            self.bake_progress.setValue(80)
            mask.paste(icon, (0, 0), cover) # Apply mask on style according to the cover(B&W photo)
            self.bake_progress.setValue(96)

            total = len(os.listdir("Baked masks"))
            self.last_baked_mask = f"baked_mask{total+1}"
            mask.save(f"Baked masks\\baked_mask{total+1}.png")

            self.bake_progress.setValue(100)
            self.bake_state.setText(
            """
            Baked icon has been saved in (Baked masks) folder
            Apply it manually
            """)
            self.is_preview_allowed = True
            
        except Exception as e:
            self.bake_state.setText("Error baking mask, read logs.txt")
            self.logs(str(e), "Error")
            self.is_preview_allowed = False

        finally:
            self.bake_preview_btn.setEnabled(self.is_preview_allowed)
            self.bake_quit_btn.setEnabled(self.is_preview_allowed)
            self.bake_btn.setEnabled(False)
    
    def preview_baked_mask(self):
        if self.is_preview_allowed:
            try:
                location = "Baked masks"
                self.bake_view.setStyleSheet(f"border-image: url({location}/{self.last_baked_mask}.png);")
            except Exception as e:
                self.logs(str(e), "Warning")

    def quit(self):
        exit()