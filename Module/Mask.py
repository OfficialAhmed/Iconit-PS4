from threading import Lock
from environment import Common

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image

import os, shutil, json, concurrent.futures

class Main(Common):

    def __init__(self) -> None:
        super().__init__()
                
        self.group_ids = {}
        self.last_browse_path = ""
        self.game_icon_location = ""
        self.mask_is_changed = False
        self.is_preview_allowed = False
        self.group_icons_is_changed = False


    def browse_icon_group(self) -> None:
        """ Get the json group chosen by the user  """

        self.group_icons_is_changed = False
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        options |= QtWidgets.QFileDialog.ReadOnly
        dialog = QFileDialog()
        dialog.setDirectory(self.groups_path)
        dialog.setOptions(options)

        group_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose a group for the mask",
            self.groups_path,
            "json(*.json)",
            options=options,
        )

        if group_path and group_path.split('/')[-2] == 'Groups':

            self.bake_state.setText("Baking mask required")
            preview = self.pref_path.replace('\\', '/')
            self.game_icon_view.setStyleSheet(f'border-image: url({preview}previewTest.@OfficialAhmed0);')
            
            self.group_icons_is_changed = True

            self.group_ids: dict = json.load(open(group_path))

        else:

            QtWidgets.QMessageBox.warning(None, "Error", f"Please select an icon-group from {self.groups_path}")

        self.validate_baking()


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
                        self.log_to_external_file("Invalid mask file", "Error")

                except Exception as e:
                    self.log_to_external_file(str(e), "Error")
                    
            else:
                self.bake_state.setText("ZIP file too large")

        self.validate_baking()


    def bake_mask(self) -> None:
        """ Apply chosen mask on JSON Group """

        def apply_mask(id, cover, mask:Image, lock):
            """ Apply mask on style according to the cover(B&W photo) """
            
            with Image.open(f"{self.temp_path}Groups\\Backup\\{id}.png").resize((512, 512)) as icon:
                mask_copy = mask.copy()
                mask_copy.paste(icon, (0, 0), cover) 
                
                # One thread writing to the system at a time
                with lock:
                    mask_copy.save(f"{self.groups_path}Baked\\{id}.png")

        try:

            # Lock for all threads before race conditions or other synchronization issues
            lock = Lock()

            with concurrent.futures.ThreadPoolExecutor() as executor:

                style = Image.open(f"{self.temp_path}mask-style.png")
                cover = Image.open(f"{self.temp_path}mask.jpg").resize((512, 512)).convert("L")
                mask = style.copy()

                tasks = [executor.submit(apply_mask, id, cover, mask, lock) for id in self.group_ids]
                
                concurrent.futures.wait(tasks)

            self.bake_progress.setValue(100)
            self.bake_state.setText(""" Done """)
            self.is_preview_allowed = True

        except Exception as e:

            self.bake_state.setText("Error baking mask, read logs.txt")
            self.log_to_external_file(str(e), "Error")
            self.is_preview_allowed = False

        finally:

            self.bake_preview_btn.setEnabled(self.is_preview_allowed)
            self.bake_quit_btn.setEnabled(self.is_preview_allowed)
            self.bake_btn.setEnabled(False)


    def validate_baking(self) -> None:
        """ Enable/Disable the baking button """

        self.bake_btn.setEnabled(False)
    
        if self.group_icons_is_changed and self.mask_is_changed:
            self.bake_btn.setEnabled(True)
    

    def preview_baked_mask(self) -> None:
        """ Render baked test icon for preview """

        if self.is_preview_allowed:

            try:
                location = "Baked"
                self.bake_view.setStyleSheet(f"border-image: url({location}/{self.last_baked_mask}.png);")

            except Exception as e:
                self.log_to_external_file(str(e), "Warning")


    def quit(self):
        exit()