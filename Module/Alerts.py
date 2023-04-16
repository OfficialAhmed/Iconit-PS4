from environment import Common

class Main(Common):
    def  __init__(self) -> None:
        super().__init__()
        self.translated_content: dict = self.translation.get_translation(self.language, "Alerts")

        self.copyright = f"\nhttps://twitter.com/OfficialAhmed0\n {self.translated_content.get('Thanks')}"

    def alert(self, type:str) -> None:
        match type:
            case "About":
                msg = f"{self.translated_content.get('About')}.\n\n{self.translated_content.get('AppVer')} v{self.app_version} [{self.app_release_date}]\n {self.translated_content.get('Thanks')}"
            case "db success":
                msg = self.translated_content.get("DbSuccess")
            case "CUSTOMspecial_thanks":
                msg = f"{self.translated_content.get('SpecialThanks')}:-\n@Lapy05575948\n\nTesters:-\n@laz305\n@maxtinion\n@_deejay87_\n@PS__TRICKS\n\n{self.translated_content.get('ThanksAll')}"
            case "CUSTOMdoneRmvCache":
                msg = self.translated_content.get("CacheRemoved")
            case "PermissionDenied":
                msg = self.translated_content.get("PermissionErr")
            case "Invalid":
                msg = f"{self.translated_content.get('InvalidCred')}.\n{self.copyright}"
            case "IconIssue":
                msg = f"{self.translated_content.get('InvalidCred')}.\n{self.copyright}"
            case "icon size":
                msg = f"{self.translated_content.get('SmallSize')} (440x440).\n{self.copyright}"
            case "disconnected":
                msg = f"{self.translated_content.get('Disconnected')}.\n{self.copyright}"
            case "invalid_ip_port":
                msg = f"{self.translated_content.get('InvalidInput')}.\n{self.copyright}"
            case "are_you_sure":
                msg = f"{self.translated_content.get('IsPS4')}.\n{self.copyright}"
            case "timeout":
                msg = f"{self.translated_content.get('TimeOut')}.\n{self.copyright}"
            case "connection_refused":
                msg = f"{self.translated_content.get('TimeOut')}.\n{self.copyright}"
            case _:
                msg = f"{type}. \n{self.copyright}"
            
        self.Message.setPlainText(msg)