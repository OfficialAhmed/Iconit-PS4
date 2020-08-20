from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
import Message, ChangeIcon, ProfileIcons

# connection through FTP
from ftplib import FTP
import os, sys, time
# resizing images
from PIL import Image
import PIL

ftp = FTP()
working_dir = "user/appmeta"
local_path = str(os.getcwd())
temp_path = local_path + "\Data\prxUserMeta\\"
img_dir = local_path + "\\data\\User\\appmeta"

setting_path = ""
for change in local_path:
    if change == "\\":
        setting_path += "/"
    else:
        setting_path += change

IP = ""
Port = 1337 #Al-Azif's default FTP payload Port

all_CUSA = []
all_CUSA_ex = []
Game = {}
class Ui_IPortWindow(object):
    def setupUi(self, IPortWindow):
        global local_path, setting_path, temp_path
        IPortWindow.setObjectName("IPortWindow")
        IPortWindow.resize(409, 290)
        IPortWindow.setMinimumSize(QtCore.QSize(409, 290))
        IPortWindow.setMaximumSize(QtCore.QSize(409, 290))
        IPortWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        IPortWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        IPortWindow.setWindowIcon(QtGui.QIcon(local_path + "\Data\Pref\ic1.@OfficialAhmed0"))
        self.centralwidget = QtWidgets.QWidget(IPortWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Settings
        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIPath = local_path
        self.userDPath = local_path
        self.userHB = "False"
        try:
            with open(temp_path + "pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2: -1]
                self.userPort = content[1][2: -1]
                self.userIPath = content[2][6: -1]
                self.userDPath = content[3][6: -1]
                self.userHB = (content[4][content[4].find(":")+1:])
        except:
            pass
        font = QtGui.QFont()
        font.setFamily(self.userFont)
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        
        self.BackgroundView = QtWidgets.QGraphicsView(self.centralwidget)
        self.BackgroundView.setGeometry(QtCore.QRect(-940, -490, 1461, 871))
        self.BackgroundView.setStyleSheet("background-image: url("+ setting_path +"/Data/Pref/bg.@OfficialAhmed0);")
        self.BackgroundView.setFrameShape(QtWidgets.QFrame.Box)
        self.BackgroundView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BackgroundView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.BackgroundView.setObjectName("BackgroundView")
        self.IP_Label = QtWidgets.QLabel(self.centralwidget)
        self.IP_Label.setGeometry(QtCore.QRect(20, 60, 71, 51))
        self.IP_Label.setStyleSheet("font: 11pt \""+self.userFont+"\"; color: rgb(85, 170, 255);")
        self.IP_Label.setObjectName("IP_Label")
        
        self.Port_Label = QtWidgets.QLabel(self.centralwidget)
        self.Port_Label.setGeometry(QtCore.QRect(20, 100, 71, 51))
        self.Port_Label.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(85, 170, 255);")
        self.Port_Label.setObjectName("Port_Label")

        self.Change_label = QtWidgets.QLabel(self.centralwidget)
        self.Change_label.setGeometry(QtCore.QRect(20, 155, 71, 51))
        self.Change_label.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(85, 170, 255);")
        self.Change_label.setObjectName("Change_label")

        self.IP_input = QtWidgets.QLineEdit(self.centralwidget)
        self.IP_input.setGeometry(QtCore.QRect(110, 70, 201, 31))
        self.IP_input.setFont(font)
        self.IP_input.setStyleSheet("background-color: rgb(77, 99, 126); border-radius: 5px;")
        self.IP_input.setMaxLength(24)
        self.IP_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.IP_input.setAlignment(QtCore.Qt.AlignCenter)
        self.IP_input.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.IP_input.setClearButtonEnabled(True)
        self.IP_input.setObjectName("IP_input")
        
        self.Port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Port_input.setGeometry(QtCore.QRect(110, 110, 201, 31))
        self.Port_input.setFont(font)
        self.Port_input.setStyleSheet("background-color: rgb(77, 99, 126); border-radius: 5px;")
        self.Port_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Port_input.setMaxLength(8)
        self.Port_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Port_input.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_input.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.Port_input.setClearButtonEnabled(True)
        self.Port_input.setObjectName("Port_input")

        font.setPointSize(8)
        self.Connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_btn.setGeometry(QtCore.QRect(264, 180, 93, 31))
        self.Connect_btn.setFont(font)
        self.Connect_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Connect_btn.setStyleSheet("background-color: rgb(77, 99, 126);")
        self.Connect_btn.setText("Connect PS4")
        self.Connect_btn.setObjectName("Connect_btn")

        self.Connect_btn.clicked.connect(self.Check_IPort)
        
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(110, 20, 185, 31))
        self.Status.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(85, 170, 255);")
        self.Status.setFrameShape(QtWidgets.QFrame.Panel)
        self.Status.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")

        self.Credits = QtWidgets.QLabel(self.centralwidget)
        self.Credits.setGeometry(QtCore.QRect(10, 230, 191, 41))

        self.Credits.setFont(font)
        self.Credits.setStyleSheet("font: 9pt \""+ self.userFont +"\"; color: rgba(85, 170, 255, 80);")
        self.Credits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Credits.setAlignment(QtCore.Qt.AlignCenter)
        self.Credits.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Credits.setObjectName("Credits")

        self.CacheBar = QtWidgets.QProgressBar(self.centralwidget)
        self.CacheBar.setGeometry(QtCore.QRect(80, 220, 121, 21))
        self.CacheBar.setProperty("value", 0)
        self.CacheBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CacheBar.setOrientation(QtCore.Qt.Horizontal)
        self.CacheBar.setObjectName("CacheBar")

        self.Cache_label = QtWidgets.QLabel(self.centralwidget)
        self.Cache_label.setGeometry(QtCore.QRect(20, 200, 71, 51))
        self.Cache_label.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(85, 170, 255);")
        self.Cache_label.setObjectName("Cache_label")

        self.ProfileIcon_label = QtWidgets.QLabel(self.centralwidget)
        self.ProfileIcon_label.setGeometry(QtCore.QRect(130, 170, 71, 51))
        self.ProfileIcon_label.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(85, 170, 255);")
        self.ProfileIcon_label.setObjectName("ProfileIcon_label")
        self.ProfileIcon = QtWidgets.QRadioButton(self.centralwidget)
        self.ProfileIcon.setGeometry(QtCore.QRect(100, 170, 71, 51))

        self.GameIcon_label = QtWidgets.QLabel(self.centralwidget)
        self.GameIcon_label.setGeometry(QtCore.QRect(130, 140, 71, 51))
        self.GameIcon_label.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(85, 170, 255);")
        self.GameIcon_label.setObjectName("GameIcon_label")
        self.GameIcon = QtWidgets.QRadioButton(self.centralwidget)
        self.GameIcon.setGeometry(QtCore.QRect(100, 140, 71, 51))
        self.GameIcon.setChecked(True)

        # Settings
        IPortWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IPortWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        IPortWindow.setMenuBar(self.menubar)

        self.About = QtWidgets.QAction(IPortWindow)
        self.About.setObjectName("About")

        self.Options = QtWidgets.QAction(IPortWindow)
        self.Options.setObjectName("Options")

        self.menuSettings.addAction(self.Options)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.About)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.Options.triggered.connect(self.OpenOptions)
        self.About.triggered.connect(self.about)

        self.retranslateUi(IPortWindow)
        QtCore.QMetaObject.connectSlotsByName(IPortWindow)
    
    def OpenOptions(self):
        import OptionsWin
        self.window = QtWidgets.QDialog()
        self.ui = OptionsWin.Ui_OptionsWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def about(self):
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        self.ui.setupUi(self.window, "About")
        self.window.show()

    def retranslateUi(self, IPortWindow):
        _translate = QtCore.QCoreApplication.translate
        IPortWindow.setWindowTitle(_translate("IPortWindow", "Iconit v4.01"))
        self.IP_Label.setText(_translate("IPortWindow", "PS4 IP"))
        self.Port_Label.setText(_translate("IPortWindow", "PS4 Port"))
        self.IP_input.setPlaceholderText(_translate("IPortWindow", "Exp: 192.168.100.1"))
        self.Port_input.setText(_translate("IPortWindow", self.userPort))
        self.Port_input.setPlaceholderText(_translate("IPortWindow", "Exp: 1337"))
        self.Status.setText(_translate("IPortWindow", "Waiting to connect"))
        self.Credits.setText(_translate("IPortWindow", "Created by @OfficialAhmed0"))
        self.Cache_label.setText(_translate("IPortWindow", "Caching"))
        self.menuSettings.setTitle(_translate("IPortWindow", "Setting"))
        self.About.setText(_translate("IPortWindow", "About"))
        self.Options.setText(_translate("IPortWindow", "Options..."))
        self.ProfileIcon_label.setText(_translate("IPortWindow", "Profile Icon"))
        self.GameIcon_label.setText(_translate("IPortWindow", "Game Icon"))
        self.Change_label.setText(_translate("IPortWindow", "Change "))

    def Check_IPort(self):
        global IP, Port

        IP = self.IP_input.text()
        Port = self.Port_input.text()

        valid = True
        for i in IP:
            if i.isalpha():
                valid = False
                break
        for p in str(Port):
            if p.isalpha():
                valid = False
                break
        self.Connect_PS4(valid)

    def Connect_PS4(self, isvalid):
        global ftp, working_dir, IP, Port, local_path, all_CUSA, all_CUSA_ex, temp_path
        self.window = QtWidgets.QDialog()
        self.ui = Message.Ui_Message()
        if isvalid:
            try:
                #Delete old Cache
                try:
                    cache = os.listdir(temp_path + "MegaSRX\metadata")
                    for i in cache:
                        os.remove(temp_path + "MegaSRX\metadata\\" + str(i))
                except:
                    pass

                #Iconit Or Profileit ?
                if self.GameIcon.isChecked() == True:
                    self.iconDirs = [working_dir]
                    ftp.set_debuglevel(2)
                    ftp.connect(IP, int(Port))
                    ftp.login("", "")
                    ftp.cwd("user/appmeta")
                    #look for external folder in appmeta
                    directories = []
                    ftp.retrlines("LIST ", directories.append)
                    for dir in directories:
                        if "external" in dir:
                            print(">"*70, "External found")
                            self.iconDirs.append(working_dir + "/external")
                            break

                    self.Status.setText("Connected")
                    self.Status.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(92, 213, 21);")
                    self.Connect_btn.setEnabled(False)
                    self.GameIcon.setEnabled(False)
                    self.ProfileIcon.setEnabled(False)
                    for dir in self.iconDirs:
                        ftp.set_debuglevel(2)
                        ftp.connect(IP, int(Port))
                        ftp.login("", "")
                        try:
                            ftp.cwd(dir)
                        except:
                            pass
                        directories = []

                        ftp.retrlines("LIST ", directories.append)
                        """create a file & copy, paste all them directories within"""

                        all_directories_in_system = open(temp_path + "directories in system.dat", "w+")
                        for line in directories:
                            all_directories_in_system.write(line + "\n")
                        all_directories_in_system = open(temp_path + "directories in system.dat", "r")
                        all_lines = all_directories_in_system.readlines()
                        all_Games = open(temp_path + "All Games.dat", "w+")

                        """Take only CUSAxxxx from each line and write them on all Games.dat """
                        if self.userHB == "True": 
                            #Check Homebrews
                            HB_id = ("LAPY", "MODS", "CRST", "NPX", "PNE", "BOR", "FLT", "CUSB", "MEDN", "SLES", "SLUS", "SSNE")
                            for CUSA_lines in all_lines:
                                for HB in HB_id:
                                    if HB in CUSA_lines:
                                        index_l = CUSA_lines.index(HB)
                                        only_CUSA = CUSA_lines[index_l:]
                                        if "external" in dir:
                                            all_Games.write(only_CUSA)
                                            all_CUSA_ex.append(only_CUSA[:-1])
                                        else:
                                            all_Games.write(only_CUSA)
                                            all_CUSA.append(only_CUSA[:-1])

                        for CUSA_lines in all_lines:
                            if "CUSA" in CUSA_lines:
                                index_C = CUSA_lines.index("CUSA")
                                only_CUSA = CUSA_lines[index_C:]
                                if "external" in dir:
                                    all_Games.write(only_CUSA)
                                    all_CUSA_ex.append(only_CUSA[:-1])
                                else:
                                    all_Games.write(only_CUSA)
                                    all_CUSA.append(only_CUSA[:-1])

                    all_directories_in_system.close()
                    all_Games.close()
                    self.CacheGameIcon()

                else: #Profileit
                    ftp.set_debuglevel(2)
                    ftp.connect(IP, int(Port))
                    ftp.login("", "")
                    self.sysProfileRoot = "system_data/priv/cache/profile/"
                    self.userID = []
                    ftp.cwd(self.sysProfileRoot)
                    self.Status.setText("Connected")
                    self.Status.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(92, 213, 21);")
                    self.Connect_btn.setEnabled(False)
                    self.GameIcon.setEnabled(False)
                    self.ProfileIcon.setEnabled(False)
                    directories = []
                    ftp.retrlines("LIST ", directories.append)

                    with open(temp_path + "directories in system.dat", "w+") as all_directories_in_system:
                        for line in directories:
                            all_directories_in_system.write(line + "\n")
                    with open(temp_path + "directories in system.dat") as file:
                        lines = file.readlines()
                        for line in lines:
                            if "0x" in line:
                                account_index = line.index("0x")
                                self.userID.append(line[account_index:-1])
                    self.CacheProfileIcon()

            except Exception as e:
                self.Status.setText("Not connected")
                self.Status.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(255, 0, 0);")
                self.ui.setupUi(self.window, str(e))
                self.window.show()
        else:
            self.Status.setText("Not connected")
            self.Status.setStyleSheet("font: 11pt \""+ self.userFont +"\"; color: rgb(255, 0, 0);")
            self.ui.setupUi(self.window, "Invalid")
            self.window.show()

    def CacheProfileIcon(self):
        import shutil
        fileName = "online.json"
        dir = temp_path + "MegaSRX\metaprodata\\"
        progress = int(100/len(self.userID))
        progressed = 0
        self.CacheBar.setProperty("value", 1)
        for user in self.userID:
            ftp.set_debuglevel(0)
            ftp.connect(IP, int(Port))
            ftp.login("", "")
            ftp.cwd(self.sysProfileRoot + "/" + user)

            with open(dir + "\\" + user + ".png", "wb") as file:
                ftp.retrbinary("RETR " + "avatar.png", file.write, 1024)
            with open(dir + "\\" + user + ".json", "wb") as file:
                ftp.retrbinary("RETR " + fileName, file.write, 1024)

            #Download original Profile Icon from Sony server
            import requests as req
            try:
                with open(dir + "\\" + user + ".json") as file:
                    #Extract Icon url from json file
                    read = file.read()
                    url = read[read.find("avatarUrl") + len("avatarUrl") + 3 : read.find(".png")+len(".png")]
                    cont = url.split("\/")
                    link = ""
                    for i in cont:
                        if i != "":
                            link += i + "//"
                    img = req.get(link[:-2])
                    
                    with open(dir + "\\" + user + "Original.png", "wb") as origIcon:
                        origIcon.write(img.content)
            except:
                pass

            for i in range(1, progress):
                self.CacheBar.setProperty("value", progressed + i)
                time.sleep(0.01)
            progressed += progress
        self.CacheBar.setProperty("value", 100)
        self.OpenWindow("ProfileIcon")

    def CacheGameIcon(self):
        global all_CUSA, all_CUSA_ex, ftp, temp_path, working_dir, IP, Port, Game

        numGames = len(all_CUSA+all_CUSA_ex)

        file_name = "pronunciation.xml"
        icon_name = "icon0.png"
        CUSA = ""
        self.CacheBar.setProperty("value", 1)
        for dir in self.iconDirs:
            ftp.set_debuglevel(0)
            ftp.connect(IP, int(Port))
            ftp.login("", "")
            ftp.cwd(dir)
            counter = 0
            if "external" in dir:
                currentDir = all_CUSA_ex
            else:
                currentDir = all_CUSA
            for i in currentDir:
                if counter == int(numGames/2):
                    for i in range(25, 50):
                        self.CacheBar.setProperty("value", i)
                        time.sleep(0.01)
                elif counter == int(numGames/4):
                    for i in range(2, 25):
                        self.CacheBar.setProperty("value", i)
                        time.sleep(0.01)
                elif counter == int(numGames/(75/100)):
                    for i in range(50, 75):
                        self.CacheBar.setProperty("value", i)
                        time.sleep(0.01)
                ftp.cwd(currentDir[counter])
                CUSA = currentDir[counter]

                #Check the files in each game directory
                with open(temp_path + "files_in_dir.dat", "w+", encoding="utf8") as files_in_dir:
                    ftp.retrlines("LIST", files_in_dir.write)
                with open(temp_path + "files_in_dir.dat", "r", encoding="utf8") as files_in_dir:
                    content_in_file = files_in_dir.read()
                    #Check for pronunciation.xml or icon0
                    if file_name in content_in_file or icon_name in content_in_file :
                        current_CUSA = currentDir[counter]
                        if file_name in content_in_file:
                            with open(temp_path + file_name, "wb") as downloaded_file:
                                ftp.retrbinary("RETR " + file_name, downloaded_file.write, 1024)

                            with open(temp_path + "MegaSRX\metadata\\" + str(current_CUSA) + ".png", "wb") as downloaded_file:
                                ftp.retrbinary("RETR " + icon_name, downloaded_file.write, 1024) 

                            #Reading pronounciation.xml for gameTitle
                            with open(temp_path + file_name, "r", encoding="utf8") as file: 
                                with open(temp_path + "Possible game title.dat", "w+", encoding="utf8") as game_titles_file: #Create temp file
                                    for each_line in file:
                                        if "text" in each_line:
                                            game_titles_file.write(each_line)
                            #simplifying xml file
                            alpha = ("a A b B c C d D e E f F g G h H i I j J k K l L m M n N o O p P q Q r R s S t T u U v V w W x X y Y z Z ™ ' ! ?")
                            Eng = alpha.split(" ")
                            Eng.append(" ")
                            num = (1, 2, 3, 4 , 5, 6 , 7, 8 , 9, 0)
                            with open(temp_path + "Possible game title.dat", "r", encoding="utf8") as game_titles_file:
                                lines = game_titles_file.readlines()
                                GameTitle = ""
                                for line in lines:
                                    english = True
                                    starting_index = line.index(">") + 1
                                    original_title = line[starting_index : -8]

                                    if "One" or "Two" or "Three" or "Nine" or "Seven" or "Eight" or "Four" or "Six" in original_title:
                                        GameTitle = original_title
                                        Game[current_CUSA] = GameTitle
                                    else:
                                        for char in original_title:
                                            if char not in Eng and char not in num:
                                                english = False
                                                break
                                    if english:
                                        if len(original_title) > len(GameTitle):
                                            GameTitle = original_title
                                            Game[current_CUSA] = GameTitle
                        else:
                            with open(temp_path + "MegaSRX\metadata\\" + str(current_CUSA) + ".png", "wb") as downloaded_file:
                                ftp.retrbinary("RETR " + icon_name, downloaded_file.write, 1024) 
                            if "CUSA" in current_CUSA:
                                Game[current_CUSA] = "Unknown"
                            else:
                                Game[current_CUSA] = "Unknown Homebrew"
                    if "external" in dir:
                        #Get back to root directory
                        ftp.set_debuglevel(0)
                        ftp.connect(IP, int(Port))
                        ftp.login("", "")
                        ftp.cwd(dir)
                    else:
                        ftp.set_debuglevel(0)
                        ftp.connect(IP, int(Port))
                        ftp.login("", "")
                        ftp.cwd(working_dir)
                counter += 1
            
        for i in range(51, 100):
            self.CacheBar.setProperty("value", i)
            time.sleep(0.01)
        self.OpenWindow("GameIcon")

    def OpenWindow(self, WinType):
        if WinType == "GameIcon":
            global IP, Port, Game
            IPortWindow.hide()
            self.window = QtWidgets.QWidget()
            self.ui = ChangeIcon.Ui_ChangeIconWindow()
            self.ui.setupUi(self.window, IP, Port, Game, self.userFont, self.userIPath, self.userDPath, self.userHB, all_CUSA_ex)
            self.window.show()
        else:
            IPortWindow.hide()
            self.window = QtWidgets.QWidget()
            self.ui = ProfileIcon.Ui_ProfileIconWin()
            self.ui.setupUi(self.window, self.userID, IP, Port)
            self.window.show()

if __name__ == "__main__":
    print("OfficialAhmed0")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IPortWindow = QtWidgets.QMainWindow()
    ui = Ui_IPortWindow()
    ui.setupUi(IPortWindow)
    IPortWindow.show()
    sys.exit(app.exec_())
