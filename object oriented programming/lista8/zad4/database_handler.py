import sqlite3
import os
from base_class import DataProcessingStrategy

class SumColumnStrategy(DataProcessingStrategy):
    def process(self, data):
        total = sum(data)
        print(f"Total sum: {total}")

def get_db_data():
    db_path = "sales.db"
    first = not os.path.exists(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if first:
        cursor.execute("CREATE TABLE sales (id INTEGER PRIMARY KEY, amount INTEGER)")
        cursor.executemany("INSERT INTO sales (amount) VALUES (?)", [(100,), (200,), (300,)])
        conn.commit()

    cursor.execute("SELECT amount FROM sales")
    data = [row[0] for row in cursor.fetchall()]
    conn.close()
    return data
