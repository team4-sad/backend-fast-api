import re
import sqlite3
from typing import List, Tuple, Optional


class SQLiteDatabase:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._connection = None
        self._cursor = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self) -> None:
        self._connection = sqlite3.connect(self.db_path)
        self._cursor = self._connection.cursor()

    def close(self) -> None:
        if self._connection:
            self._connection.close()

    def table_exists(self, table_name: str) -> bool:
        try:
            query = """
                SELECT count(*) FROM sqlite_master 
                WHERE type='table' AND name=?
            """
            self._cursor.execute(query, (table_name,))
            result = self._cursor.fetchone()
            return result[0] == 1
        except sqlite3.Error as e:
            print(f"Ошибка проверки существования таблицы: {e}")
            return False

    def execute_script(self, script: str) -> None:
        self._cursor.executescript(script)
        self._connection.commit()

    def execute_query(self, query: str, params: Tuple = ()) -> None:
        self._cursor.execute(query, params)
        self._connection.commit()

    def fetch_all(self, query: str, params: Tuple = ()) -> List[Tuple]:
        self._cursor.execute(query, params)
        return self._cursor.fetchall()

    def fetch_one(self, query: str, params: Tuple = ()) -> Optional[Tuple]:
        self._cursor.execute(query, params)
        return self._cursor.fetchone()

    def insert(self, table_name: str, data: dict) -> None:
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(data.values()))

    def update(self, table_name: str, data: dict, condition: str) -> None:
        set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.execute_query(query, tuple(data.values()))

    def delete(self, table_name: str, condition: str) -> None:
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)

    def select_all(self, table_name: str, columns: str = "*") -> List[Tuple]:
        query = f"SELECT {columns} FROM {table_name}"
        return self.fetch_all(query)

    def select_where(self, table_name: str, condition: str, columns: str = "*") -> List[Tuple]:
        query = f"SELECT {columns} FROM {table_name} WHERE {condition}"
        return self.fetch_all(query)


