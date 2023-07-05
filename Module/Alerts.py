from PyQt5.QtWidgets import QMessageBox

class Main:

    def __init__(self, translation:str, language:str) -> None:
        super().__init__()

        self.translated_content: dict = translation.get_translation(language, "Alerts")


    def display(self, window_title:str, description:str) -> None:
        """
            Display a widget(window) as an alert with useful information of an issue
        """

        msg = ""

        match description:

            case "About":
                msg = f"{self.translated_content.get('About')}.\n\n{self.translated_content.get('Thanks')}"

            case "db success":
                msg = self.translated_content.get("DbSuccess")

            case "CUSTOMspecial_thanks":
                msg = f"{self.translated_content.get('SpecialThanks')}:-\n@Lapy05575948\n@DefaultDNB\n\nTesters:-\n@laz305\n@maxtinion\n@_deejay87_\n@PS__TRICKS\n\n{self.translated_content.get('ThanksAll')}"

            case "CUSTOMdoneRmvCache":
                msg = self.translated_content.get("CacheRemoved")

            case "PermissionDenied":
                msg = self.translated_content.get("PermissionErr")

            case "Invalid":
                msg = f"{self.translated_content.get('InvalidCred')}."

            case "IconIssue":
                msg = f"{self.translated_content.get('InvalidCred')}."

            case "icon size":
                msg = f"{self.translated_content.get('SmallSize')} (440x440)."

            case "disconnected":
                msg = f"{self.translated_content.get('Disconnected')}."

            case "invalid_ip_port":
                msg = f"{self.translated_content.get('InvalidInput')}."

            case "are_you_sure":
                msg = f"{self.translated_content.get('IsPS4')}."

            case "timeout":
                msg = f"{self.translated_content.get('TimeOut')}."

            case "connection_refused":
                msg = f"{self.translated_content.get('TimeOut')}."

            case "incompleteProcess":
                msg = f"{self.translated_content.get('IncompleteProcess')}."

            case _:
                msg = f"{description}."
            
        QMessageBox.warning(None, f"{window_title.upper()}", f"{msg}")


    def alert(self, title:str, message:str, question=True) -> bool:
        """
            Render message box window for confirmation/Information
        """

        msg_window = QMessageBox()

        icon = QMessageBox.Question
        buttons = QMessageBox.Yes | QMessageBox.No
        default_btn = QMessageBox.No

        if not question:
            icon = QMessageBox.Information
            buttons = QMessageBox.Yes
            default_btn = QMessageBox.Yes

        msg_window.setIcon(icon)
        msg_window.setWindowTitle(title)
        msg_window.setText(message)
        msg_window.setStandardButtons(buttons)
        msg_window.setDefaultButton(default_btn)

        if msg_window.exec_() == QMessageBox.Yes:
            return True
        
        return False
