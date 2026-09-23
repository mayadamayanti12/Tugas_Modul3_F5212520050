# Program Catatan Tugas Mahasiswa - Modul 3
def main():
    print("=======================================")
    print("       TRACKER TUGAS MAHASISWA         ")
    print("=======================================")
    
    nama     = input("Nama Mahasiswa : ")
    nim      = input("NIM            : ")
    matkul   = input("Mata Kuliah    : ")
    judul    = input("Judul Tugas    : ")
    deadline = input("Tenggat Waktu  : ")
    status   = input("Status         : ")
    
    print("\n---------------------------------------")
    print("          RINGKASAN TUGAS              ")
    print("---------------------------------------")
    print(f"Nama        : {nama}")
    print(f"NIM         : {nim}")
    print(f"Mata Kuliah : {matkul}")
    print(f"Judul Tugas : {judul}")
    print(f"Deadline    : {deadline}")
    print(f"Status      : {status}")
    print("=======================================")
    print("      Tugas Berhasil Dicatat!          ")

if __name__ == "__main__":
    main()