from environment import Common

class Main(Common):
    def  __init__(self) -> None:
        super().__init__()

    def alert(self, type):
        if type == "About":
            self.Message.setPlainText(
                "Iconit is an automated Windows application for jailbroken PS4 consoles to change xmb icons and profile avatars with the help of FTP payload. Do you like what you see? Please consider donating \n"
                "\nApp version v"
                + self.get_update_version()
                + "released in "
                + self.get_update_release_date()
                + "\n"
                "Thanks for using Iconit"
            )

        elif type == "CUSTOMspecial_thanks":
            self.Message.setPlainText(
                "Special Thanks:-\n@Lapy05575948\n\nTesters:-\n@laz305\n@maxtinion\n@_deejay87_\n@PS__TRICKS\n\nThanks to all the devs in the scene who made this possible",
            )
        elif type == "CUSTOMdoneRmvCache":
            self.Message.setPlainText(
                "Cached icons has been removed.",
            )
        elif type == "PermissionDenied":
            self.Message.setPlainText(
                "Error Iconit needs admin permission to perform the task. Rerun as administrator",
            )

        elif type == "Invalid":
            self.Message.setPlainText(
                "Invalid IP or Port (Alphabets not allowed).\n" + self.copyright
            )

        elif type == "IconIssue":
            self.Message.setPlainText(
                "Invalid IP or Port (Alphabets not allowed).\n" + self.copyright
            )

        elif type == "Invalid icon size":
            self.Message.setPlainText(
                "Invalid icon size 'too small'. Minimum size required (440x440).\n"
                    + self.copyright
            )
        elif type == "disconnected":
            self.Message.setPlainText(
                "Disconnected from PS4. Re-enable FTP payload.\n" + self.copyright
            )

        elif type == "Magick image not found":
            self.Message.setPlainText(
                "ImageMagick not installed in \nrequired path.\nInstall it from 'Install This' Folder\n"
                + self.copyright,
            )

        else:
            self.Message.setPlainText(
 "Error Type: " + type + ". \n" + self.copyright
            )

