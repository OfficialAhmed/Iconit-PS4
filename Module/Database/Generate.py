"""
Game_database
    Fetch game titles and ids from 
    https://github.com/DEFAULTDNB/DEFAULTDNB.github.io
    and store them locally as JSON

System_database
    Fetch apps info from online repo

    and store them locally as JSON
"""
import requests, json


class Game_database:
    def __init__(self, db_file) -> None:
        self.db_file = db_file
        self.lines = ""
        self.games = {}
        self.raw_data = "https://raw.githubusercontent.com/DEFAULTDNB/DEFAULTDNB.github.io/master/ps4date.db"


    def fetch_game_title(self, game_id) -> tuple:
        """ return the local data """
        result = None
        try:
            if not self.games: 
                self.games = json.load(open(self.db_file))

            if game_id in self.games:
                result = (True, self.games.get(game_id))
            else:
                result = (False, f"{game_id} not found in database. It'll be fetched from PS4")

        except FileNotFoundError:
            result = (False, "Fetching data from console is going to take longer. Please consider downoading the database from the settings | FileNotFoundError")
        except Exception as e:
            result = (False, f"Couldn't read database! fetching process will be slower. Consider redownloading the database from the settings | {str(e)}")
        finally:
            return result


    def save(self) -> tuple:
        fetched_data = self.fetch_data()
        if fetched_data[0] == True:
            try:
                with open(self.db_file, "w+") as file:
                    json.dump(self.get_game_id_and_title(), file)
            except: pass
        return fetched_data


    def fetch_data(self) -> tuple:
        try:
            self.lines = requests.get(self.raw_data).text.split("\n")
            return (True, )
        except requests.ConnectionError:
            return (False, "ConnectionError| Internet connection failed")
        except Exception as e:
            return (False, f"Couldn't update database| {e}")


    def find_game_ids(self, line) -> list:
        """ return indices of CUSA/s in a line """
        return [idx for idx, _ in enumerate(line) if line[idx:idx+4] == "CUSA"]


    def get_game_id_and_title(self) -> dict:
        data = {}
        for line in self.lines:
            title = line[ : line.find("(")-1]

            for cusa_index in self.find_game_ids(line):
                cusa = line[cusa_index : cusa_index+9]
                if cusa:
                    data[cusa] = title
        return data

 
class System_database:
    def __init__(self, db_file) -> None:
        self.db_file = db_file
        self.raw_data = "https://raw.githubusercontent.com/OfficialAhmed/Iconit-PS4/master/Data/Cache/Icons/metadata/system/Database.json"

    
    def save(self) -> tuple:
        fetched_data = self.fetch_data()
        if fetched_data[0] == True:
            try:
                with open(self.db_file, "w+", encoding="utf-8") as file:
                    file.write(self.database)
            except:  pass
        return fetched_data


    def fetch_data(self) -> tuple:
        try:
            self.database:str = requests.get(self.raw_data).text
            return (True, )
        except requests.ConnectionError:
            return (False, "ConnectionError| Internet connection failed")
        except Exception as e:
            return (False, f"Couldn't update database| {e}")
