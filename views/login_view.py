import tkinter as tk
from tkinter import Label, Entry, Button


class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistem Perpustakaan")
        self.geometry("360x300")
        self.resizable(False, False)

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        Label(frame, text="LOGIN SISTEM", font=("Helvetica", 16, "bold")).pack(pady=(10, 15))

        Label(frame, text="Username:", font=("Helvetica", 9, "bold")).pack(anchor="w")
        self.entry_username = Entry(frame)
        self.entry_username.pack(fill="x", pady=(2, 10))

        Label(frame, text="Password:", font=("Helvetica", 9, "bold")).pack(anchor="w")
        self.entry_password = Entry(frame, show="*")
        self.entry_password.pack(fill="x", pady=(2, 15))

        self.btn_login = Button(frame, text="Masuk", bg="#007bff", fg="white", font=("Helvetica", 9, "bold"), pady=5)
        self.btn_login.pack(fill="x")