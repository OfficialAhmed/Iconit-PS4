""" Read-only classes """

class PS4:
    # ___________   Private PS4 constant attrs   _______________#

    __SYS_SCE = "sce_sys"
    __ICON_SIZE = (512, 512)
    __PIC_SIZE = (1920, 1080)
    __4k_ICON_SIZE = (660, 660)
    __USER_DATA = "user/data/" 
    __INT_ICONS = "user/appmeta/"
    __SYS_ICONS = "system_ex/app/"
    __EXT_ICONS = "user/appmeta/external/"
    __PRONOUNCIATION_FILE = "pronunciation.xml"

    __ICONS_BACKUP_NAME = "Backup"
    __ICON_SUPPORTED_FORMATS = "Image (*.png *.jpg *.jpeg)"

    __HASH_THEME_COLOR = {
        "red":"#e83c3c",
        "green":"#55ff00",
        "white":"#ffffff",
        "orange":"#ffaa00",
    }

    def __init__(self) -> None:
        # init the self parameter
        pass

    def __setattr__(self, __name: str, __value: any) -> None:
        raise AttributeError(f"READ-ONLY: Class 'Constant' allow getters only. Occured while trying to set [{__name}]")
        
    def get_color(self, str_color:str) -> str:
        return PS4.__HASH_THEME_COLOR[str_color]

    def get_ps4_pic_size(self) -> tuple:
        return PS4.__PIC_SIZE

    def get_ps4_icon_size(self) -> tuple:
        return PS4.__ICON_SIZE

    def get_ps4_4k_icon_size(self) -> tuple:
        return PS4.__4k_ICON_SIZE

    def get_sce_folder_name(self) -> str:
        return PS4.__SYS_SCE

    def get_system_icons_path(self) -> str:
        return PS4.__SYS_ICONS

    def get_backup_folder_name(self) -> str:
        return PS4.__ICONS_BACKUP_NAME

    def get_internal_icons_path(self) -> str:
        return PS4.__INT_ICONS

    def get_external_icons_path(self) -> str:
        return PS4.__EXT_ICONS

    def get_icon_supported_format(self) -> str:
        return PS4.__ICON_SUPPORTED_FORMATS

    def get_pronunciation_file_path(self) -> str:
        return PS4.__PRONOUNCIATION_FILE
    
    def get_user_data_path(self) -> str:
        return PS4.__USER_DATA


class PS5:
    # ___________   Private PS5 constant attrs   _______________#

    pass