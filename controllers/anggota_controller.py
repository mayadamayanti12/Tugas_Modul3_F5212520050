import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()
        self.selected_id = None

        self.view.btn_simpan.configure(command=self.simpan_data)
        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)
        if hasattr(self.view, 'btn_perbarui'):
            self.view.btn_perbarui.configure(command=self.perbarui_data)

        self.view.tabel.bind("<ButtonRelease-1>", self.pilih_data_tabel)
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['email'], anggota['no_telepon']))

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        email = self.view.entry_email.get()
        no_telepon = self.view.entry_no_telepon.get()

        if not nama or not email or not no_telepon:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, email, no_telepon)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def pilih_data_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item = self.view.tabel.item(selected_item)
            values = item['values']
            self.selected_id = values[0]

            self.bersihkan_form()
            self.view.entry_nama.insert(0, values[1])
            self.view.entry_email.insert(0, values[2])
            self.view.entry_no_telepon.insert(0, values[3])

    def perbarui_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data dari tabel terlebih dahulu!")
            return

        nama = self.view.entry_nama.get()
        email = self.view.entry_email.get()
        no_telepon = self.view.entry_no_telepon.get()

        if not nama or not email or not no_telepon:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_anggota(self.selected_id, nama, email, no_telepon)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
            self.selected_id = None
        else:
            messagebox.showerror("Error", "Gagal memperbarui data anggota.")

    def hapus_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data dari tabel yang ingin dihapus!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if konfirmasi:
            berhasil = self.model.delete_anggota(self.selected_id)
            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
                self.selected_id = None
            else:
                messagebox.showerror("Error", "Gagal menghapus data anggota.")

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_email.delete(0, 'end')
        self.view.entry_no_telepon.delete(0, 'end')

    def run(self):
        self.view.mainloop()