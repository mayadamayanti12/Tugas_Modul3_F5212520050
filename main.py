import tkinter as tk
from views.buku_view import BukuView      # Sesuaikan dengan letak file view Anda
from models.buku_model import BukuModel  # Sesuaikan dengan letak file model Anda
from controllers.buku_controller import BukuController # Sesuaikan letak file controller

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistem Perpustakaan")
    root.geometry("900x500")

    # Inisialisasi Model, View, dan Controller
    model = BukuModel()
    view = BukuView(root)
    controller = BukuController(model, view)

    root.mainloop()