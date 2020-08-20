from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Message(object):
    def setupUi(self, Message, MessageType):
        self.Type = MessageType
        Message.setObjectName("Message")
        Message.resize(357, 208)
        Message.setMinimumSize(QtCore.QSize(357, 208))
        Message.setMaximumSize(QtCore.QSize(357, 208))
        Message.setStyleSheet("font: 75 12pt \"Comic Sans MS\";")
        Message.setWindowIcon(QtGui.QIcon(str(os.getcwd()) + "\Data\Pref\ic1.@OfficialAhmed0"))
        self.buttonBox = QtWidgets.QDialogButtonBox(Message)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 160, 261, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.Message = QtWidgets.QPlainTextEdit(Message)
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

        self.retranslateUi(Message)
        self.buttonBox.accepted.connect(Message.accept)
        self.buttonBox.rejected.connect(Message.reject)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        if self.Type == "About":
            Message.setWindowTitle(_translate("Message", "About"))
            self.Message.setPlainText(_translate("Message", 
"                   Change Game Icons & \n             profile avatars with few clicks.\n"
"   App version 4.01 released in Aug 20, 2020 \n             if you have any reports don\'t\n"
"                   hesitate to submit them\n"
"         https://twitter.com/OfficialAhmed0\n"
"                 Thanks for using Iconit"))

        elif self.Type == "Invalid":
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(_translate("Message", 
"Invalid IP or Port (Alphabets not allowed).\n"
"\nhttps://twitter.com/OfficialAhmed0\n"
"   Thanks for using Iconit v4.01"))

        elif self.Type == "IconIssue":
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(_translate("Message", 
"Invalid IP or Port (Alphabets not allowed).\n"
"\nhttps://twitter.com/OfficialAhmed0\n"
"   Thanks for using Iconit v4.01"))

        elif self.Type == "Invalid icon size":
            Message.setWindowTitle(_translate("Message", "Too small icon ERROR"))
            self.Message.setPlainText(_translate("Message", 
"Invalid icon size 'too small'. Minimum size required (440x440).\n"
"\nhttps://twitter.com/OfficialAhmed0\n"
"   Thanks for using Iconit v4.01"))
        elif self.Type == "disconnected":
            Message.setWindowTitle(_translate("Message", "Too small icon ERROR"))
            self.Message.setPlainText(_translate("Message", 
"Disconnected from PS4. Re-enable FTP payload.\n"
"\nhttps://twitter.com/OfficialAhmed0\n"
"   Thanks for using Iconit v4.01"))

        elif self.Type == "Magick image not found":
            Message.setWindowTitle(_translate("Message", "Too small icon ERROR"))
            self.Message.setPlainText(_translate("Message", 
"ImageMagick-6.9.10 not installed in \nC:\Program Files\ImageMagick-6.9.10-Q16.\nInstall it from 'Install This' Folder\n"
"\nhttps://twitter.com/OfficialAhmed0\n"
"   Thanks for using Iconit v4.01"))

        else:
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(_translate("Message", 
"Error Type: " + self.Type + ". \n*Check Your IP and Port\n*Make sure PS4 & PC connected to same WiFi\n"
"\nhttps://twitter.com/OfficialAhmed0\n"
"   Thanks for using Iconit v4.01"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Message = QtWidgets.QDialog()
    ui = Ui_Message()
    ui.setupUi(Message)
    Message.show()
    sys.exit(app.exec_())
