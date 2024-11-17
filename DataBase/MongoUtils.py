import sqlite3
from threading import local

class MongoUtils:
    def __init__(self, db_path):
        self.db_path = db_path
        self.local = local()
        self.init_schema()

    def get_connection(self):
        if not hasattr(self.local, 'connection'):
            self.local.connection = sqlite3.connect(self.db_path)
        return self.local.connection


    def init_schema(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Players (
                ID INTEGER PRIMARY KEY,
                Token TEXT NOT NULL,
                Name TEXT DEFAULT 'Guest',
                NameSet BOOLEAN DEFAULT 0,
                Gems INTEGER DEFAULT 0,
                Trophies INTEGER DEFAULT 0,
                Tickets INTEGER DEFAULT 0,
                Resources TEXT DEFAULT '{}',
                TokenDoubler INTEGER DEFAULT 0,
                HighestTrophies INTEGER DEFAULT 0,
                HomeBrawler INTEGER DEFAULT 0,
                TrophyRoadReward INTEGER DEFAULT 300,
                ExperiencePoints INTEGER DEFAULT 0,
                ProfileIcon INTEGER DEFAULT 0,
                NameColor INTEGER DEFAULT 0,
                UnlockedBrawlers TEXT DEFAULT '{}',
                BrawlersTrophies TEXT DEFAULT '{}',
                BrawlersHighestTrophies TEXT DEFAULT '{}',
                BrawlersLevel TEXT DEFAULT '{}',
                BrawlersPowerPoints TEXT DEFAULT '{}',
                UnlockedSkins TEXT DEFAULT '{}',
                SelectedSkins TEXT DEFAULT '{}',
                SelectedBrawler INTEGER DEFAULT 0,
                Region TEXT DEFAULT '',
                SupportedContentCreator TEXT DEFAULT '',
                StarPower TEXT DEFAULT '{}',
                Gadget TEXT DEFAULT '{}',
                BrawlPassActivated BOOLEAN DEFAULT 0,
                WelcomeMessageViewed BOOLEAN DEFAULT 0,
                ClubID INTEGER DEFAULT 0,
                ClubRole INTEGER DEFAULT 1,
                TimeStamp TEXT DEFAULT ''
            )
            """)
            connection.commit()
        finally:
            cursor.close()

    def close_connection(self):
        if hasattr(self.local, 'connection'):
            self.local.connection.close()
            del self.local.connection

    def insert_data(self, table, data):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join("?" * len(data))
            values = tuple(data.values())
            cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", values)
            connection.commit()
        finally:
            cursor.close()

    def update_data(self, table, query, updates):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            set_clause = ", ".join([f"{col} = ?" for col in updates.keys()])
            values = list(updates.values()) + list(query.values())
            where_clause = " AND ".join([f"{col} = ?" for col in query.keys()])
            cursor.execute(f"UPDATE {table} SET {set_clause} WHERE {where_clause}", values)
            connection.commit()
        finally:
            cursor.close()

    def fetch_one(self, table, query):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            where_clause = " AND ".join([f"{col} = ?" for col in query.keys()])
            cursor.execute(f"SELECT * FROM {table} WHERE {where_clause}", tuple(query.values()))
            return cursor.fetchone()
        finally:
            cursor.close()

    def fetch_all(self, table, query=None):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            if query:
                where_clause = " AND ".join([f"{col} = ?" for col in query.keys()])
                cursor.execute(f"SELECT * FROM {table} WHERE {where_clause}", tuple(query.values()))
            else:
                cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()
        finally:
            cursor.close()

    def delete_data(self, table, query):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            where_clause = " AND ".join([f"{col} = ?" for col in query.keys()])
            cursor.execute(f"DELETE FROM {table} WHERE {where_clause}", tuple(query.values()))
            connection.commit()
        finally:
            cursor.close()
