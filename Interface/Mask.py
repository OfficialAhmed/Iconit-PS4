import os
from PyQt5 import QtCore, QtGui, QtWidgets
from Module.Mask import Main as Mask
from Module.Multi_upload import Main as multi_upload

class Ui(Mask):

    def setupUi(self, window):
        
        window.resize(690, 573)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(window)
        self.mainLayout = QtWidgets.QVBoxLayout()

        spacer_widget_min_exp = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer_widget_exp_min = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        spacerItem = spacer_widget_min_exp
        self.mainLayout.addItem(spacerItem)
        self.UpperLayout = QtWidgets.QGridLayout()
        self.MaskView = QtWidgets.QGraphicsView(window)
        self.MaskView.setMinimumSize(QtCore.QSize(250, 260))
        self.MaskView.setMaximumSize(QtCore.QSize(250, 250))
        self.UpperLayout.addWidget(self.MaskView, 5, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.GroupName = QtWidgets.QLabel(window)
        self.gridLayout_3.addWidget(self.GroupName, 0, 2, 1, 1)

        self.GroupBtn = QtWidgets.QPushButton(window)
        self.GroupBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.GroupBtn, 0, 0, 1, 1)

        self.RevertBtn = QtWidgets.QPushButton(window)
        self.RevertBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_3.addWidget(self.RevertBtn, 1, 0, 1, 1)

        self.UpperLayout.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.MaskName = QtWidgets.QLabel(window)
        self.gridLayout_2.addWidget(self.MaskName, 0, 2, 1, 1)

        self.MaskBtn = QtWidgets.QPushButton(window)
        self.MaskBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_2.addWidget(self.MaskBtn, 0, 0, 1, 1)
        self.UpperLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.BakeState = QtWidgets.QLabel(window)
        self.gridLayout_5.addWidget(self.BakeState, 1, 1, 1, 1)
        self.UploadState = QtWidgets.QLabel(window)
        self.gridLayout_5.addWidget(self.UploadState, 2, 1, 1, 1)

        self.UploadBtn = QtWidgets.QPushButton(window)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UploadBtn.sizePolicy().hasHeightForWidth())
        self.UploadBtn.setSizePolicy(sizePolicy)
        self.UploadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_5.addWidget(self.UploadBtn, 2, 0, 1, 1)

        self.BakeBtn = QtWidgets.QPushButton(window)
        self.BakeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_5.addWidget(self.BakeBtn, 1, 0, 1, 1)
        spacerItem1 = spacer_widget_min_exp
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.UpperLayout.addLayout(self.gridLayout_5, 7, 1, 1, 1)
        spacerItem2 = spacer_widget_exp_min
        self.UpperLayout.addItem(spacerItem2, 5, 3, 1, 1)
        spacerItem3 = spacer_widget_exp_min
        self.UpperLayout.addItem(spacerItem3, 5, 0, 1, 1)

        self.BakedView = QtWidgets.QGraphicsView(window)
        self.BakedView.setMinimumSize(QtCore.QSize(250, 260))
        self.BakedView.setMaximumSize(QtCore.QSize(250, 250))
        self.UpperLayout.addWidget(self.BakedView, 5, 2, 1, 1)

        spacerItem4 = spacer_widget_min_exp
        self.UpperLayout.addItem(spacerItem4, 4, 1, 1, 1)
        self.mainLayout.addLayout(self.UpperLayout)
        spacerItem5 = spacer_widget_min_exp
        self.mainLayout.addItem(spacerItem5)

        self.line = QtWidgets.QFrame(window)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainLayout.addWidget(self.line)
        
        self.ButtomLayout = QtWidgets.QGridLayout()
        self.ButtomLayout.setContentsMargins(-1, 17, -1, -1)
        self.ContinueProcessLabel = QtWidgets.QLabel(window)

        self.ButtomLayout.addWidget(self.ContinueProcessLabel, 0, 3, 1, 1)
        spacerItem6 = spacer_widget_exp_min
        self.ButtomLayout.addItem(spacerItem6, 0, 4, 1, 1)

        self.ContinueProcessBtn = QtWidgets.QPushButton(window)
        self.ContinueProcessBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtomLayout.addWidget(self.ContinueProcessBtn, 0, 1, 1, 1)
        spacerItem7 = spacer_widget_exp_min
        
        self.ButtomLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.mainLayout.addLayout(self.ButtomLayout)
        self.CreditsLayout = QtWidgets.QHBoxLayout()

        spacerItem8 = spacer_widget_exp_min
        self.CreditsLayout.addItem(spacerItem8)

        self.IconitLinkLabel = QtWidgets.QLabel(window)
        self.FreeMasksLinkLabel = QtWidgets.QLabel(window)

        links = (self.IconitLinkLabel, self.FreeMasksLinkLabel)

        for indx, link in enumerate(links):
            
            if indx == 1:
                spacerItem9 = spacer_widget_exp_min
                self.CreditsLayout.addItem(spacerItem9)

            link.setOpenExternalLinks(True)
            self.CreditsLayout.addWidget(link)

        spacerItem10 = spacer_widget_exp_min
        self.CreditsLayout.addItem(spacerItem10)

        self.mainLayout.addLayout(self.CreditsLayout)
        self.verticalLayout_2.addLayout(self.mainLayout)


        """
        #################################################################
                        BTN BEHAVIOR ON RENDER
        #################################################################
        """
        self.BakeBtn.setEnabled(False)
        self.UploadBtn.setEnabled(False)
        self.RevertBtn.setEnabled(False)


        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)


    def retranslateUi(self, window):

        win_name = "MaskMakerWindow"
        _translate = QtCore.QCoreApplication.translate

        window.setWindowTitle(_translate(win_name, self.translated_content.get("WindowTitle")))
        self.MaskName.setText(_translate(win_name, ""))
        self.GroupName.setText(_translate(win_name, ""))

        self.BakeBtn.setText(_translate(win_name, self.translated_content.get("BakeBtn")))
        self.MaskBtn.setText(_translate(win_name, self.translated_content.get("MaskBtn")))
        self.GroupBtn.setText(_translate(win_name, self.translated_content.get("GroupBtn")))
        self.RevertBtn.setText(_translate(win_name, self.translated_content.get("RevertBtn")))
        self.UploadBtn.setText(_translate(win_name, self.translated_content.get("UploadBtn")))
        self.ContinueProcessBtn.setText(_translate(win_name, self.translated_content.get("ContinueProcessBtn")))

        self.BakeState.setText(
            _translate(
                win_name, 
                self.html.span_tag(
                    self.translated_content.get("BakeState"), 
                    self.constant.get_color('orange'),
                    8
                )
            )
        )
        
        self.ContinueProcessLabel.setText(
            _translate(
                win_name, 
                self.translated_content.get("ContinueProcessLabel")
            )
        )
        
        self.IconitLinkLabel.setText(
            _translate(
                win_name, 
                self.html.a_tag(
                    'https://github.com/OfficialAhmed/Iconit-PS4/releases', 
                    'Iconit', 
                    '#f250e7', 
                    9
                )
            )
        )

        self.FreeMasksLinkLabel.setText(
            _translate(
                win_name, 
                self.html.a_tag(
                    'https://all-exhost.github.io/Masks.html', 
                    self.translated_content.get("FreeMasksLinkLabel"), 
                    '#f250e7', 
                    9
                )
            )
        )

        self.UploadState.setText(
            _translate(
                win_name, 
                self.translated_content.get("UploadState")
            )
        )
        

        """
        #################################################################
                        CONTINUE PROCESS - FEATURE
        #################################################################
        """
        self.ContinueProcessBtn.setEnabled(False)

        for baked in os.listdir(self.baked_path):
            if ".png" in baked:
                self.ContinueProcessBtn.setEnabled(True)
                self.alerts.display(self.translated_content.get("WarnWindowTitle"), "incompleteProcess")
                break


        """
        #################################################################
                                SIGNALS
        #################################################################
        """
        self.BakeBtn.clicked.connect(self.bake_mask)    
        self.MaskBtn.clicked.connect(self.browse_mask)
        self.GroupBtn.clicked.connect(self.browse_icon_group)
        self.RevertBtn.clicked.connect(self.revert_to_default)

        multi_upload_obj = multi_upload()
        self.UploadBtn.clicked.connect(lambda: multi_upload_obj.generate_icons_from_baked(self.UploadState, self.UploadBtn, self.group_path))
        self.ContinueProcessBtn.clicked.connect(lambda: multi_upload_obj.continue_upload(self.ContinueProcessBtn, self.UploadBtn, self.UploadState))
