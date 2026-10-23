from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

print("=== PENGUJIAN BUKU MODEL ===")
buku_model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("\n[+] Menambahkan data buku...")
buku_model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)

# 2. Menguji fungsi Update (mengubah data buku berdasarkan id)
print("\n[*] Mengubah data buku...")
buku_model.update_buku(1, "Pemrograman Python Lanjutan", "Guido van Rossum", 2024)

# 3. Menguji fungsi Delete (menghapus data buku berdasarkan id - aktifkan jika ingin diuji)
# print("\n[-] Menghapus data buku...")
# buku_model.delete_buku(1)

# 4. Menguji fungsi Read (menampilkan daftar buku terkini)
print("\n=== Daftar Buku Terkini ===")
daftar_buku = buku_model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


print("\n=== PENGUJIAN ANGGOTA MODEL ===")
anggota_model = AnggotaModel()

# 1. Menguji fungsi Create Anggota
print("\n[+] Menambahkan data anggota...")
anggota_model.create_anggota("Aya", "Palu")

# 2. Menguji fungsi Read Anggota
print("\n=== Daftar Anggota Terkini ===")
daftar_anggota = anggota_model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")