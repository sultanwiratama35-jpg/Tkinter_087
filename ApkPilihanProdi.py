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

#Judul
judul = tk.Label(
    frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 19, "bold"),
    bg=PANEL,
    fg=WHITE
)
judul.pack(pady=(5, 25))

#INPUT 10 NILAI MATA PELAJARAN

frame_input = tk.Frame(frame, bg=PANEL)
frame_input.pack()

entries = []

for i in range(10):
    baris = tk.Frame(frame_input, bg=PANEL)
    baris.pack(fill="x", pady=5)
    
    label = tk.Label(
        baris,
        text=f"Nilai Mata Pelajaran {i + 1}:",
        font=("Arial", 10),
        bg=PANEL,
        fg=WHITE,
        width=24,
        anchor="e"
    )
    label.pack(side="left", padx=(0, 12))

    entry = tk.Entry(
        baris,
        font=("Arial", 11),
        width=16,
        bg=ENTRY_BG,
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        justify="center"
    )
    entry.pack(side="left", ipady=4)

    entries.append(entry)
    
    #PILIHAN JURUSAN
    
    label_jurusan = tk.Label(
    frame,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 11, "bold"),
    bg=PANEL,
    fg=WHITE
)
label_jurusan.pack(pady=(25, 8))

jurusan = ttk.Combobox(
    frame,
    values=[
        "Teknologi Informasi",
        "Informatika",
        "Sistem Informasi"
    ],
    state="readonly",
    font=("Arial", 10),
    width=23,
    justify="center"
)
jurusan.set("Teknologi Informasi")
jurusan.pack(pady=(0, 20))


#FUNGSI HASIL PREDIKSI
def hasil_prediksi():
    label_hasil.config(
        text="Hasil Prediksi: Teknologi Informasi"
    )

#TOMBOL HASIL PREDIKSI
tombol = tk.Button(
    frame,
    text="Hasil Prediksi",
    command=hasil_prediksi,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg="#302775",
    activebackground=WHITE,
    activeforeground="#302775",
    relief="raised",
    bd=2,
    padx=15,
    pady=7,
    cursor="hand2"
)
tombol.pack(pady=5)

label_hasil = tk.Label(
    frame,
    text="Hasil prediksi akan ditampilkan di sini.",
    font=("Arial", 11, "bold"),
    bg=PANEL,
    fg=WHITE,
    wraplength=450,
    justify="center"
)
label_hasil.pack(pady=(15, 5))

# Fokus ke input pertama
entries[0].focus_set()

#MENJALANKAN APLIKASI
root.mainloop()