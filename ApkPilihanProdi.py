import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x750")
root.configure(bg="#302775")
root.resizable(False, False)

# Warna
BG = "#302775"
PANEL = "#493DB5"
ENTRY_BG = "#6559C9"
WHITE = "#FFFFFF"
ACCENT = "#DCD7FF"

# Frame Utama
frame = tk.Frame(
    root,
    bg=PANEL,
    padx=25,
    pady=25
)
frame.pack(fill="both", expand=True, padx=15, pady=15)