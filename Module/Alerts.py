from environment import Common

class Main(Common):
    def  __init__(self) -> None:
        super().__init__()
        self.copyright = "\nhttps://twitter.com/OfficialAhmed0\nThank you for using Iconit"

    def alert(self, type:str) -> None:
        if type == "About":
            msg = f"Iconit is an automated Windows application for jailbroken PS4 consoles to change xmb icons and profile avatars with the help of FTP payload.\n\nApp version v{self.app_version} [{self.app_release_date}]\n Thank you for using Iconit"
        elif type == "db success":
            msg = f"Successfully downloaded database."
        elif type == "db fail":
            msg = f"Something went wrong. Cannot download/update the database. Please Read the logs.txt and contact the developer."
        elif type == "CUSTOMspecial_thanks":
            msg = "Special Thanks:-\n@Lapy05575948\n\nTesters:-\n@laz305\n@maxtinion\n@_deejay87_\n@PS__TRICKS\n\nThanks to all the devs in the scene who made this possible"
        elif type == "CUSTOMdoneRmvCache":
            msg = "Cached icons have been removed. It'll take time to cache next time you connect to the PS4"
        elif type == "PermissionDenied":
            msg = "Error Iconit needs admin permission to perform the task. Rerun as administrator"
        elif type == "Invalid":
            msg = f"Invalid IP or Port (Alphabets not allowed).\n{self.copyright}"
        elif type == "IconIssue":
            msg = f"Invalid IP or Port (Alphabets not allowed).\n{self.copyright}"
        elif type == "Invalid icon size":
            msg = f"Invalid icon size 'too small'. Minimum size required (440x440).\n{self.copyright}"
        elif type == "disconnected":
            msg = f"Disconnected from PS4. Re-enable FTP payload.\n{self.copyright}"
        elif type == "Magick image not found":
            msg = f"ImageMagick not installed in the required path. Reinstall it to the default path please\n{self.copyright}"
        else:
            msg = f"Error Type:{type}. \n{self.copyright}"
            
        self.Message.setPlainText(msg)