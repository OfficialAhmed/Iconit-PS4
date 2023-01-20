from Module.Alerts import Main as Alerts
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui(Alerts):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, window):
        font = QtGui.QFont()
        font.setWeight(9)
        font.setPointSize(12)
        font.setFamily(self.userFont)
        
        window.resize(357, 208)
        window.setWindowTitle("Alert")
        window.setMinimumSize(QtCore.QSize(357, 208))
        window.setMaximumSize(QtCore.QSize(357, 208))

        self.buttonBox = QtWidgets.QDialogButtonBox(window)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 160, 261, 51))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        
        self.Message = QtWidgets.QPlainTextEdit(window)
        self.Message.setFont(font)
        self.Message.setReadOnly(True)
        self.Message.setCenterOnScroll(False)
        self.Message.setFrameShape(QtWidgets.QFrame.Box)
        self.Message.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Message.setGeometry(QtCore.QRect(3, 10, 351, 151))
        self.Message.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Message.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.buttonBox.accepted.connect(window.accept)
        self.buttonBox.rejected.connect(window.reject)
        QtCore.QMetaObject.connectSlotsByName(window)
