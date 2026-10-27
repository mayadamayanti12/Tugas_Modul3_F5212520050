from config.database import get_db_connection

def perbaiki_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        print("Membersihkan data peminjaman yang tidak memiliki buku induk...")
        # Hapus data peminjaman yang id_buku-nya tidak ada di tabel buku
        cursor.execute("""
            DELETE FROM peminjaman 
            WHERE id_buku NOT IN (SELECT id_buku FROM buku);
        """)
        conn.commit()
        
        print("Sedang mengubah aturan database...")
        # Coba drop foreign key lama jika ada
        try:
            cursor.execute("ALTER TABLE peminjaman DROP FOREIGN KEY peminjaman_ibfk_1;")
        except:
            pass
        
        # Tambahkan kembali foreign key dengan ON DELETE CASCADE
        cursor.execute("""
            ALTER TABLE peminjaman 
            ADD CONSTRAINT peminjaman_ibfk_1 
            FOREIGN KEY (id_buku) REFERENCES buku(id_buku) 
            ON DELETE CASCADE;
        """)
        
        conn.commit()
        print("Berhasil! Aturan ON DELETE CASCADE telah diaktifkan.")
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    perbaiki_database()