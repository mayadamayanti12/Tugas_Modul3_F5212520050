from tkinter import messagebox


class BukuController:
    def __init__(self, model, view, user_role="anggota"):
        self.model = model
        self.view = view
        self.user_role = user_role

        self.view.parent.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Hubungkan tombol GUI ke method controller
        self.view.btn_simpan.config(command=self.simpan_buku)
        self.view.btn_update.config(command=self.update_buku)
        self.view.btn_hapus.config(command=self.hapus_buku)
        self.view.btn_logout.config(command=self.logout)

        # Event klik baris tabel
        self.view.tree.bind("<<TreeviewSelect>>", self.pada_baris_dipilih)

        # OTORISASI: kunci tombol jika bukan admin (Tugas 2)
        if self.user_role != "admin":
            self.view.btn_simpan.config(state="disabled")
            self.view.btn_update.config(state="disabled")
            self.view.btn_hapus.config(state="disabled")

        # Muat data pertama kali
        self.load_data()

    def load_data(self):
        """Mengambil data dari database dan merapikannya ke tabel GUI"""
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        data_buku = self.model.get_all_buku()

        for row in data_buku:
            # Menangani format data baik berupa dictionary maupun tuple
            if isinstance(row, dict):
                buku_id = row.get('id') or row.get('id_buku')
                judul = row.get('judul') or row.get('judul_buku')
                penulis = row.get('penulis') or row.get('stok')
                tahun = row.get('tahun') or row.get('tahun_terbit') or ''
                values = (buku_id, judul, penulis, tahun)
            else:
                values = row

            self.view.tree.insert("", "end", values=values)

    def simpan_buku(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.ent_judul.get().strip()
        penulis = self.view.ent_penulis.get().strip()
        tahun = self.view.ent_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        try:
            self.model.add_buku(judul, penulis, int(tahun))
            self.load_data()
            self.view.clear_inputs()
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data: {e}")

    def pada_baris_dipilih(self, event):
        selected_item = self.view.tree.selection()
        if selected_item:
            item_data = self.view.tree.item(selected_item[0])['values']
            if item_data:
                self.view.selected_id = item_data[0]
                self.view.ent_judul.delete(0, "end")
                self.view.ent_judul.insert(0, str(item_data[1]))

                self.view.ent_penulis.delete(0, "end")
                self.view.ent_penulis.insert(0, str(item_data[2]))

                self.view.ent_tahun.delete(0, "end")
                self.view.ent_tahun.insert(0, str(item_data[3]))

    def update_buku(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk mengubah data!")
            return

        if not self.view.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data dari tabel terlebih dahulu!")
            return

        judul = self.view.ent_judul.get().strip()
        penulis = self.view.ent_penulis.get().strip()
        tahun = self.view.ent_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        try:
            self.model.update_buku(self.view.selected_id, judul, penulis, int(tahun))
            self.load_data()
            self.view.clear_inputs()
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memperbarui data: {e}")

    def hapus_buku(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        if not self.view.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data dari tabel terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if konfirmasi:
            try:
                self.model.delete_buku(self.view.selected_id)
                self.load_data()  # Refresh tabel otomatis agar baris langsung hilang
                self.view.clear_inputs()
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menghapus data: {e}")

    def logout(self):
        if messagebox.askyesno("Logout", "Apakah Anda yakin ingin keluar?"):
            self.view.parent.destroy()
            from controllers.auth_controller import AuthController
            AuthController().run()