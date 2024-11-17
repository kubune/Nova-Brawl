import sqlite3
import json

class MongoUtils:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def insert_data(self, table, data):
        placeholders = ', '.join(['?'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(json.dumps(v) if isinstance(v, (dict, list)) else v for v in data.values())
        self.cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", values)
        self.conn.commit()

    def update_document(self, table, query, item, value):
        query_column, query_value = list(query.items())[0]
        value = json.dumps(value) if isinstance(value, (dict, list)) else value
        self.cursor.execute(f"UPDATE {table} SET {item} = ? WHERE {query_column} = ?", (value, query_value))
        self.conn.commit()

    def delete_document(self, table, query):
        query_column, query_value = list(query.items())[0]
        self.cursor.execute(f"DELETE FROM {table} WHERE {query_column} = ?", (query_value,))
        self.conn.commit()

    def load_document(self, table, query):
        query_column, query_value = list(query.items())[0]
        self.cursor.execute(f"SELECT * FROM {table} WHERE {query_column} = ?", (query_value,))
        return self.cursor.fetchone()

    def load_all_documents(self, table, query=None):
        if query:
            query_column, query_value = list(query.items())[0]
            self.cursor.execute(f"SELECT * FROM {table} WHERE {query_column} = ?", (query_value,))
        else:
            self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
