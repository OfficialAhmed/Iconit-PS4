from Module.Alerts import Main as Alerts
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui(Alerts):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, current_window):
        self.ver = self.get_update_version()
        self.releaseDate = self.get_update_release_date()
        self.copyright = "\nhttps://twitter.com/OfficialAhmed0\nThanks for using Iconit"

        current_window.setObjectName("Alert")
        current_window.resize(357, 208)
        current_window.setMinimumSize(QtCore.QSize(357, 208))
        current_window.setMaximumSize(QtCore.QSize(357, 208))
        current_window.setStyleSheet('font: 75 12pt "Comic Sans MS";')

        self.buttonBox = QtWidgets.QDialogButtonBox(current_window)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 160, 261, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.Message = QtWidgets.QPlainTextEdit(current_window)
        self.Message.setGeometry(QtCore.QRect(3, 10, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setWeight(9)
        self.Message.setFont(font)
        self.Message.setFrameShape(QtWidgets.QFrame.Box)
        self.Message.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Message.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Message.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Message.setReadOnly(True)
        self.Message.setCenterOnScroll(False)
        self.Message.setObjectName("Message")

        self.retranslateUi(current_window)
        self.buttonBox.accepted.connect(current_window.accept)
        self.buttonBox.rejected.connect(current_window.reject)
        QtCore.QMetaObject.connectSlotsByName(current_window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Message", "Alert"))
