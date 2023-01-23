"""
    Fetch game titles and ids from 
    https://github.com/DEFAULTDNB/DEFAULTDNB.github.io
    and store them locally as JSON
"""
from environment import Common
import requests, json

class Database(Common):
    def __init__(self) -> None:
        super().__init__()
        self.raw_data = "https://raw.githubusercontent.com/DEFAULTDNB/DEFAULTDNB.github.io/master/ps4date.db"
        self.lines = ""

    def generate_db(self) -> bool:
        if self.fetch_data():
            try:
                with open(self.database_file, "w+") as file:
                    json.dump(self.get_game_info(), file)
                return True
            except:
                return False

    def fetch_data(self) -> bool:
        try:
            self.lines = requests.get(self.raw_data).text.split("\n")
            return True
        except requests.ConnectionError:
            self.logs("Internet connection failed.", "ConnectionError")
            return False
        except Exception as e:
            self.logs("Couldn't update database.", str(e))
            return False

    def find_game_ids(self, line) -> list:
        """ return indices of CUSA/s in a line """
        return [idx for idx, _ in enumerate(line) if line[idx:idx+4] == "CUSA"]

    def get_game_info(self) -> dict:
        data = {}
        for line in self.lines:
            title = line[ : line.find("(")-1]

            for cusa_index in self.find_game_ids(line):
                cusa = line[cusa_index : cusa_index+9]
                if cusa:
                    data[cusa] = title
        return data
