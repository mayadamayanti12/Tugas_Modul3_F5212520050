import tkinter as tk
import tkinter.messagebox as messagebox
from models.user_model import UserModel
from models.buku_model import BukuModel
from views.login_view import LoginView
from views.buku_view import BukuView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.view.btn_login.config(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
            return

        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {user['username']} ({user['role']})!")
            self.view.destroy()
            self.buka_aplikasi_utama(user["role"])
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def buka_aplikasi_utama(self, role):
        root = tk.Tk()
        root.geometry("900x500")
        view = BukuView(root)
        model = BukuModel()
        BukuController(model, view, user_role=role)
        root.mainloop()

    def run(self):
        self.view.mainloop()