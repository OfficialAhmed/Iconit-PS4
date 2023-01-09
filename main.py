#  BUG:port caching not working
#  BUG:Remove cache from options not working
#  FIXME:settings doesnt save nor default 

import Interface.Iconit as Iconit
from environment import Common

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen_res = app.desktop().screenGeometry()
env = Common()
env.playSound(f"{env.local_path}/Data/Pref/bgm/home.@OfficialAhmed0")
env.set_screen_size(screen_res.width(), screen_res.height())

window = QtWidgets.QMainWindow()
window.show()

iconit_window = Iconit.Ui()
iconit_window.setupUi(window)


sys.exit(app.exec_())