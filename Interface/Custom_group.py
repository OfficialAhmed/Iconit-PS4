from PyQt5 import QtCore, QtWidgets
from Module.Custom_group import Main as Custom_group

class Ui(Custom_group):

    def __init__(self) -> None:
        super().__init__()


    def setupUi(self, window):
        self.window = window
        self.window.setObjectName("Dialog")
        self.window.resize(503, 301)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.window)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.window)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 481, 222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_3 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_3.setObjectName("formLayout_3")


        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setContentsMargins(0, 0, -1, -1)
        self.formLayout_6.setObjectName("formLayout_6")
        self.group_title_label = QtWidgets.QLabel(self.window)
        self.group_title_label.setObjectName("group_title_label")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.group_title_label)
        self.group_title_input = QtWidgets.QLineEdit(self.window)
        self.group_title_input.setAlignment(QtCore.Qt.AlignCenter)
        self.group_title_input.setClearButtonEnabled(True)
        self.group_title_input.setObjectName("group_title_input")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.group_title_input)
        self.verticalLayout_2.addLayout(self.formLayout_6)

        self.buttonBox = QtWidgets.QDialogButtonBox(self.window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        #___________    CUSTOM SELECT/DESELECT ALL BTNs    _______________ #

        self.selectAllBtn = QtWidgets.QPushButton("Select all")
        self.buttonBox.addButton(self.selectAllBtn, QtWidgets.QDialogButtonBox.ActionRole)
        self.deselectAllBtn = QtWidgets.QPushButton("Deselect all")
        self.buttonBox.addButton(self.deselectAllBtn, QtWidgets.QDialogButtonBox.ActionRole)


        #___________    Render Game ID - title as checkbox    _______________ #
        self.checkboxes:list = []
        ids:dict = self.get_ids()
        row = 0

        for id, id_info in ids.items():
            content = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            content.setObjectName(id)
            content.setText(f"[{id}] {id_info.get('title')}")

            self.gridLayout.addWidget(content, row, 1, 1, 1)
            self.checkboxes.append(content)

            row += 1


        self.retranslateUi()
        self.buttonBox.accepted.connect(lambda: self.save_group())
        self.buttonBox.rejected.connect(self.window.reject)
        self.selectAllBtn.clicked.connect(lambda: self.select_all())
        self.deselectAllBtn.clicked.connect(lambda: self.deselect_all())


        QtCore.QMetaObject.connectSlotsByName(self.window)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("Dialog", "CUSTOM GROUPs"))

        self.group_title_label.setText(_translate("Dialog", "GROUP TITLE"))
        self.group_title_input.setPlaceholderText(_translate("Dialog", "i.e. Homebrews"))