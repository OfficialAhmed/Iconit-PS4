from environment import Common
import json

class Main(Common):

    def __init__(self) -> None:
        super().__init__()

    
    def save_group(self) -> bool:
        """ 
            Save selected titles as JSON file 
        """
        
        group = {}
        group_title = self.group_title_input.text()
        
        if group_title:

            err = 'Cannot use "default" as group name'
            
            if group_title.lower() == "default" or group_title == err:

                # Avoid overwriting the default file
                self.group_title_input.setText(err)

            else:

                for checkbox in self.checkboxes:

                    if checkbox.isChecked():

                        text = checkbox.text()

                        id = text[1:10]
                        title = text[12:]

                        group[id] = title


                with open(f"{self.groups_path}{group_title}.json", 'w+') as file:
                    file.write(json.dumps(group))

                self.window.close()

                return True
            
        return False
    

    def select_all(self):

        for checkbox in self.checkboxes:
            checkbox.setChecked(True)
    
    
    def deselect_all(self):

        for checkbox in self.checkboxes:
            checkbox.setChecked(False)
