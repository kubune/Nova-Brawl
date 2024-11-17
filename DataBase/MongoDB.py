import datetime
from DataBase.MongoUtils import MongoUtils
from Logic.Player import Player

class MongoDB:
    def __init__(self):
        self.players = MongoUtils("players.sqlite")
        self.clubs = MongoUtils("clubs.sqlite")

        self.data = {
            'Name': 'Guest',
            'NameSet': False,
            'Gems': Player.gems,
            'Trophies': Player.trophies,
            'Tickets': Player.tickets,
            'Resources': Player.resources,
            'TokenDoubler': 0,
            'HighestTrophies': Player.high_trophies,
            'HomeBrawler': 0,
            'TrophyRoadReward': 300,
            'ExperiencePoints': Player.exp_points,
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': Player.brawlers_unlocked,
            'BrawlersTrophies': Player.brawlers_trophies,
            'BrawlersHighestTrophies': Player.brawlers_high_trophies,
            'BrawlersLevel': Player.brawlers_level,
            'BrawlersPowerPoints': Player.brawlers_powerpoints,
            'UnlockedSkins': Player.unlocked_skins,
            'SelectedSkins': Player.selected_skins,
            'SelectedBrawler': 0,
            'Region': Player.region,
            'SupportedContentCreator': "Nova Brawl",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
            'BrawlPassActivated': False,
            'WelcomeMessageViewed': False,
            'ClubID': 0,
            'ClubRole': 1,
            'TimeStamp': str(datetime.datetime.now()),
        }

    def create_player_account(self, id, token):
        auth = {
            'ID': id,
            'Token': token,
        }
        auth.update(self.data)
        self.players.insert_data("Players", auth)

    def load_player_account(self, token):
        result = self.players.fetch_one("Players", {"Token": token})
        if result:
            return result
        return None

    def update_player_account(self, token, updates):
        self.players.update_data("Players", {"Token": token}, updates)

    def delete_player_account(self, token):
        self.players.delete_data("Players", {"Token": token})

    def create_club(self, id, data):
        data["ID"] = id
        self.clubs.insert_data("Clubs", data)

    def load_club(self, id):
        return self.clubs.fetch_one("Clubs", {"ID": id})

    def update_club(self, id, updates):
        self.clubs.update_data("Clubs", {"ID": id}, updates)

    def delete_club(self, id):
        self.clubs.delete_data("Clubs", {"ID": id})

    def close(self):
        self.players.close_connection()
        self.clubs.close_connection()
