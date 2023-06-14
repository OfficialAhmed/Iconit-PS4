"""
    Class to handle uploading of multiple baked icons
"""

import os, json
from environment import Common
import Common.Uploader as Uploader

class Main(Common):
    
    def __init__(self) -> None:
        super().__init__()
        self.uploader = Uploader.Main()
        self.icons = None


    def upload_baked_icons(self, state_widget, group_path):

        state_widget.setText("Uploading...")

        self.icons = json.load(open(group_path))
        baked_icons = os.listdir(self.baked_path)

        for icon in self.icons:

            if f"{icon}.png" in baked_icons:

                self.uploader.update_local_icon(f"{self.baked_path}{icon}.png", icon)