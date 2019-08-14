#for connection through FTP
from ftplib import FTP
import os, sys
import time
#for resizing images
from PIL import Image
import PIL

ftp = FTP()
working_dir = "user/appmeta"
img_dir = str(os.getcwd()) + "\\" + "Uploadit\\"

class settings(): #Connecting to PS4
    IP = ""    
    Port = ""
    
    with open("PS4 IP.txt", "r") as PS4_IP_file:
        lines = PS4_IP_file.readlines()
        
        for check in lines[0][1:-25]:
            if check.isdigit() or check == ".":
                IP += check
            else:
                continue
            
        for check in lines[1][1:-25]:
            if check.isdigit():
                Port += check    
            else:
                continue

def connect(IP, Port): #Connect through FTP 
    
    ftp.set_debuglevel(2)
    ftp.connect(IP, Port)
    ftp.login("", "")
    ftp.cwd(working_dir)

def Get_CUSA_from_PS4():
    directories = []
    ftp.retrlines("LIST ", directories.append)#Get all dir from the server and append them
    """create a file & copy, paste all them directories within that file"""
    all_directories_in_system = open("directories in system.dat", "w+")
    for line in directories:
        all_directories_in_system.write(line + "\n")#Copy and paste in file
    all_directories_in_system = open("directories in system.dat", "r")#Read file
    all_lines = all_directories_in_system.readlines()
    
    """Create a file and print only lines that has the word CUSA"""
    directories_with_CUSA = open("CUSA directories.dat", "w+")
    for CUSA_lines in all_lines:
        if "C" + "U" + "S" + "A" in CUSA_lines:
            directories_with_CUSA.write(CUSA_lines)
        else:
            pass
    
    """finally taking only CUSAxxxx from each line from the file CUSA directories and write them on new file named all Games.dat """
    all_CUSA = open("all Games.dat", "w+")
    directories_with_CUSA = open("CUSA directories.dat", "r")
    lines = directories_with_CUSA.readlines()
    for line in lines:
        index_C = line.index("C")
        only_CUSA = line[index_C:-1]
        all_CUSA.write(only_CUSA + "\n")
    
    """Count how many games in the system by counting CUSA titles"""
    all_CUSA = open("all Games.dat", "r")
    CUSA_lines = all_CUSA.readlines()
    total_CUSA = len(CUSA_lines) - 1 #return number of lines without the last one since it's empty
    
    directories_with_CUSA.close()
    all_directories_in_system.close()
    return total_CUSA

def gameSearch():
    Title = str(input("""Give me your Game title and let me do the magic for you 
        [exp: god of war]: """)).strip()
        
    print("""
    This might take few minutes or even seconds depends on how
    many games you have... 
    Searching 20 games sometimes up to 35 games per second """)    
    time.sleep(9)
    
    return Title

