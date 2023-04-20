from environment import Common
import json

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

    
    def save_group(self) -> bool:
        """ Save selected titles as JSON file """
        
        group = {}
        group_title = self.group_title_input.text()

        if group_title:

            for selected_id in self.selected_ids:

                if selected_id.isChecked():
                    text = selected_id.text()
                    id = text[1:10]
                    title = text[12:]
                    group[id] = title

            with open(f"{self.groups_path}{group_title}.json", 'w+') as file:
                file.write(json.dumps(group))

            self.window.close()

            return True
        
        return False