import hashlib
from config.database import get_db_connection


class UserModel:
    def __init__(self):
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def autentikasi(self, username, password):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
        cursor.execute(query, (username, self.hash_password(password)))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    def register_user(self, username, password, role="anggota"):
        if role not in ("admin", "anggota"):
            return False
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, self.hash_password(password), role))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Gagal registrasi user: {e}")
            return False