def check_each_CUSA_file(title):
    title = title.rstrip()
    
    file = open("all Games.dat", "r")
    games = file.readlines()
    
    next_game = 0
    file_name = "pronunciation.xml"
    CUSA = ""
        
    while next_game < len(games) :
        #Check the files in each game directory
        ftp.cwd(games[next_game][0:-1])
        CUSA = games[next_game][0:-1]
            
        with open("files_in_dir.dat", "w+", encoding="utf8") as files_in_dir:
            ftp.retrlines("LIST", files_in_dir.write)
            
            print("""Created by : @OfficialAhmed0""")
        
        with open("files_in_dir.dat", "r", encoding="utf8") as files_in_dir:
            content_in_file = files_in_dir.read()
            if file_name in content_in_file: #If pronunciation.xml found 
                
                with open(file_name, "wb") as downloaded_file: #Download it
                    ftp.retrbinary("RETR " + file_name, downloaded_file.write, 1024) #copy everything in downloaded file                    
                print("Created by : @OfficialAhmed0")
                with open(file_name, "r", encoding="utf8") as file: #Read Downloaded ponunciation.xml file
                    with open("Possible game title.dat", "w+", encoding="utf8") as game_titles_file: #Create temp file
                        for each_line in file: #Check for <text> which is 100% will be the title of the game
                            if "text" in each_line: #It's there copy it to temp file
                                game_titles_file.write(each_line)
                            else: #it's not there just ignore it and go to next line
                                pass
                with open("Possible game title.dat", "r", encoding="utf8") as game_titles_file:
                    check = game_titles_file.read()
                    
                    possible_titles = []
                    def caps(x): #Change the way capitalization look
                        a = x.lower()   #All letters are lowerCase
                        b = x.upper()    #All letters are upperCase
                        c = x.title()        #All first letters are upperCase only
                        d = x.capitalize()  #first letter of first word is upperCase only
                        e = x                      #original letters the user put
                        
                        total_words = x.split() #Count words
                        if len(total_words) == 3:   #Capitalize only first and third words
                            first_word = total_words[0].title()
                            second_word = total_words[1]
                            thrid_word = total_words[2].title()
                            
                            f = first_word + " " + second_word + " " + thrid_word 
                            
                            return a,b,c,d,e,f
                        else:
                            return a,b,c,d,e
                    for characters_Cases in caps(title):
                        possible_titles.append(characters_Cases)                    
                    
                    found = False
                    
                    #Get Original game title from the downloaded pronunciation.xml 
                    from_file = open("Possible game title.dat", "r", encoding="utf8")
                    game_title_in_console = from_file.readlines()
                    lines = len(game_title_in_console)
                    
                    lower_alphabets = "abcdefghijklmnopqrstuvwxyz"
                    upper_alphabets = lower_alphabets.upper()
                    
                    for each_line in range(lines):
                        if game_title_in_console[each_line] in lower_alphabets or upper_alphabets:
                            title_from_line = game_title_in_console[each_line]
                        else:
                            print("""
                The game not in English it might be in different language 
                for now supporting only English """)
                        
                    #getting this <text display="1">God of War</text> 
                        #only get >God of War</text> and then split the rest from God of War
                    starting_index = title_from_line.index(">") + 1
                    original_title = title_from_line[starting_index : -8]
                    
                    if len(possible_titles) == 4:
                        if possible_titles[0] in check or possible_titles[1] in check or possible_titles[2] in check or possible_titles[3] in check:
                            print("")
                            print("Found [" + title + "] as [" + original_title + "] in your system") 
                            found = True
                            break
                    if len(possible_titles) == 5: 
                        if possible_titles[0] in check or possible_titles[1] in check or possible_titles[2] in check or possible_titles[3] in check or possible_titles[4] in check:
                            print("")
                            print("Found [" + title + "] as [" + original_title + "] in your system") 
                            found = True
                            break
                    if len(possible_titles) == 6: 
                        if possible_titles[0] in check or possible_titles[1] in check or possible_titles[2] in check or possible_titles[3] in check or possible_titles[4] in check or possible_titles[5] in check:
                            print("")
                            print("Found [" + title + "] as [" + original_title + "] in your system") 
                            found = True
                            break                            
                        else:
                            pass
                next_game += 1  #Go to next game  
            else: #If pronunciation.xml isn't found
                next_game += 1
        connect(settings.IP ,int(settings.Port)) #Going back to root of the system
    
    if found == True:
        print(original_title + " = " + CUSA)
        
    if found == False:
        print("Sorry cannot find [" + title + "] in your system")
        check_each_CUSA_file(gameSearch())  
        
    return found    
    
def resize_and_duplicate(IconName):
    try:
        Icon_dir = img_dir + str(IconName)
        
        """ 
        For icon0 type images
        """            
        picture = Image.open(Icon_dir) 
        size = picture.size
        resize = None
        
        if size[0] == 512 and size[1] == 512:
            resize = picture
        if size[0] < 512 or size[1] < 512:
            print("The Image is smaller than (512x512)")
        else:
            resize = picture.resize((512, 512), PIL.Image.ANTIALIAS)           
        
        print(""" 
    Please wait while I resize the images...""")
        time.sleep(2)
        with open("files_in_dir.dat", "r", encoding="utf8") as files_in_dir_4_pics:
            content_in_file = files_in_dir_4_pics.read() 
                    
            files = []
            
            if "icon0.png" in content_in_file:
                resize.save(img_dir + "icon0.png")
                files.append("icon0.png")
            if "icon0.dds" in content_in_file:
                resize.save(img_dir + "icon00.png")     
                os.rename(img_dir + "icon00.png", img_dir + "icon0.dds")
                files.append("icon0.dds")
                
            for through_20 in range(1, 21): 
                if through_20 <= 9:
                    search_png = ("icon0_0" + str(through_20) + ".png")
                    search_dds = ("icon0_0" + str(through_20) + ".dds")
                    
                    copy_for_dds = ("icon0_0" + str(through_20) + ".jpeg")
                    
                    if search_png in content_in_file:
                        resize.save(img_dir + search_png)               
                        files.append(search_png)
                        
                    if search_dds in content_in_file:
                        resize.save(img_dir + copy_for_dds)   
                        os.rename(img_dir + copy_for_dds, img_dir + search_dds)
                        files.append(search_dds)
                        
                else:
                    search_png = ("icon0_" + str(through_20) + ".png")
                    search_dds = ("icon0_" + str(through_20) + ".dds")
                    
                    copy_for_dds = ("icon0_" + str(through_20) + ".jpeg")
                    
                    search_png = ("icon0_" + str(through_20) + ".png")
                    search_dds = ("icon0_" + str(through_20) + ".dds")
                    if search_png in content_in_file:
                        resize.save(img_dir + search_png) 
                        files.append(search_png)
                        
                    if search_dds in content_in_file:
                        os.rename(img_dir + copy_for_dds, img_dir + search_dds)
                        files.append(search_dds)
                        
            print("""
    Resized Successfully 
            """)       
        pictures = open("FoundImg.dat", "w+")                
        for picture in files:
            pictures.write(picture + ",")
            
        pictures.close()                       
    except FileNotFoundError:
            print("""
    Sorry I couldn't find the image. make sure you typed the image name correctly
    with the extension and don't forget to keep it in [Uploadit] folder 
    if it doesn't exist create one >> NOTE : everything's CASE sensitive.
            """)
            
    except FileExistsError:
            print("""
    SORRY I couldn't create a file when that file already exists please delete all pictures
    in the [Uploadit] file except the icon you want to upload as well as the image and try again. 
            """)                 
            resize_and_duplicate(input("""
    Give me the picture name you want to upload for the 
    >>> Icon <<< with it's format [exp: test.png]: """) )            

