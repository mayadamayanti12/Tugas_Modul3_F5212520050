import tkinter as tk
from tkinter import ttk

class AnggotaView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # PERBAIKAN: Baris title dan geometry dihapus dari sini 
        # karena pengaturannya sudah dipusatkan di main.py (menggunakan Tab/Notebook).
        
        self.selected_id = None
        self.pack(fill="both", expand=True, padx=15, pady=15)
        self.create_widgets()

    def create_widgets(self):
        # Frame Kiri: Form Data Anggota
        frame_form = ttk.LabelFrame(self, text=" Form Data Anggota ", padding=15)
        frame_form.pack(side="left", fill="both", expand=False, padx=(0, 10), ipadx=10)

        lbl_nama = ttk.Label(frame_form, text="Nama Anggota:", font=("Helvetica", 9, "bold"))
        lbl_nama.pack(anchor="w", pady=(5, 2))
        
        self.ent_nama = ttk.Entry(frame_form, width=32)
        self.ent_nama.pack(fill="x", pady=(0, 15))

        lbl_alamat = ttk.Label(frame_form, text="Alamat:", font=("Helvetica", 9, "bold"))
        lbl_alamat.pack(anchor="w", pady=(5, 2))
        
        self.txt_alamat = tk.Text(frame_form, width=30, height=8, font=("Helvetica", 9))
        self.txt_alamat.pack(fill="x", pady=(0, 20))

        # Tombol Simpan Data (Warna Hijau)
        self.btn_simpan = tk.Button(
            frame_form, 
            text="Simpan Data", 
            bg="#28a745", 
            fg="white", 
            font=("Helvetica", 9, "bold"), 
            relief="flat", 
            cursor="hand2", 
            pady=6
        )
        self.btn_simpan.pack(fill="x", pady=5)

        # Frame Kanan: Tabel Daftar Anggota
        frame_table = ttk.LabelFrame(self, text=" Daftar Anggota Perpustakaan ", padding=15)
        frame_table.pack(side="right", fill="both", expand=True)

        columns = ("id_anggota", "nama_anggota", "alamat")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=15)

        self.tree.heading("id_anggota", text="ID Anggota")
        self.tree.heading("nama_anggota", text="Nama Anggota")
        self.tree.heading("alamat", text="Alamat")

        self.tree.column("id_anggota", width=80, anchor="center")
        self.tree.column("nama_anggota", width=180, anchor="w")
        self.tree.column("alamat", width=220, anchor="w")

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def clear_inputs(self):
        self.selected_id = None
        self.ent_nama.delete(0, "end")
        self.txt_alamat.delete("1.0", "end")

# (Opsional) Blok ini agar file bisa dites jalan sendiri jika diperlukan
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistem Perpustakaan - Manajemen Data Anggota")
    root.geometry("900x550")
    app = AnggotaView(root)
    root.mainloop()