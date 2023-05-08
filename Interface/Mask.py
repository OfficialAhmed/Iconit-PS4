from PyQt5 import QtCore, QtGui, QtWidgets
from Module.Mask import Main as Mask

class Ui(Mask):

    def setupUi(self, window):
        
        window.setObjectName("mask_maker")
        window.resize(690, 573)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem)
        self.UpperLayout = QtWidgets.QGridLayout()
        self.UpperLayout.setObjectName("UpperLayout")
        self.MaskView = QtWidgets.QGraphicsView(window)
        self.MaskView.setMinimumSize(QtCore.QSize(250, 260))
        self.MaskView.setMaximumSize(QtCore.QSize(250, 250))
        self.MaskView.setObjectName("MaskView")
        self.UpperLayout.addWidget(self.MaskView, 5, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GroupName = QtWidgets.QLabel(window)
        self.GroupName.setObjectName("GroupName")
        self.gridLayout_3.addWidget(self.GroupName, 0, 2, 1, 1)

        self.GroupBtn = QtWidgets.QPushButton(window)
        self.GroupBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GroupBtn.setObjectName("GroupBtn")
        self.gridLayout_3.addWidget(self.GroupBtn, 0, 0, 1, 1)
        self.UpperLayout.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MaskName = QtWidgets.QLabel(window)
        self.MaskName.setObjectName("MaskName")
        self.gridLayout_2.addWidget(self.MaskName, 0, 2, 1, 1)

        self.MaskBtn = QtWidgets.QPushButton(window)
        self.MaskBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MaskBtn.setObjectName("MaskBtn")
        self.gridLayout_2.addWidget(self.MaskBtn, 0, 0, 1, 1)
        self.UpperLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.BakeState = QtWidgets.QLabel(window)
        self.BakeState.setObjectName("BakeState")
        self.gridLayout_5.addWidget(self.BakeState, 1, 1, 1, 1)
        self.UploadState = QtWidgets.QLabel(window)
        self.UploadState.setObjectName("UploadState")
        self.gridLayout_5.addWidget(self.UploadState, 2, 1, 1, 1)

        self.UploadBtn = QtWidgets.QPushButton(window)
        self.UploadBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UploadBtn.sizePolicy().hasHeightForWidth())
        self.UploadBtn.setSizePolicy(sizePolicy)
        self.UploadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UploadBtn.setObjectName("UploadBtn")
        self.gridLayout_5.addWidget(self.UploadBtn, 2, 0, 1, 1)

        self.BakeBtn = QtWidgets.QPushButton(window)
        self.BakeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BakeBtn.setObjectName("BakeBtn")
        self.gridLayout_5.addWidget(self.BakeBtn, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.UpperLayout.addLayout(self.gridLayout_5, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.UpperLayout.addItem(spacerItem2, 5, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.UpperLayout.addItem(spacerItem3, 5, 0, 1, 1)

        self.BakedView = QtWidgets.QGraphicsView(window)
        self.BakedView.setMinimumSize(QtCore.QSize(250, 260))
        self.BakedView.setMaximumSize(QtCore.QSize(250, 250))
        self.BakedView.setStyleSheet("border-image: url(:/newPrefix/Documents/GitHub/Iconit-PS4/test/10.png);")
        self.BakedView.setObjectName("BakedView")
        self.UpperLayout.addWidget(self.BakedView, 5, 2, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.UpperLayout.addItem(spacerItem4, 4, 1, 1, 1)
        self.mainLayout.addLayout(self.UpperLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem5)
        self.line = QtWidgets.QFrame(window)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mainLayout.addWidget(self.line)
        self.ButtomLayout = QtWidgets.QGridLayout()
        self.ButtomLayout.setContentsMargins(-1, 17, -1, -1)
        self.ButtomLayout.setObjectName("ButtomLayout")
        self.ContinueProcessLabel = QtWidgets.QLabel(window)
        self.ContinueProcessLabel.setObjectName("ContinueProcessLabel")

        self.ButtomLayout.addWidget(self.ContinueProcessLabel, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtomLayout.addItem(spacerItem6, 0, 4, 1, 1)

        self.ContinueProcessBtn = QtWidgets.QPushButton(window)
        self.ContinueProcessBtn.setEnabled(False)
        self.ContinueProcessBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ContinueProcessBtn.setObjectName("ContinueProcessBtn")
        self.ButtomLayout.addWidget(self.ContinueProcessBtn, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.ButtomLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.mainLayout.addLayout(self.ButtomLayout)
        self.CreditsLayout = QtWidgets.QHBoxLayout()
        self.CreditsLayout.setObjectName("CreditsLayout")

        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CreditsLayout.addItem(spacerItem8)

        self.IconitLinkLabel = QtWidgets.QLabel(window)
        self.FreeMasksLinkLabel = QtWidgets.QLabel(window)

        links = (self.IconitLinkLabel, self.FreeMasksLinkLabel)

        for indx, link in enumerate(links):
            
            if indx == 1:
                spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.CreditsLayout.addItem(spacerItem9)

            link.setOpenExternalLinks(True)
            self.CreditsLayout.addWidget(link)

        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CreditsLayout.addItem(spacerItem10)

        self.mainLayout.addLayout(self.CreditsLayout)
        self.verticalLayout_2.addLayout(self.mainLayout)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)


    def retranslateUi(self, window):

        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("mask_maker", "Iconit - Mask maker"))

        self.BakeBtn.setText(_translate("mask_maker", "BAKE ICONS"))
        self.MaskBtn.setText(_translate("mask_maker", "Mask..."))
        self.GroupBtn.setText(_translate("mask_maker", "Group..."))
        self.ContinueProcessBtn.setText(_translate("mask_maker", "Continue"))
        self.UploadBtn.setText(_translate("mask_maker", "UPLOAD BAKED ICONS"))

        self.MaskName.setText(_translate("mask_maker", ""))
        self.GroupName.setText(_translate("mask_maker", ""))

        self.BakeState.setText(_translate("mask_maker", self.html.span_tag('AWAITING...', self.constant.get_color('orange'), 8)))
        self.UploadState.setText(_translate("mask_maker", self.html.span_tag('BAKING REQUIRED', self.constant.get_color('red'), 8)))
        self.ContinueProcessLabel.setText(_translate("mask_maker", "If anything goes wrong while uploading the icons click 'continue' anytime to proceed the process from where it stopped."))
        self.IconitLinkLabel.setText(_translate("mask_maker", self.html.a_tag('https://github.com/OfficialAhmed/Iconit-PS4/releases', 'Iconit', '#f250e7', 9)))
        self.FreeMasksLinkLabel.setText(_translate("mask_maker", self.html.a_tag('https://all-exhost.github.io/Masks.html', 'Download Free Masks', '#f250e7', 9)))

        self.MaskBtn.clicked.connect(self.browse_mask)
        self.GroupBtn.clicked.connect(self.browse_icon_group)
        self.BakeBtn.clicked.connect(self.bake_mask)    
