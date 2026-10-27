from config.database import get_db_connection

class BukuModel:
    def __init__(self):
        pass

    def get_all_buku(self):
        """Mengambil seluruh data buku dari database"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM buku"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def add_buku(self, judul, penulis, tahun_terbit):
        """Menambahkan buku baru ke database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        cursor.execute(query, (judul, penulis, tahun_terbit))
        conn.commit()
        cursor.close()
        conn.close()

    def create_buku(self, judul, penulis, tahun_terbit):
        """Alias method untuk add_buku agar mendukung runner testing"""
        return self.add_buku(judul, penulis, tahun_terbit)

    def delete_buku(self, id_buku):
        """Menghapus data buku berdasarkan ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Gunakan 'id_buku' atau 'id' sesuai dengan nama kolom primary key di database Anda
        query = "DELETE FROM buku WHERE id_buku = %s"
        
        cursor.execute(query, (id_buku,))
        conn.commit()
        cursor.close()
        conn.close()