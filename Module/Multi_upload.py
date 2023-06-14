"""
    Class to handle uploading of multiple baked icons
"""

from environment import Common
import Common.Uploader as Uploader


class Main(Common):
    
    def __init__(self) -> None:
        super().__init__()
        self.uploader = Uploader()


    def upload_baked_icons(self, state_widget, group_path):
        state_widget.setText("Uploading...")
        print(group_path)
    
        
    def get_icon_group(self):
        self.GroupName