import os, json
from environment import Common

from PyQt5 import QtWidgets

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

    
    def is_default_set(self) -> bool:
        """ Check Default titles """

        if os.path.isfile(self.default_group_file):
            return True
        return False
    

    def set_default(
        self, 
        custom_group_btn_obj:QtWidgets.QPushButton,
        new_icons_number:QtWidgets.QLCDNumber
    ):
        
        try:
            with open(self.default_group_file, 'w+') as file:
                file.write(json.dumps(self.get_ids()))
                custom_group_btn_obj.setEnabled(True)
            self.calc_new_titles(custom_group_btn_obj, new_icons_number)
            
        except Exception as e:
            self.log_to_external_file('Cannot make default file', str(e))


    def calc_new_titles(
        self,
        custom_group_btn_obj:QtWidgets.QPushButton, 
        new_icons_number:QtWidgets.QLCDNumber
    ):

        total_ids = len(self.get_ids())
        total_default_ids = 0

        if self.is_default_set():

            custom_group_btn_obj.setEnabled(True)
            total_default_ids = len(json.load(open(self.default_group_file)))

        new_titles = total_ids - total_default_ids
        new_icons_number.setProperty("intValue", new_titles)