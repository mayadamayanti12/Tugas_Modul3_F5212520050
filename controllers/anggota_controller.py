from tkinter import messagebox

class AnggotaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Pasang fungsi tombol simpan
        self.view.btn_simpan.config(command=self.simpan_anggota)
        
        # Ambil data asli dari MySQL Laragon saat dibuka
        self.load_data()

    def load_data(self):
        # Bersihkan tabel GUI dulu
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        try:
            # Mengambil 7 data asli yang sudah kamu INSERT di MySQL Laragon
            data_anggota = self.model.get_all_anggota()

            for row in data_anggota:
                if isinstance(row, dict):
                    vals = list(row.values())
                else:
                    vals = row
                self.view.tree.insert("", "end", values=vals)
        except Exception as e:
            messagebox.showerror("Error Load Data", f"Gagal mengambil data dari MySQL:\n{e}")

    def simpan_anggota(self):
        nama = self.view.ent_nama.get().strip()
        alamat = self.view.txt_alamat.get("1.0", "end-1c").strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Nama Anggota dan Alamat harus diisi!")
            return

        try:
            self.model.add_anggota(nama, alamat)
            self.load_data()
            self.view.clear_inputs()
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan ke database!")
        except Exception as e:
            messagebox.showerror("Error Database", f"Gagal menyimpan data:\n{e}")