from environment import Common

class Main(Common):
    def __init__(self) -> None:
        super().__init__()

    
    def f(self):
        for i in self.all_ids:
            if i.isChecked():
                print(i.text())

        self.window.close()