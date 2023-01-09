
#  BUG:port caching not working

import Interface.Iconit as Iconit
from environment import Environment
from func import playSound

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen_res = app.desktop().screenGeometry()
env = Environment()
env.set_screen_size(screen_res.width(), screen_res.height())

window = QtWidgets.QMainWindow()
window.show()

iconit_window = Iconit.Ui()
iconit_window.setupUi(window)

playSound(f"{env.local_path}/Data/Pref/bgm/home.@OfficialAhmed0")

sys.exit(app.exec_())