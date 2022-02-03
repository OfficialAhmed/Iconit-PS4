# Iconit
Latest version 4.65 (Dec 6, 2021)
No longer ftp client needed to change PS4 games' icon this tool will do it for you (everything Automated). Works with FTP (PS4 fw "1.74-9.00")
it's an open source you can clone the repository or download the executable version (exe) down below

# Download from here
**Iconit v4.65 (85.1Mb)**
https://github.com/OfficialAhmed/Iconit-PS4/releases/tag/v4.65


# About

This application is much convenient than uploading the images manually for many reasons :-

* This tool will take the game title and search for the equivalent CUSA title of the game from the PS4 console. You don't have to deal with CUSA of the game anymore 

* It'll resize the images for you to the required size so you don't need to use any applications whatsoever note:(for pic1 change the tool needed is included with the zip file). 

* It'll count how many icons are required for the game some games require only 1, while others require more

* This tool will connect to your PS4 system through FTP directly so you no longer need FTP client applications such as FileZilla atleast not for changing the game icons or profile avatar.

* I added a Library (https://all-exhost.github.io/icon%20downloader.html) that has Dozens of icons for you to pick from.

# Update v4.72 (WIP. Not yet compiled for the end-user)

* Ability to change all Homebrews (Note: make sure to enable HB in the settings) (4-letter prefix followed by 5-number suffix format. Exp: LAPY00000)  

* Ability to change System icons (ATTENTION: This will require extra permissions. Make sure to run FTP with Full R/W mode, as of writing this only Lapy Xplorer offer an option to allow FTP in "Danger mode" => Full R/W permissions by pressing (L2+Triangle). Only allow "Danger mode" when you need to change the system icons disable it afterwards to be in the safe side) 

* More accurate Game Titles (Less abbreviations shown as the Game title)

* Overall performance ++ (Implemented low-level Threading/multiprocessing)

* Better caching performance (used to Write/Read some data from/to Hard Disk now uses the RAM instead)

* Caching size reduced

* Fixed when renaming PSN activated account Deactivates it (Recommended to use it on offline accounts. Use it on online accounts on your own risk this might need more attention as I don't have PSN activated accounts I can't test it, so I can't guarantee for activated accounts SORRY!)

* Fixed when using AvatarChange Error (No such file or directory: Pref.ini)

* Fixed more noob algorithms (now the code is waaaaay much easier to read)

# Update v4.65

* Added Pic change (you can now change background of any game, that show up when a game launches) => full hd up to 2k dimensions only

* Avatar change now works for both (Offline & Activated accounts) Note: If you have psn games installed, this will disable the games use it on your own risk

* Avatar change works on 64-bit and 32-bit using only "32-bit ImageMagic" (used to yield 550 error for 64-bit windows)

* Added legit png to dds convertion for accurate icons (Dxt1 compression)

* Added more functions under Settings (default IP, restore default settings)

* Added shortcut key (Enter/Return) to Select a game title

* Added Tooltips to better understand each section of the application

* Added numbering along the game title in the Games List

* Added Renaming accounts (used to be visible only on application now will be visible on PS4 system)

* Added more homebrew compatibles with prefix (PKGI, FLTZ, BORC, NPXS, NPXX, PNES)

# Update v4.07

* Key shortcuts supported (Return) to click main button. (Left & Right arrows) for (Next image, Previous image respectively) 

* Multiprocessing method added for better performance

* Shrinked application size from(131mb) to(74mb)

* Fixed 550 error and other bugs

# Update v4.05

* Changed the entire UI to support 2k and 4k screen resolution

* Application window now resizable

* Fixed 505 error when changing profile avatar 

# Update v4.01

* Added new feature change profile icon "profile avatar" (Many issues fixed in later versions)

* External hdd games support.

* More homebrews are supported starting with:-
>(SSNE, MODS, LAPY, NP and more) as the Game ID.
(Make sure to enable it under Settings>>Options)

* Fixed cache bar wrong calculations.

* Fixed many bugs.

# Older versions

The tool consist of 2 files 

* The application executable 

>Iconit v4.07 (74.1Mb)(Nov 25, 2020)
https://mega.nz/file/S7h2QIQY#uSgZBu_iET1ihZBJvpTYNXcH1481cLGFg4ZNbG1DIP8

>Iconit v4.05 (131.6Mb)(Aug 30, 2020)
https://mega.nz/file/Tq4zAB7L#Vm3Cj003CDWUYZzkN5WcQJGuvvwL3f4oJVfamAIuMMI

>Iconit v4.01 (91.6Mb)
https://mega.nz/file/zu43zDiL#yIKFNKVpTwWZpY0_YID0pzf72IxE0ClHsMRaMph7Y8s

>Iconit v3.00 (53.6Mb)
https://mega.nz/file/mv4hyJya#dylV-otTZH_GMptPRafhg7kJd1T6mvARuuZvQF3VTBg

>Iconit v1.00 (31Mb)
https://mega.nz/#!nqQ3RKrD!Tgbu4mp2flfrZPx-wA9_j_MZyBae3Z5xCwf3ZV_Gcw4
________________________________________

* Images library (Optional) 

>Circlizeit (Icons package)(62Mb)
https://mega.nz/#!qrRTAA4R!vId588A9wkINXz7q3EpN62GKrIdKM0oh5c3Ge0ne-oA

# Contribution
Do not hesitate to send me new suggestions and ideas for the application.
Twitter: https://twitter.com/OfficialAhmed0

# Pictures 
![iconit v4.05](https://img.techpowerup.org/200830/1.png)
![Image of Game icon using iconit v4.05](https://img.techpowerup.org/200830/2.png)
![Profile avatar using iconit v4.05](https://img.techpowerup.org/200830/3.png)

