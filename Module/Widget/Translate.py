import json

class Translate:
    def __init__(self, lang_path) -> None:
        self.language_path = lang_path


    def get_supported_languages(self) -> dict:
        """ Fetch supported languages from the English json """

        with open(f"{self.language_path}English.json") as file:
            return json.load(file).get("Languages")

    
    def get_translation(self, lang:str, data_to_fetch:str) -> dict:
        """ Get info from tranlated json files. (lang):represent the json name to fetch data from """

        file = open(f"{self.language_path}{lang}.json", encoding="utf-8")
        return json.load(file).get(data_to_fetch)

