from PyQt5 import QtCore, QtGui, QtWidgets
import os
import Update


class Ui_Message(object):
    def setupUi(self, Message, MessageType):
        self.ver = Update.get_update_version()
        self.releaseDate = Update.get_update_release_date()
        self.copyright = "\nhttps://twitter.com/OfficialAhmed0\nThanks for using Iconit"

        self.Type = MessageType
        Message.setObjectName("Message")
        Message.resize(357, 208)
        Message.setMinimumSize(QtCore.QSize(357, 208))
        Message.setMaximumSize(QtCore.QSize(357, 208))
        Message.setStyleSheet('font: 75 12pt "Comic Sans MS";')
        Message.setWindowIcon(
            QtGui.QIcon(str(os.getcwd()) + "\Data\Pref\ic1.@OfficialAhmed0")
        )
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
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Iconit is an automated Windows application for jailbroken PS4 consoles to change xmb icons and profile avatars with the help of FTP payload. Do you like what you see? Please consider donating \n"
                    "\n   App version v"
                    + str(self.ver)
                    + " released in "
                    + self.releaseDate
                    + "\n"
                    "                 Thanks for using Iconit",
                )
            )
        elif self.Type == "CUSTOMspecial_thanks":
            Message.setWindowTitle(_translate("Message", "Shout-out"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Special Thanks:-\n@Lapy05575948\n\nTesters:-\n@laz305\n@maxtinion\n@_deejay87_\n@PS__TRICKS\n\nThanks to all the devs in the scene who made this possible",
                )
            )
        elif self.Type == "CUSTOMdoneRmvCache":
            Message.setWindowTitle(_translate("Message", "Cache Removed"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Cached icons has been removed.",
                )
            )
        elif self.Type == "PermissionDenied":
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Error Iconit needs admin permission to perform the task. Rerun as administrator",
                )
            )

        elif self.Type == "Invalid":
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Invalid IP or Port (Alphabets not allowed).\n" + self.copyright,
                )
            )

        elif self.Type == "IconIssue":
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Invalid IP or Port (Alphabets not allowed).\n" + self.copyright,
                )
            )

        elif self.Type == "Invalid icon size":
            Message.setWindowTitle(_translate("Message", "Too small icon ERROR"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Invalid icon size 'too small'. Minimum size required (440x440).\n"
                    + self.copyright,
                )
            )
        elif self.Type == "disconnected":
            Message.setWindowTitle(_translate("Message", "Too small icon ERROR"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "Disconnected from PS4. Re-enable FTP payload.\n" + self.copyright,
                )
            )

        elif self.Type == "Magick image not found":
            Message.setWindowTitle(_translate("Message", "Too small icon ERROR"))
            self.Message.setPlainText(
                _translate(
                    "Message",
                    "ImageMagick not installed in \nrequired path.\nInstall it from 'Install This' Folder\n"
                    + self.copyright,
                )
            )

        else:
            Message.setWindowTitle(_translate("Message", "Error"))
            self.Message.setPlainText(
                _translate(
                    "Message", "Error Type: " + self.Type + ". \n" + self.copyright
                )
            )

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Message = QtWidgets.QDialog()
    ui = Ui_Message()
    ui.setupUi(Message)
    Message.show()
    sys.exit(app.exec_())
