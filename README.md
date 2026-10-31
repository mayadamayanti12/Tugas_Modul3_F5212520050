# Sistem Manajemen Perpustakaan

Aplikasi desktop manajemen perpustakaan berbasis Python dengan pola arsitektur
MVC (Model-View-Controller). Fitur utama:

- Login dengan hashing password SHA-256
- Otorisasi berbasis peran (admin dan anggota)
- Pengelolaan data buku dan data anggota (tambah, lihat, ubah, hapus)
- Data disimpan di database MySQL

## Struktur Direktori MVC

```
Tugas_Modul3_F5212520050/
├── config/
│   └── database.py           # Koneksi ke MySQL
├── models/
│   ├── buku_model.py         # Query data buku
│   ├── anggota_model.py      # Query data anggota
│   └── user_model.py         # Autentikasi dan registrasi user
├── views/
│   ├── buku_view.py          # Antarmuka data buku
│   ├── anggota_view.py       # Antarmuka data anggota
│   └── login_view.py         # Antarmuka login
├── controllers/
│   ├── buku_controller.py    # Logika data buku
│   ├── anggota_controller.py # Logika data anggota
│   └── auth_controller.py    # Alur login dan logout
├── tests/                    # Unit test (pytest)
├── .github/workflows/        # CI pipeline (GitHub Actions)
├── fix_database.py           # Skrip perbaikan database
├── main.py                   # Titik masuk aplikasi
└── requirements.txt          # Daftar dependensi
```

## Instalasi dan Konfigurasi Database MySQL

1. Pasang Python 3.x, Laragon, dan Git.
2. Clone repositori lalu masuk ke foldernya:
   ```
   git clone https://github.com/mayadamayanti12/Tugas_Modul3_F5212520050.git
   cd Tugas_Modul3_F5212520050
   ```
3. Buat virtual environment dan pasang dependensi:
   ```
   python -m venv env
   ./env/Scripts/activate
   pip install -r requirements.txt
   ```
4. Buka Laragon, klik **Mulai Semua** agar MySQL menyala.
5. Buka terminal MySQL (`mysql -u root -p`), lalu buat database dan tabel:
   ```sql
   CREATE DATABASE IF NOT EXISTS perpustakaan;
   USE perpustakaan;

   CREATE TABLE buku (
       id_buku INT PRIMARY KEY AUTO_INCREMENT,
       judul VARCHAR(100) NOT NULL,
       penulis VARCHAR(100) NOT NULL,
       tahun_terbit YEAR
   );

   CREATE TABLE users (
       id_user INT PRIMARY KEY AUTO_INCREMENT,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL,
       role ENUM('admin', 'anggota') NOT NULL DEFAULT 'anggota'
   );

   INSERT INTO users (username, password, role) VALUES
   ('petugas', SHA2('admin123', 256), 'admin'),
   ('mahasiswa', SHA2('user123', 256), 'anggota');
   ```
   Tabel `anggota` dibuat otomatis oleh aplikasi saat pertama kali dijalankan.
6. Koneksi database diatur di `config/database.py` (host `localhost`, user
   `root`, password kosong, database `perpustakaan`). Sesuaikan bila konfigurasi
   MySQL Anda berbeda.

## Cara Menjalankan Aplikasi

Pastikan MySQL di Laragon sudah menyala, lalu jalankan:

```
python main.py
```

Akun uji coba:

| Username  | Password | Role    | Hak akses                    |
|-----------|----------|---------|------------------------------|
| petugas   | admin123 | admin   | Tambah, ubah, hapus, lihat   |
| mahasiswa | user123  | anggota | Hanya melihat (read-only)    |

Menjalankan unit test:

```
python -m pytest -v
```

Versi `.exe` untuk Windows dapat diunduh di menu **Releases** pada halaman
repositori GitHub ini.