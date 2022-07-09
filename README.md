# Iconit
Latest version 4.72 (Jan 5, 2022)
No longer ftp client needed to change PS4 games' icon this tool will do it for you (everything Automated). PS4 FTP required (PS4 fw "1.74-9.00").
Download the executable version (exe) down below and the icons from https://all-exhost.github.io/icon%20downloader.html

# Download
**Latest Iconit version**
https://github.com/OfficialAhmed/Iconit-PS4/releases

# About

This application is much convenient than uploading the icons manually, it automates the following

* Game ID `CUSA` to game title conversion

* Resize images to the required size `512x512` 

* Icon duplication

* Backup original icons

* Locate game folder on console


# v4.72 Changelog

* Ability to change any Homebrew (All homebrews will be detected format:LAPYxxxxx 4-letter prefix followed by 5-number suffix)  

* Ability to change System icons (ATTENTION: This will require extra permissions. Make sure to run FTP with Full R/W mode, Lapy Xplorer offer an option to allow FTP in "Danger mode" => Full R/W permissions by pressing (L2+Triangle). SomeTimes Xplorer seem to be allowing Full R/W but its not for some reason, try removing game data for Xplorer and retry) 

* Fixed major bug with caching (used to overwrite the cache meaning old cache is useless. Note: first time running the application might take awhile and may freeze wait for it. The 2nd time you run it would be ~99% faster)

* Game/Pic fully compatible with "GoldHen FTP" (The whole process rely on one connection now)

* Auto backup changed icons (stored in "Your Backup" folder)

* More accurate Game Titles (Less abbreviations shown as the Game title)

* Overall performance ++ (Implemented low-level Threading/multiprocessing)

* Better caching performance (used to Write/Read some data from/to Hard Disk now uses the RAM instead)

* Progress bar now shows realtime progression (used to be static and hard coded)

* Caching size reduced significantly

* Brand new User interface when connecting to PS4 (Modern design less memory usage)

* Fixed when using AvatarChange Error (No such file or directory: Pref.ini)

* Fixed noob algorithms to approach different problems (now the code is waaaaay much easier to read)

* Fixed when renaming PSN activated account Deactivates it (Recommended to use it on offline accounts. Use it on online accounts on your own risk this might need more attention as I don't have PSN activated accounts I can't test it, so I can't guarantee for activated accounts SORRY!)

# v4.65 Changelog

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


# Older versions

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

# To do list
- [ ] Render Game ID `CUSAXXXXX` text on icon 
- [ ] Multiple icon change 
- [ ] Apply `PSD` cover on icons
- [ ] Performance++ : save game title as cache on game folder 


# Contribution
Do not hesitate to send me new suggestions and ideas for the application.
https://twitter.com/OfficialAhmed0

# Pictures 
![iconit v4.05](https://img.techpowerup.org/200830/1.png)
![Image of Game icon using iconit v4.05](https://img.techpowerup.org/200830/2.png)
![Profile avatar using iconit v4.05](https://img.techpowerup.org/200830/3.png)

