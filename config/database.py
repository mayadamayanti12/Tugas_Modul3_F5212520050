import mysql.connector

def get_db_connection():
    """Membuat koneksi ke database MySQL"""
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='perpustakaan' # Sesuaikan dengan nama database Anda jika berbeda
    )
    return connection