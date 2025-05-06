import sqlite3
import os
from base_class import DataAccessHandler

class DatabaseAccessHandler(DataAccessHandler):
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        first_time = not os.path.exists(self.db_path)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        if first_time:
            self.create_table_and_insert_data()

        print(f"Connecting with the database: {self.db_path}")

    def create_table_and_insert_data(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount INTEGER NOT NULL
            )
        ''')
        #executemany expects a sequence of sequences
        self.cursor.executemany('INSERT INTO sales (amount) VALUES (?)',
                                [(100,), (200,), (300,), (400,)]) 
        
        self.connection.commit()

    def get_data(self):
        self.cursor.execute("SELECT amount FROM sales")
        return [row[0] for row in self.cursor.fetchall()]

    def process_data(self, data):
        total = sum(data)
        print(f"Total sum: {total}")

    def disconnect(self):
        self.connection.close()
        print("Disconnecting form the database.")
