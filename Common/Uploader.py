""" 
    Class for common methods for uploading
"""
import shutil, os
from ftplib import FTP
from environment import Common


class Main(Common):

    def __init__(self) -> None:
        super().__init__()
        
        self.ftp:FTP = self.get_ftp()
        self.game_ids:dict = self.get_ids()


    def update_local_icon(self, icon_path, game_id):
        """
            Move icon to local view path to update the iconit view screen
        """

        shutil.move(icon_path,
            f"{self.metadata_path}{self.selected_mode}\\{game_id}.png"
        )


    def png_to_dds(self, png_dir: str, output_dir: str) -> None:
        """ 
            DDS conversion with DXT1 compression using 
            Microsoft corp. (texconv) LICENSED software under MIT license
        """

        os.system(f"Data\\BIN\\texconv -f BC1_UNORM {png_dir} -o {output_dir} -y")


    def upload_to_server(self, icon_to_upload:str, icon_name:str) -> bool:
        """
            Send icon (png/dds) to PS4 through FTP 'STOR' COMMAND
            NOTE: current ftp dir should be the game folder i.e CUSAxxxxx
        """
        
        try:
            with open(icon_to_upload, "rb") as binary_data:
                self.ftp.storbinary(f"STOR {icon_name}", binary_data, 1024)
                return True
            
        except: return False