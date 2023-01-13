#  BUG:Remove cache from options not working
#  FIXME:Homebrew aren't detected

import Interface.Iconit as Iconit
from environment import Common
 
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen_res = app.desktop().screenGeometry()
env = Common()
env.play_sound(f"{env.pref_path}bgm/home.@OfficialAhmed0", True)
env.set_screen_size(screen_res.width(), screen_res.height())

window = QtWidgets.QMainWindow()
iconit_window = Iconit.Ui()
iconit_window.setupUi(window)
window.show()

sys.exit(app.exec_())