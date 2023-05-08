# Overview

_Latest `exe` version `5.06 BETA (Jan 29th, 2023)`_

_Currently working on `v5.56` mainly for performance & code factorization for `PS5 FTP` in the future_.

*Download `icons` from <https://all-exhost.github.io/Icons.html>*

*Download `masks` from <https://all-exhost.github.io/Masks.html>*

*Download `.exe` the latest windows executable version from* <https://github.com/OfficialAhmed/Iconit-PS4/releases>

## About

Pure Python implementation of an automated software to change `PS4` xmb icons, pictures and profile avatars. PS4 (5.05 - 9.00).

This application is much convenient than uploading the icons manually, it automates the following:

* Icon duplication 
* Backup original icons `icon0, icon1, ...`
* Upload and overwrite icons to the `PS4`  
* Game ID `CUSA` to game title conversion
* Image conversion `JPG, ICO, ...` to `PNG`
* Image to compressed textures conversion `PNG` to `DDS dxt1`
* Resize images to the required size `512x512`, `1920x1080`

________________________________________

## *What's new in v5*

#### _For end users:_

*  Fixed `picX_XX.png` & `picX_XX.dds` conversion
*  `Independent version` ImageMagick is no longer required
*  In the `Games List` _Game IDs_ now shown next to the game title
*  `Modes` can be changed without restarting the program
*  `Backup icons` will never be overwritten nor removed [_used to cache once then overwrite the older one_]
*  `Circular icon scrolling` when the last icon's reached, it'll begin again from the start and vice versa.
*  `Faster caching` new techniques added
*  `New option` __Download database__ for a faster caching process
*  `New Feature` you can now group a set of icons and apply a mask to them
 
#### _For developers:_
*  `Image Detection` detects all images of the form `iconX_XX` & `picX_XX`
*  `Clean up` code and file structure
*  `Buffer size` increased to ~65500 bytes
*  `Required Icons` now will be cached on PS4 connect (_Slower_)
*  `Required Icons` will be read from cache instead of FTP (_Faster_)
*  `OOP implementation` (_Faster but more memory usage_)
*  `Break GIL Limitation` implemented concurrent methods for CPU I/O bound (_Faster when lots of icons, slower otherwise_)
*  `Local database` implemented & fetched from [DEFAULTDNB](https://github.com/DEFAULTDNB/DEFAULTDNB.github.io). For game titles caching "_Read [wiki](https://github.com/OfficialAhmed/Iconit-PS4/wiki/Performance) for detailes_"
*  `Subproccess` implementation to convert `PNG` to `DDS` DXT1 compression using [DirectXTex/texconv](https://github.com/Microsoft/DirectXTex/wiki/Texconv)
________________________________________

## *Current implementation Main bugs* 
 This version isn't ready for end-users
1. Avatars option patch required

## _To do list (UPCOMING UPDATE)_

* [x] Mask a Set Of Icons `New Feature`
* [x] Group a Set Of Icons `New Feature`

* [x] Utilize 100% CPU usage `Concurrent processing`
* [x] Multiple Icon Duplication at Once - heavy R/W Bound `Threading`

* [ ] Backup/Restore cache to/from PS4 `New Feature`
* [ ] Render Game ID `CUSAXXXXX` text on icon
* [ ] Feature : User can edit displayed game title through cache file
* [ ] Feature : Read titles from xmb DB 

## _Credits_
* Special thanks to [@Lapy](https://twitter.com/Lapy05575948) for the help.
* Special thanks to [@DEFAULTDNB](https://github.com/DEFAULTDNB) AKA [@KiiWii](https://twitter.com/DefaultDNB) for the Database

    ### _Testers_:
* [@laz305](https://twitter.com/laz305)
* [@maxtinion](https://twitter.com/maxtinion)
* [@_deejay87_](https://twitter.com/_deejay87_)
* [@PS__TRICKS](https://twitter.com/PS__TRICKS)

## _Preview_
![Main_screen](Interface/view/main_screen.jpg)
![Icons_screen](Interface/view/icons_screen.jpg)

# Attention

Some antivirus detect the compiled/converted `.exe` version as **_trojan or malware_ [Win64:Evo-gen [Trj] or Trojan.Generic.horqm]** because the compiler _Pyinstaller_ used by some people to make malware but don't worry `Iconit.exe is False-positive`. If you don't trust it, you can check the commits and changes if there's any malicious code or compile the code on your own. Otherwise, you may whitelist it and continue. 
The _Pyinstaller_ devs stated it here [False-positive Pyinstaller](https://github.com/pyinstaller/pyinstaller/issues/6754)

# License
Iconit-PS4 - Copyright (C) 2019-2023 OfficialAhmed

This software is free to use, distribute and/or modify it under the terms of the [MIT License](LICENSE) (MIT)
