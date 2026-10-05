import sqlite3
import hashlib
import os


class Database:

    def __init__(self, db_name="study_manager.db"):
        self.db_name = db_name
        self.init_db()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                full_name TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, username, password):
        conn = self.connect()
        cursor = conn.cursor()

        hashed_password = self.hash_password(password)

        cursor.execute("""
            SELECT id, username, full_name
            FROM users
            WHERE username = ? AND password = ?
        """, (username, hashed_password))

        user = cursor.fetchone()
        conn.close()

        if user:
            return {
                "id": user[0],
                "username": user[1],
                "full_name": user[2]
            }

        return None

    def create_user(self, username, password, full_name):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            hashed_password = self.hash_password(password)

            cursor.execute("""
                INSERT INTO users (username, password, full_name)
                VALUES (?, ?, ?)
            """, (username, hashed_password, full_name))

            conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False

        finally:
            conn.close()