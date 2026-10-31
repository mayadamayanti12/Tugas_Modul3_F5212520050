import tkinter as tk
from tkinter import ttk, LabelFrame, Label, Entry, Button

class BukuView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.selected_id = None
        
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        # ---------------- Form Left Frame ----------------
        frame_form = LabelFrame(self, text="Form Input Buku", font=("Helvetica", 10, "bold"), padx=10, pady=10)
        frame_form.pack(side="left", fill="both", expand=False, padx=(0, 10))

        Label(frame_form, text="Judul Buku:", font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(5, 2))
        self.ent_judul = Entry(frame_form, width=30)
        self.ent_judul.pack(fill="x", pady=(0, 10))

        Label(frame_form, text="Penulis:", font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(5, 2))
        self.ent_penulis = Entry(frame_form, width=30)
        self.ent_penulis.pack(fill="x", pady=(0, 10))

        Label(frame_form, text="Tahun Terbit:", font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(5, 2))
        self.ent_tahun = Entry(frame_form, width=30)
        self.ent_tahun.pack(fill="x", pady=(0, 15))

        # Buttons
        self.btn_simpan = Button(frame_form, text="Simpan Data", bg="#28a745", fg="white", font=("Helvetica", 9, "bold"), pady=5)
        self.btn_simpan.pack(fill="x", pady=4)

        self.btn_update = Button(frame_form, text="Perbarui Data (Update)", bg="#007bff", fg="white", font=("Helvetica", 9, "bold"), pady=5)
        self.btn_update.pack(fill="x", pady=4)

        self.btn_hapus = Button(frame_form, text="Hapus Data (Delete)", bg="#dc3545", fg="white", font=("Helvetica", 9, "bold"), pady=5)
        self.btn_hapus.pack(fill="x", pady=4)

        self.btn_logout = Button(frame_form, text="Logout", bg="#6c757d", fg="white", font=("Helvetica", 9, "bold"), pady=5)
        self.btn_logout.pack(fill="x", pady=(20, 4))

        # ---------------- Table Right Frame ----------------
        frame_table = LabelFrame(self, text="Daftar Koleksi Buku", font=("Helvetica", 10, "bold"), padx=10, pady=10)
        frame_table.pack(side="right", fill="both", expand=True)

        columns = ("id", "judul", "penulis", "tahun")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings")

        self.tree.heading("id", text="ID Buku")
        self.tree.heading("judul", text="Judul Buku")
        self.tree.heading("penulis", text="Penulis")
        self.tree.heading("tahun", text="Tahun Terbit")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("judul", width=200, anchor="w")
        self.tree.column("penulis", width=150, anchor="w")
        self.tree.column("tahun", width=90, anchor="center")

        self.tree.pack(fill="both", expand=True)

    def clear_inputs(self):
        self.selected_id = None
        self.ent_judul.delete(0, "end")
        self.ent_penulis.delete(0, "end")
        self.ent_tahun.delete(0, "end")

# Tambahkan bagian ini di baris paling bawah file agar bisa dijalankan mandiri
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplikasi Buku")
    root.geometry("850x450")
    
    app = BukuView(root)
    
    root.mainloop()