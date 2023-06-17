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
        self.group_icons_is_changed = False
        self.preview_icon_path = self.pref_path.replace('\\', '/')
        self.ps4_icon_dimension = self.constant.get_ps4_icon_size()


    def check_bake_state(self):
        """ Check if all baked icons of selected group found """
        
        is_found_baked = False
        try: group_ids = json.load(open(self.group_path))
        except: group_ids = []
        
        # Only check if group ids not empty
        if group_ids:
            
            for file in os.listdir(self.baked_path):

                if file[-4:] == '.png':

                    # at least one icon not found terminate
                    if file[:-4] not in group_ids:
                        is_found_baked = False
                        break

                    is_found_baked = True
        
        if is_found_baked:
            clr = "green"
            baking_state = "BAKED ICONS FOUND"
            
        else:
            clr = "red"
            baking_state = "BAKING REQUIRED"

        self.UploadBtn.setEnabled(is_found_baked)
        self.UploadState.setText(self.html.span_tag(baking_state, self.constant.get_color(clr), 8))


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
            self.group_path = group_path
            self.check_bake_state()
            self.BakeState.setText("Baking mask required")
            self.BakedView.setStyleSheet(f'border-image: url({self.preview_icon_path}previewTest.@OfficialAhmed0);')
            
            self.group_icons_is_changed = True
            self.GroupName.setText(group_path.split('/')[-1])
            self.group_ids: dict = json.load(open(group_path))

        else:
            
            self.BakedView.setStyleSheet('')
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

            # 120Kb size limit for ZIP archives
            if os.path.getsize(mask_location) <= 120000: 

                try:

                    # Check the unpacked zip, if compatible and contain masks 
                    shutil.unpack_archive(mask_location, self.temp_path, "zip")

                    if os.path.exists(f"{self.temp_path}\\mask-style.png"):
                        
                        img_location = self.temp_path.replace('\\', '/')
                        self.MaskName.setText(mask_location.split('/')[-1])
                        self.mask_location = img_location
                        self.mask_is_changed = True
                        self.show_mask()

                    else:
                        
                        self.BakeState.setText("Invalid mask file")
                        self.log_to_external_file("Invalid mask file", "Error")

                except Exception as e:
                    self.log_to_external_file(str(e), "Error")
                    
            else:
                self.BakeState.setText("ZIP file too large")

        else:
            self.MaskView.setStyleSheet('')

        self.validate_baking()


    def bake_mask(self) -> None:
        """ Apply chosen mask on all JSON Group """

        def apply_mask(id, cover, mask:Image, lock):
            """ Apply mask on style according to the cover(B&W photo) """
            
            with Image.open(f"{self.temp_path}Groups\\Backup\\{id}.png").resize(self.ps4_icon_dimension) as icon:
                
                mask_copy = mask.copy()
                mask_copy.paste(icon, (0, 0), cover) 
                
                # One thread writing to the system at a time
                with lock:
                    mask_copy.save(f"{self.baked_path}{id}.png")

        try:

            # Lock for all threads before race conditions or other synchronization issues
            lock = Lock()

            with concurrent.futures.ThreadPoolExecutor() as executor:

                style = Image.open(f"{self.temp_path}mask-style.png")
                cover = Image.open(f"{self.temp_path}mask.jpg").resize(self.ps4_icon_dimension).convert("L")
                mask = style.copy()

                # Apply mask for all ids
                tasks = [executor.submit(apply_mask, id, cover, mask, lock) for id in self.group_ids]
                
                concurrent.futures.wait(tasks)

            self.BakeState.setText("DONE!")
            self.UploadBtn.setEnabled(True)

        except Exception as e:

            self.BakeState.setText("Error baking mask, read logs.txt")
            self.log_to_external_file(str(e), "Error")

        finally:

            self.BakeBtn.setEnabled(False)


    def bake_preview_icon(self) -> None:
        """ Bake a temp icon for preview with chosen mask """

        style = Image.open(f"{self.temp_path}mask-style.png")
        cover = Image.open(f"{self.temp_path}mask.jpg").resize(self.ps4_icon_dimension).convert("L")
        mask = style.copy()

        with Image.open(f"{self.preview_icon_path}previewTest.@OfficialAhmed0") as icon:

            mask_copy = mask.copy()
            mask_copy.paste(icon, (0, 0), cover) 
            mask_copy.save(f"{self.temp_path}preview.png")


    def validate_baking(self) -> None:
        """ Enable/Disable the baking button """

        enable = False    
        if self.group_icons_is_changed and self.mask_is_changed:

            self.bake_preview_icon()
            self.show_baked_icon()
            enable = True

        self.BakeBtn.setEnabled(enable)


    def show_mask(self) -> None:
        self.MaskView.setStyleSheet(f"border-image: url({self.mask_location}mask-style.png);")


    def show_baked_icon(self):
        path = self.temp_path.replace('\\', '/')
        self.BakedView.setStyleSheet(f"border-image: url({path}preview.png);")


    def quit(self):
        exit()