def upload():
    try:
        with open("FoundImg.dat", "r", encoding="utf8") as pictures:
            read_pictures = pictures.read()[0:-1]
            pic = read_pictures.split(",")
            print("""
    I am Uploading...
            """)
            for i in pic:
                save_file = open(img_dir + str(i), "rb")
                ftp.storbinary("STOR " + str(i), save_file,1024)
            print("""
    All Images uploaded successfully .
    Some games require system restart to show up correctly, 
    and sometimes it takes minutes to be changed.
    Restart your PS4. See you next time 
    @OfficialAhmed0
            """)
    except:
        print("DEV_ERROR: " + str(sys.exc_info()[0]))     
            
           # >>> Delete all files <<<<
    try:
        os.remove("directories in system.dat")
        os.remove("CUSA directories.dat")
        os.remove("pronunciation.xml")
        os.remove("all Games.dat")
        os.remove("CUSA_ID.dat")
        os.remove("files_in_dir.dat")
        os.remove("FoundImg.dat")
        os.remove("Possible game title.dat")
    except:
        pass
    
    time.sleep(25) #Before ShutDown
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>
        
if settings.IP == "...":  
    print("<<<  Please Put your PS4 IP in [PS4 IP.txt] file. turns off in 20sec  >>>")
    time.sleep(10)
    
else:
    print("""
    Connecting to your PS4 system... 
    """)
    time.sleep(2)
    
    try:
        connect(settings.IP ,int(settings.Port)) #<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        time.sleep(3)
        print("""
    Connected successfully!
        """)
        time.sleep(3)
        
        print("""
    Reading your games...
        """)
        time.sleep(5)
        Get_CUSA_from_PS4() #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        print("""
##### Please DO NOT include anything in the title other than the alphabets 
##### [ Exp: (the sims 4) ------> (the sims) or even (the sims four) ]
##### [ Exp: (Grand Theft auto : san andreas) ------> (grand theft auto) 
##### if you have more than one title matchs (grand theft auto) then be more
##### specific (grand theft auto san andreas) without (:)]
        """)
        time.sleep(2)
        
        check_each_CUSA_file(gameSearch()) #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<
        
        time.sleep(5)
        resize_and_duplicate(input("""
            Give me the picture name you want to upload for the 
            >>> Icon <<< 
            with it's format [exp: test.png]: """))  
        
        upload() #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    except TimeoutError:                    
        print("""
        PS4 didn't respond
        >> Make sure you're connected to the same Internet connection <<
        >> Make sure you entered the right IP/port <<  
        """)
        time.sleep(10)
        
    except OSError:
        print("""
        UnknownError: Possible solutions 
        >> Make sure you're connected to the same Internet connection <<
        >> Make sure you entered the right IP/port <<
        >> Try to change name of the image you want to upload << 
        DEV_ERROR_""" + str(sys.exc_info()[0]))
        time.sleep(20)
        
    except:
        print("""UnknownError : Please read errors file to see possible solutions
        """ + "_DevError: " + str(sys.exc_info()[0]))
        
        time.sleep(20)