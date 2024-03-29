from PIL import Image
from PyQt5 import QtWidgets
from threading import Lock
from environment import Common
from Module.Multi_upload import Main as multi_uploader
from PyQt5.QtWidgets import QFileDialog

import os, shutil, concurrent.futures


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
        self.multi_uploader = multi_uploader()
        
        win_name = "MaskMakerWindow"
        self.translated_content: dict = self.translation.get_translation(self.language, win_name)
    

    def quit(self):
        exit()


    def show_mask(self) -> None:
        self.MaskView.setStyleSheet(f"border-image: url({self.mask_location}mask-style.png);")


    def show_baked_icon(self):
        path = self.temp_path.replace('\\', '/')
        self.BakedView.setStyleSheet(f"border-image: url({path}preview.png);")


    def bake_preview_icon(self) -> None:
        """ 
            Bake a temp icon for preview with chosen mask 
        """

        style = Image.open(f"{self.temp_path}mask-style.png")
        cover = Image.open(f"{self.temp_path}mask.png").convert("L")
        mask = style.copy()

        self.apply_mask("preview", cover, mask)


    def validate_baking(self) -> None:
        """ 
            Enable/Disable the baking button 
        """

        enable = False    
        if self.group_icons_is_changed and self.mask_is_changed:

            self.bake_preview_icon()
            self.show_baked_icon()
            enable = True

        self.BakeBtn.setEnabled(enable)


    def check_bake_state(self):
        """ 
            Check if all baked icons of selected group found 
        """
        
        is_found_baked = False
        try: group_ids = self.read_json(self.selected_group_path)
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
        """ 
            Get the json group chosen by the user  
        """

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
            
            self.RevertBtn.setEnabled(True)
            self.selected_group = group_path.split('/')[-1]
            self.selected_group_path = group_path

            self.check_bake_state()
            self.BakeState.setText("Baking mask required")
            self.BakedView.setStyleSheet(f'border-image: url({self.preview_icon_path}previewTest.@OfficialAhmed0);')
            
            self.group_icons_is_changed = True
            self.GroupName.setText(self.selected_group)
            self.group_ids: dict = self.read_json(group_path)

        else:
            
            self.BakedView.setStyleSheet('')
            QtWidgets.QMessageBox.warning(None, "Error", f"Please select an icon-group from {self.groups_path}")

        self.validate_baking()


    def browse_mask(self) -> None:
        """ 
            Allow Zip files to be selected through a new rendered window 
        """

        self.mask_is_changed = False
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)

        mask_location, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "CHOOSE MASK FOR THE ICONS",
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


    def revert_to_default(self):
        """
            Get selected group to `default style` from default cached icons

            * ##### User will be prompted before proceeding
        """

        translated_content: dict = self.translated_content.get("RevertToDefaultWindow")
        
        is_confirmed = self.alerts.alert(
            translated_content.get("WinTitle"),
            f"{translated_content.get('Msg1')} *{self.selected_group}* {translated_content.get('Msg2')}"
        )

        if is_confirmed:

            self.RevertBtn.setEnabled(False)
            selected_group = self.read_json(self.selected_group_path)
            
            # Copy group icons from cache to baked folder
            for id in selected_group:

                shutil.copy(
                    f"{self.mode.get(self.get_selected_mode()).get('default group path')}{id}.png", 
                    f"{self.baked_path}{id}.png"
                )

            if self.multi_uploader.generate_and_upload_icons(self.selected_group_path):
                title = "SUCCESSFULL REVERT"
                msg = f"*{self.selected_group}* has been successfully reverted to default"
            
            else:
                title = "UNSUCCESSFULL REVERT"
                msg = f"Something went wrong. Please refer to Logs.txt"

            self.alerts.alert(
                title,
                msg,
                False
            )


    def apply_mask(self, id, cover, mask:Image, lock=None):
        """ 
            - Shrink icon while keeping aspect ratio `(512, 512)`
                by pasting the icon/mask on transparent image
                - i.e. shrink size `(412, 412)` - trasparent `(100, 100)` - icon `(512, 512)`

            - Apply mask on style according to the cover(B&W photo) 
        """

        vertical_shift = 0
        horizontal_shift = 0
        width, height = self.ps4_icon_dimension
        transparent_icon = Image.new("RGBA", self.ps4_icon_dimension, (0, 0, 0, 0))

        if id == "preview":
            game_icon = Image.open(f"{self.preview_icon_path}previewTest.@OfficialAhmed0")
        else:
            game_icon = Image.open(f"{self.temp_path}Groups\\Backup\\{id}.png")

        try:
            # Reading mask specifications from JSON
            info = self.read_json(f"{self.temp_path}set.json")

            vertical_shift = int(info.get("vertical_shift"))
            horizontal_shift = int(info.get("horizontal_shift"))
            width, height = int(info.get("width")), int(info.get("height"))
        except: pass

        resized_game_icon = game_icon.resize((width, height))
        resized_game_icon_x = resized_game_icon.size[0]
        resized_game_icon_y = resized_game_icon.size[1]

        if vertical_shift or horizontal_shift:

            # Set Shift to 0 if not included in the mask 
            vertical_shift = 0 if not vertical_shift else vertical_shift
            horizontal_shift = 0 if not horizontal_shift else horizontal_shift

            position = ((horizontal_shift, vertical_shift))
        
        else:

            # Calculate the center point to center-align the shrunken icon
            center_point = ( (512 - resized_game_icon_x) // 2, (512 - resized_game_icon_y) // 2 )
            position = center_point

        transparent_icon.paste(resized_game_icon, position)
        
        mask_copy = mask.copy()
        mask_copy.paste(transparent_icon, (0, 0), cover) 
        
        if lock:
            # One thread writing to the system at a time
            with lock:
                mask_copy.save(f"{self.baked_path}{id}.png")
        
        else:
            # Preview baked 
            mask_copy.save(f"{self.temp_path}preview.png")
            

    def bake_mask(self) -> None:
        """
            #### Low-level implementation

            * Baking icon & mask concurrently using Threads
        """

        try:

            # Lock - Restrict to one thread at a time writing to memory to prevent race conditions/synchronization issues
            lock = Lock()

            with concurrent.futures.ThreadPoolExecutor() as executor:

                style = Image.open(f"{self.temp_path}mask-style.png")
                cover = Image.open(f"{self.temp_path}mask.png").convert("L")
                mask = style.copy()

                # Apply mask for all ids
                tasks = [executor.submit(self.apply_mask, id, cover, mask, lock) for id in self.group_ids]
                
                concurrent.futures.wait(tasks)

            self.BakeState.setText("DONE!")
            self.UploadBtn.setEnabled(True)

        except Exception as e:
            self.BakeState.setText("Error baking mask, read logs.txt")
            self.log_to_external_file(str(e), "Error")

        finally:
            self.BakeBtn.setEnabled(False)
