import json
import datetime
from DataBase.MongoUtils import MongoUtils
from Logic.Player import Player
from Utils.Helpers import Helpers


class MongoDB:
    def __init__(self, db_path):
        self.utils = MongoUtils(db_path)
        self.player = Player

        self.utils.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Players (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Token TEXT UNIQUE NOT NULL,
                Data TEXT
            )
        ''')
        self.utils.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clubs (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Data TEXT
            )
        ''')
        self.utils.conn.commit()

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
            'TrophyRoadReward': 1,
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
            'SupportedContentCreator': "Classic Brawl",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
            'BrawlPassActivated': False,
            'WelcomeMessageViewed': False,
            'ClubID': 0,
            'ClubRole': 1,
            'TimeStamp': str(datetime.datetime.now())
        }

        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': '',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': []
        }

    def create_player_account(self, id, token):
        auth = {'ID': id, 'Token': token, 'Data': json.dumps(self.data)}
        self.utils.insert_data('Players', auth)

    def load_player_account(self, id, token):
        result = self.utils.load_document('Players', {'Token': token})
        if result:
            player_data = json.loads(result[2])
            for key in self.data:
                if key not in player_data:
                    player_data[key] = self.data[key]
            return player_data

    def update_player_account(self, token, item, value):
        result = self.utils.load_document('Players', {'Token': token})
        if result:
            player_data = json.loads(result[2])
            player_data[item] = value
            self.utils.update_document('Players', {'Token': token}, 'Data', json.dumps(player_data))

    def delete_player(self, token):
        self.utils.delete_document('Players', {'Token': token})

    def create_club(self, id, data):
        club = {'ID': id, 'Data': json.dumps(data)}
        self.utils.insert_data('Clubs', club)

    def load_club(self, id):
        result = self.utils.load_document('Clubs', {'ID': id})
        return json.loads(result[1]) if result else None

    def update_club(self, id, item, value):
        result = self.utils.load_document('Clubs', {'ID': id})
        if result:
            club_data = json.loads(result[1])
            club_data[item] = value
            self.utils.update_document('Clubs', {'ID': id}, 'Data', json.dumps(club_data))

    def delete_club(self, id):
        self.utils.delete_document('Clubs', {'ID': id})

    def close(self):
        self.utils.close()
