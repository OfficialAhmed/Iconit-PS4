from PyQt5 import QtCore, QtWidgets
from Module.Custom_group import Main as Custom_group

class Ui(Custom_group):

    def __init__(self) -> None:
        super().__init__()


    def setupUi(self, window):
        self.window = window
        self.window.setObjectName("Dialog")
        self.window.resize(503, 301)

        self.gridLayout = QtWidgets.QGridLayout()
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea(self.window)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.window)
        self.group_title_label = QtWidgets.QLabel(self.window)

        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 481, 222))
        self.formLayout_3 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)

        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setVerticalSpacing(10)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.formLayout_6.setContentsMargins(0, 0, -1, -1)
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.group_title_label)
        self.group_title_input = QtWidgets.QLineEdit(self.window)
        self.group_title_input.setAlignment(QtCore.Qt.AlignCenter)
        self.group_title_input.setClearButtonEnabled(True)
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.group_title_input)
        self.verticalLayout_2.addLayout(self.formLayout_6)

        self.buttonBox = QtWidgets.QDialogButtonBox(self.window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setObjectName("scrollArea")
        self.formLayout_6.setObjectName("formLayout_6")
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_title_input.setObjectName("group_title_input")
        self.group_title_label.setObjectName("group_title_label")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        """
        #################################################################
                    CUSTOM SELECT/DESELECT ALL BTNs
        #################################################################
        """

        self.selectAllBtn = QtWidgets.QPushButton()
        self.deselectAllBtn = QtWidgets.QPushButton()
        self.buttonBox.addButton(self.selectAllBtn, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.deselectAllBtn, QtWidgets.QDialogButtonBox.ActionRole)


        """
        #################################################################
                    RENDER GAME ID/TITLE AS CHECKBOX
        #################################################################
        """

        self.checkboxes:list = []
        ids:dict = self.get_ids()
        row = 0

        for id, id_info in ids.items():
            checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            checkbox.setObjectName(id)
            checkbox.setText(f"[{id}] {id_info.get('title')}")

            self.gridLayout.addWidget(checkbox, row, 1, 1, 1)
            self.checkboxes.append(checkbox)

            row += 1


        self.retranslateUi()
        self.buttonBox.rejected.connect(self.window.reject)
        self.buttonBox.accepted.connect(lambda: self.save_group())
        self.selectAllBtn.clicked.connect(lambda: self.select_all())
        self.deselectAllBtn.clicked.connect(lambda: self.deselect_all())


        QtCore.QMetaObject.connectSlotsByName(self.window)


    def retranslateUi(self):

        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("Dialog", "CUSTOM GROUPs"))

        self.selectAllBtn.setText(_translate("Dialog", "Select all"))
        self.deselectAllBtn.setText(_translate("Dialog", "Deselect all"))
        self.group_title_label.setText(_translate("Dialog", "GROUP TITLE"))
        self.group_title_input.setPlaceholderText(_translate("Dialog", "i.e. Homebrews"))