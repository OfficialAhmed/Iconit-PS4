from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mask_maker(object):
    def setupUi(self, mask_maker):
        mask_maker.setObjectName("mask_maker")
        mask_maker.resize(604, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mask_maker.sizePolicy().hasHeightForWidth())
        mask_maker.setSizePolicy(sizePolicy)
        mask_maker.setMaximumSize(QtCore.QSize(604, 630))
        self.gridLayout_2 = QtWidgets.QGridLayout(mask_maker)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bake_view = QtWidgets.QGraphicsView(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bake_view.sizePolicy().hasHeightForWidth())
        self.bake_view.setSizePolicy(sizePolicy)
        self.bake_view.setMinimumSize(QtCore.QSize(256, 256))
        self.bake_view.setMaximumSize(QtCore.QSize(256, 256))
        self.bake_view.setStyleSheet("border-image: url(:/newPrefix/Pictures/Wallpapers/nload-at-WallpaperBro.png);")
        self.bake_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bake_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bake_view.setObjectName("bake_view")
        self.horizontalLayout_2.addWidget(self.bake_view)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(1, 10, 1, -1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bake_btn = QtWidgets.QPushButton(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bake_btn.sizePolicy().hasHeightForWidth())
        self.bake_btn.setSizePolicy(sizePolicy)
        self.bake_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.bake_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bake_btn.setFont(font)
        self.bake_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bake_btn.setObjectName("bake_btn")
        self.verticalLayout_3.addWidget(self.bake_btn)
        self.bake_progress = QtWidgets.QProgressBar(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bake_progress.sizePolicy().hasHeightForWidth())
        self.bake_progress.setSizePolicy(sizePolicy)
        self.bake_progress.setMaximumSize(QtCore.QSize(16777215, 15))
        self.bake_progress.setStyleSheet("QProgressBar {border-radius: 10px; color:rgb(255, 255, 255);}\n"
"QProgressBar::chunk {background: QLinearGradient( x1:0.358, y1:0.602182, x2:0.960318, y2:0.648, stop:0 rgb(124, 57, 191), stop:0.903409 rgb(242, 80, 231)); border-radius: 10px;};")
        self.bake_progress.setProperty("value", 50)
        self.bake_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.bake_progress.setTextVisible(True)
        self.bake_progress.setOrientation(QtCore.Qt.Horizontal)
        self.bake_progress.setObjectName("bake_progress")
        self.verticalLayout_3.addWidget(self.bake_progress)
        self.bake_state = QtWidgets.QLabel(mask_maker)
        self.bake_state.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bake_state.setFont(font)
        self.bake_state.setAlignment(QtCore.Qt.AlignCenter)
        self.bake_state.setObjectName("bake_state")
        self.verticalLayout_3.addWidget(self.bake_state)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.back_preview_btn = QtWidgets.QPushButton(mask_maker)
        self.back_preview_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_preview_btn.setFont(font)
        self.back_preview_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_preview_btn.setObjectName("back_preview_btn")
        self.verticalLayout_3.addWidget(self.back_preview_btn)
        self.bake_apply_btn = QtWidgets.QPushButton(mask_maker)
        self.bake_apply_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bake_apply_btn.setFont(font)
        self.bake_apply_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bake_apply_btn.setObjectName("bake_apply_btn")
        self.verticalLayout_3.addWidget(self.bake_apply_btn)
        self.download_mask_link = QtWidgets.QLabel(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_mask_link.sizePolicy().hasHeightForWidth())
        self.download_mask_link.setSizePolicy(sizePolicy)
        self.download_mask_link.setObjectName("download_mask_link")
        self.verticalLayout_3.addWidget(self.download_mask_link)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(10, -1, 10, -1)
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setObjectName("formLayout_2")
        self.game_icon_label = QtWidgets.QLabel(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_icon_label.sizePolicy().hasHeightForWidth())
        self.game_icon_label.setSizePolicy(sizePolicy)
        self.game_icon_label.setMinimumSize(QtCore.QSize(256, 40))
        self.game_icon_label.setMaximumSize(QtCore.QSize(256, 40))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.game_icon_label.setFont(font)
        self.game_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_icon_label.setObjectName("game_icon_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.game_icon_label)
        self.game_icon_view = QtWidgets.QGraphicsView(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_icon_view.sizePolicy().hasHeightForWidth())
        self.game_icon_view.setSizePolicy(sizePolicy)
        self.game_icon_view.setMinimumSize(QtCore.QSize(256, 256))
        self.game_icon_view.setMaximumSize(QtCore.QSize(256, 256))
        self.game_icon_view.setStyleSheet("border-image: url(:/newPrefix/Pictures/Wallpapers/nload-at-WallpaperBro.png);")
        self.game_icon_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.game_icon_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.game_icon_view.setObjectName("game_icon_view")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.game_icon_view)
        self.mask_view = QtWidgets.QGraphicsView(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_view.sizePolicy().hasHeightForWidth())
        self.mask_view.setSizePolicy(sizePolicy)
        self.mask_view.setMaximumSize(QtCore.QSize(256, 256))
        self.mask_view.setStyleSheet("border-image: url(:/newPrefix/All-exHost.github.io/images/masks/mask/PS4 COVER.png);")
        self.mask_view.setObjectName("mask_view")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mask_view)
        self.game_icon_btn = QtWidgets.QPushButton(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_icon_btn.sizePolicy().hasHeightForWidth())
        self.game_icon_btn.setSizePolicy(sizePolicy)
        self.game_icon_btn.setMinimumSize(QtCore.QSize(256, 0))
        self.game_icon_btn.setMaximumSize(QtCore.QSize(256, 40))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.game_icon_btn.setFont(font)
        self.game_icon_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game_icon_btn.setObjectName("game_icon_btn")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.game_icon_btn)
        self.mask_label = QtWidgets.QLabel(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_label.sizePolicy().hasHeightForWidth())
        self.mask_label.setSizePolicy(sizePolicy)
        self.mask_label.setMinimumSize(QtCore.QSize(256, 40))
        self.mask_label.setMaximumSize(QtCore.QSize(256, 40))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mask_label.setFont(font)
        self.mask_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_label.setObjectName("mask_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mask_label)
        self.mask_btn = QtWidgets.QPushButton(mask_maker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_btn.sizePolicy().hasHeightForWidth())
        self.mask_btn.setSizePolicy(sizePolicy)
        self.mask_btn.setMinimumSize(QtCore.QSize(256, 0))
        self.mask_btn.setMaximumSize(QtCore.QSize(256, 30))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mask_btn.setFont(font)
        self.mask_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mask_btn.setObjectName("mask_btn")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mask_btn)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(mask_maker)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(mask_maker)
        QtCore.QMetaObject.connectSlotsByName(mask_maker)
        mask_maker.setTabOrder(self.game_icon_btn, self.game_icon_view)
        mask_maker.setTabOrder(self.game_icon_view, self.mask_view)

    def retranslateUi(self, mask_maker):
        _translate = QtCore.QCoreApplication.translate
        mask_maker.setWindowTitle(_translate("mask_maker", "Mask maker by @Officialahmed0"))
        self.bake_btn.setText(_translate("mask_maker", "Bake Mask"))
        self.bake_state.setText(_translate("mask_maker", "Baking process required"))
        self.back_preview_btn.setText(_translate("mask_maker", "Preview"))
        self.bake_apply_btn.setText(_translate("mask_maker", "Apply"))        
        self.download_mask_link.setText(_translate("mask_maker",'<html><head/><body><p align="center"><a href="https://all-exhost.github.io/Masks.html"><span style="font-family:\'verdana\'; font-size:14pt; text-decoration: underline; color:#90f542; vertical-align:super;">Download masks<br>https://all-exhost.github.io/Masks.html</span></a></p></body></html>',))
        self.game_icon_label.setText(_translate("mask_maker", "Game Icon"))
        self.game_icon_btn.setText(_translate("mask_maker", "Change..."))
        self.mask_label.setText(_translate("mask_maker", "Mask"))
        self.mask_btn.setText(_translate("mask_maker", "Change..."))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ChangeIconWindow = QtWidgets.QWidget()
    ui = Ui_mask_maker()
    ui.setupUi(ChangeIconWindow)
    ChangeIconWindow.show()
    sys.exit(app.exec_())