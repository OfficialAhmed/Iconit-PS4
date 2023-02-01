from PyQt5 import QtCore, QtGui, QtWidgets

import Interface.Alerts as Alerts
from Module.Upload import Main as Upload

class Ui(Upload):
    def __init__(self) -> None:
        super().__init__()


    def setupUi(self, window):
        self.upload_type = self.get_upload_type()
        self.selected_mode = self.get_selected_mode()
        self.browsed_icon_path = self.get_browsed_icon_path()

        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()

        font = QtGui.QFont()
        font.setFamily(self.cached_font)
        font.setPointSize(12)
        font.setItalic(True)

        #_________________   WINDOW SPECS   _______________#
        window.resize(378, 229)
        window.setWindowTitle("Proceed sending images...")
        window.setMinimumSize(QtCore.QSize(500, 500))
        window.setMaximumSize(QtCore.QSize(500, 500))
        window.setWindowIcon(QtGui.QIcon(f"{self.pref_path}ic1.@OfficialAhmed0"))

        #_________________    BUTTONS    ________________#
        self.Yes = QtWidgets.QPushButton(window)
        self.Ok = QtWidgets.QPushButton(window)
        self.No = QtWidgets.QPushButton(window)

        btns = (self.Yes, self.Ok, self.No)
        x_axis = 155
        for inx, btn in enumerate(btns):
            if inx == 2:
                x_axis = 290
            btn.setFont(font)
            btn.setGeometry(QtCore.QRect(x_axis, 120, 100, 31))
            btn.setStyleSheet("background-color: rgb(190, 190, 190);")
            x_axis += 60

        #_________________    PROGRESS BARS    ________________#
        self.CheckingBar = QtWidgets.QProgressBar(window)
        self.ResizingBar = QtWidgets.QProgressBar(window)
        self.UploadingBar = QtWidgets.QProgressBar(window)

        bars = (self.CheckingBar, self.ResizingBar, self.UploadingBar)
        y_axis = 225
        for bar in bars:
            bar.setGeometry(QtCore.QRect(220, y_axis, 170, 40))
            bar.setTextVisible(True)
            bar.setProperty("value", 0)
            bar.setAlignment(QtCore.Qt.AlignCenter)
            bar.setOrientation(QtCore.Qt.Horizontal)
            y_axis += 100

        #_________________    LABELS    ________________#
        font.setPointSize(13)

        self.CheckingLabel = QtWidgets.QLabel(window)
        self.ResizingLabel = QtWidgets.QLabel(window)
        self.UploadingLabel = QtWidgets.QLabel(window)

        labels = (self.CheckingLabel, self.ResizingLabel, self.UploadingLabel)
        y_axis = 230
        for label in labels:
            label.setFont(font)
            label.setGeometry(QtCore.QRect(60, y_axis, 111, 31))
            label.setFrameShape(QtWidgets.QFrame.NoFrame)
            label.setStyleSheet("color: rgb(255, 255, 255);")
            label.setAlignment(QtCore.Qt.AlignCenter)
            y_axis += 100

        del labels
        del y_axis
        del bars
        del btns

        #_________________    EXTRA    ________________#
        self.msg = QtWidgets.QLabel(window)
        self.msg.setFont(font)
        self.msg.setGeometry(QtCore.QRect(20, 50, 470, 40))
        self.msg.setStyleSheet("color: rgb(255, 255, 255);")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setFrameShape(QtWidgets.QFrame.Box)
        self.msg.setFrameShadow(QtWidgets.QFrame.Plain)

        self.graphicsView = QtWidgets.QGraphicsView(window)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -10, 700, 700))
        self.graphicsView.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.line = QtWidgets.QFrame(window)
        self.line.setGeometry(QtCore.QRect(10, 160, 480, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.centralwidget = QtWidgets.QWidget(window)

        #_________________    SIGNALS    ________________#
        self.Ok.clicked.connect(window.close)
        self.No.clicked.connect(window.close)
        self.Yes.clicked.connect(self.resize_upload)

        #_________________    VISIBILITY    ________________#
        self.graphicsView.raise_()
        self.Yes.raise_()
        self.No.raise_()
        self.line.raise_()
        self.CheckingBar.raise_()
        self.ResizingBar.raise_()
        self.UploadingBar.raise_()
        self.CheckingLabel.raise_()
        self.ResizingLabel.raise_()
        self.UploadingLabel.raise_()
        self.msg.raise_()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(window)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Yes.setText(_translate("ConfirmWindow", "Yes"))
        self.Ok.setText(_translate("ConfirmWindow", "Ok"))
        self.No.setText(_translate("ConfirmWindow", "No"))
        self.CheckingLabel.setText(_translate("ConfirmWindow", "VALIDATION"))
        self.ResizingLabel.setText(_translate("ConfirmWindow", "CONVERSION"))
        self.UploadingLabel.setText(_translate("ConfirmWindow", "SEND"))
        warning_message = f"{self.html.p_tag('margin: 0px;font-size:12pt; -qt-block-indent:0; text-indent:0px; color:#e83c3c', 'ATTENTION! This will overwrite the icon on the PS4')}Are sure you want to proceed?"
        self.msg.setText(_translate("ConfirmWindow", warning_message))