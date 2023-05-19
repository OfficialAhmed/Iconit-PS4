""" 
    Class for common methods for uploading
"""
from environment import Common
import os

class Main(Common):

    def __init__(self) -> None:
        super().__init__()


    def png_to_dds(self, png_dir: str, output_dir: str) -> None:
        """ 
            DDS conversion with DXT1 compression using 
            Microsoft corp. (texconv) LICENSED software under MIT license
        """

        os.system(f"Data\\BIN\\texconv -f BC1_UNORM {png_dir} -o {output_dir} -y")

