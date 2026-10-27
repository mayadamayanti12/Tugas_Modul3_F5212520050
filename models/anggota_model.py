import mysql.connector

class AnggotaModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan"
        )
        self.setup_database()

    def setup_database(self):
        cursor = self.conn.cursor()
        try:
            # Matikan foreign key sebentar untuk menghindari error relasi
            cursor.execute("SET foreign_key_checks = 0;")
            
            # Buat tabel anggota jika belum ada
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS anggota (
                    id_anggota INT AUTO_INCREMENT PRIMARY KEY,
                    nama_anggota VARCHAR(100) NOT NULL,
                    alamat TEXT NOT NULL
                )
            """)
            
            # Cek apakah datanya masih kosong, kalau kosong otomatis isi data
            cursor.execute("SELECT COUNT(*) FROM anggota")
            count = cursor.fetchone()[0]
            if count == 0:
                data_awal = [
                    ('Jungwon', 'Jakarta Selatan'),
                    ('Jay', 'Bandung'),
                    ('Jake', 'Surabaya'),
                    ('Sunghoon', 'Yogyakarta'),
                    ('Sunoo', 'Semarang'),
                    ('Ni-ki', 'Denpasar'),
                    ('Nun Qalbu Ain', 'Palu')
                ]
                cursor.executemany(
                    "INSERT INTO anggota (nama_anggota, alamat) VALUES (%s, %s)", 
                    data_awal
                )
                self.conn.commit()
                
            cursor.execute("SET foreign_key_checks = 1;")
        except Exception as e:
            print("Info Setup Database:", e)
        finally:
            cursor.close()

    def get_all_anggota(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        result = cursor.fetchall()
        cursor.close()
        return result

    def add_anggota(self, nama_anggota, alamat):
        cursor = self.conn.cursor()
        query = "INSERT INTO anggota (nama_anggota, alamat) VALUES (%s, %s)"
        cursor.execute(query, (nama_anggota, alamat))
        self.conn.commit()
        cursor.close()

    def update_anggota(self, id_anggota, nama_anggota, alamat):
        cursor = self.conn.cursor()
        query = "UPDATE anggota SET nama_anggota = %s, alamat = %s WHERE id_anggota = %s"
        cursor.execute(query, (nama_anggota, alamat, id_anggota))
        self.conn.commit()
        cursor.close()

    def delete_anggota(self, id_anggota):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SET foreign_key_checks = 0;")
            query = "DELETE FROM anggota WHERE id_anggota = %s"
            cursor.execute(query, (id_anggota,))
            cursor.execute("SET foreign_key_checks = 1;")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()