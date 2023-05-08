""" Read-only class """

class Constants:
    # ___________   Private attrs   _______________#

    __PS4_SYS_SCE = "sce_sys"
    __PS4_ICON_SIZE = (512, 512)
    __PS4_PIC_SIZE = (1920, 1080)
    __PS4_4k_ICON_SIZE = (660, 660)
    __PS4_INT_ICONS = "user/appmeta/"
    __PS4_SYS_ICONS = "system_ex/app/"
    __PS4_EXT_ICONS = "user/appmeta/external/"
    __PS4_PRONOUNCIATION_FILE = "pronunciation.xml"

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
        return Constants.__HASH_THEME_COLOR[str_color]

    def get_ps4_pic_size(self) -> tuple:
        return Constants.__PS4_PIC_SIZE

    def get_ps4_icon_size(self) -> tuple:
        return Constants.__PS4_ICON_SIZE

    def get_ps4_4k_icon_size(self) -> tuple:
        return Constants.__PS4_4k_ICON_SIZE

    def get_sce_folder_name(self) -> str:
        return Constants.__PS4_SYS_SCE

    def get_system_icons_path(self) -> str:
        return Constants.__PS4_SYS_ICONS

    def get_backup_folder_name(self) -> str:
        return Constants.__ICONS_BACKUP_NAME

    def get_internal_icons_path(self) -> str:
        return Constants.__PS4_INT_ICONS

    def get_external_icons_path(self) -> str:
        return Constants.__PS4_EXT_ICONS

    def get_icon_supported_format(self) -> str:
        return Constants.__ICON_SUPPORTED_FORMATS

    def get_pronunciation_file_path(self) -> str:
        return Constants.__PS4_PRONOUNCIATION_FILE