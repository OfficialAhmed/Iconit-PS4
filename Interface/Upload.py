from PyQt5 import QtCore, QtGui, QtWidgets

import Interface.Alerts as Alerts
from Module.Upload import Main as Upload

class Ui(Upload):
    def setupUi(
        self,
        upload_window,
        changeIconPath,
        CUSA,
        ConfirmType,
        exGames,
        CurrentUser=None,
        changeBgPath=None,
        modeSelected="",
        sysIconsAlgo=False
    ):
        upload_window.setObjectName("ConfirmWindow")
        upload_window.resize(378, 229)
        upload_window.setMinimumSize(QtCore.QSize(500, 500))
        upload_window.setMaximumSize(QtCore.QSize(500, 500))

        self.exGames = exGames
        self.CurrentUser = CurrentUser
        self.ConfirmType = ConfirmType
        self.Current_CUSA = CUSA
        self.changeIconPath = changeIconPath
        self.changeBgPath = changeBgPath
        self.modeSelected = modeSelected
        self.sysIconsAlgo = sysIconsAlgo

        self.window = QtWidgets.QDialog()
        self.ui = Alerts.Ui()

        self.centralwidget = QtWidgets.QWidget(upload_window)
        self.centralwidget.setObjectName("ConfirmWindow")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setItalic(True)
        upload_window.setWindowIcon(
            QtGui.QIcon(self.app_root_path + "\Data\Pref\ic1.@OfficialAhmed0")
        )

        self.Yes = QtWidgets.QPushButton(upload_window)
        self.Yes.setGeometry(QtCore.QRect(155, 120, 100, 31))
        self.Yes.setFont(font)
        self.Yes.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.Yes.setObjectName("Yes")
        self.Yes.clicked.connect(self.Resize_Upload)

        self.Ok = QtWidgets.QPushButton(upload_window)
        self.Ok.setGeometry(QtCore.QRect(215, 120, 100, 31))
        self.Ok.setFont(font)
        self.Ok.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.Ok.setObjectName("Ok")

        self.No = QtWidgets.QPushButton(upload_window)
        self.No.setGeometry(QtCore.QRect(290, 120, 100, 31))
        self.No.setFont(font)
        self.No.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.No.setObjectName("No")

        self.line = QtWidgets.QFrame(upload_window)
        self.line.setGeometry(QtCore.QRect(10, 160, 480, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.CheckingBar = QtWidgets.QProgressBar(upload_window)
        self.CheckingBar.setGeometry(QtCore.QRect(220, 250, 170, 40))
        self.CheckingBar.setProperty("value", 0)
        self.CheckingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CheckingBar.setTextVisible(True)
        self.CheckingBar.setOrientation(QtCore.Qt.Horizontal)
        self.CheckingBar.setInvertedAppearance(False)
        self.CheckingBar.setObjectName("CheckingBar")
        self.ResizingBar = QtWidgets.QProgressBar(upload_window)
        self.ResizingBar.setGeometry(QtCore.QRect(220, 350, 170, 40))
        self.ResizingBar.setProperty("value", 0)
        self.ResizingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.ResizingBar.setTextVisible(True)
        self.ResizingBar.setObjectName("ResizingBar")
        self.UploadingBar = QtWidgets.QProgressBar(upload_window)
        self.UploadingBar.setGeometry(QtCore.QRect(220, 430, 170, 40))
        self.UploadingBar.setProperty("value", 0)
        self.UploadingBar.setAlignment(QtCore.Qt.AlignCenter)
        self.UploadingBar.setTextVisible(True)
        self.UploadingBar.setObjectName("UploadingBar")
        self.graphicsView = QtWidgets.QGraphicsView(upload_window)
        self.graphicsView.setGeometry(QtCore.QRect(-20, -10, 700, 700))
        self.graphicsView.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.graphicsView.setObjectName("graphicsView")

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)

        self.Checking = QtWidgets.QLabel(upload_window)
        self.Checking.setGeometry(QtCore.QRect(60, 255, 111, 31))
        self.Checking.setFont(font)
        self.Checking.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Checking.setAlignment(QtCore.Qt.AlignCenter)
        self.Checking.setObjectName("Checking")

        self.Resizing_label = QtWidgets.QLabel(upload_window)
        self.Resizing_label.setGeometry(QtCore.QRect(60, 355, 111, 31))
        self.Resizing_label.setFont(font)
        self.Resizing_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Resizing_label.setObjectName("Resizing_label")

        self.Uploading_label = QtWidgets.QLabel(upload_window)
        self.Uploading_label.setGeometry(QtCore.QRect(60, 440, 111, 31))
        self.Uploading_label.setFont(font)
        self.Uploading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Uploading_label.setObjectName("Uploading_label")

        self.Statement = QtWidgets.QLabel(upload_window)
        self.Statement.setGeometry(QtCore.QRect(20, 50, 470, 40))
        self.Statement.setFont(font)
        self.Statement.setStyleSheet("color: rgb(255, 255, 255);")
        self.Statement.setFrameShape(QtWidgets.QFrame.Box)
        self.Statement.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Statement.setAlignment(QtCore.Qt.AlignCenter)
        self.Statement.setObjectName("Statement")
        
        self.Ok.clicked.connect(upload_window.close)
        self.No.clicked.connect(upload_window.close)

        self.graphicsView.raise_()
        self.Yes.raise_()
        self.No.raise_()
        self.line.raise_()
        self.CheckingBar.raise_()
        self.ResizingBar.raise_()
        self.UploadingBar.raise_()
        self.Checking.raise_()
        self.Resizing_label.raise_()
        self.Uploading_label.raise_()
        self.Statement.raise_()
        self.retranslateUi(upload_window)
        QtCore.QMetaObject.connectSlotsByName(upload_window)

    def retranslateUi(self, ConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfirmWindow.setWindowTitle(_translate("ConfirmWindow", "Confirm"))
        self.Yes.setText(_translate("ConfirmWindow", "Yes"))
        self.Ok.setText(_translate("ConfirmWindow", "Ok"))
        self.No.setText(_translate("ConfirmWindow", "No"))
        self.Checking.setText(_translate("ConfirmWindow", "Validation"))
        self.Resizing_label.setText(_translate("ConfirmWindow", "Convertion"))
        self.Uploading_label.setText(_translate("ConfirmWindow", "Sending"))

        styleTagStart = '<p align="center" style="margin: 0px; -qt-block-indent:0; text-indent:0px;"><span style="font-size:10pt; '
        styleTagEnd = "</span></p>\n"
        warning_message = f'{styleTagStart} color:#e83c3c">ATTENTION! This will overwrite the backup icon stored in (My backup). {styleTagEnd}\n"Are sure you want to change the icon?"'
        
        self.Statement.setText(
            _translate("ConfirmWindow", warning_message)
        )
