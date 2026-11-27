import tkinter as tk

def hasil(GBK):
    global a
    a+=1
    label_skor.config(text=f"Musuh = {a} - Kamu = 0")
    label_hasil.config(text=f"Musuh memilih {GBK}, Kamu Kalah!")

def execute(kondisi):
    match kondisi:
        case "gunting":
            hasil("Batu")
        case "batu":
            hasil("Kertas")
        case "kertas":
            hasil("Gunting")

a=0

window = tk.Tk()

window.title("Gunting, Batu, Kertas")
window.geometry("500x600")

label_judul = tk.Label(
    window,
    text="GUNTING BATU KERTAS\n" \
    "Kelompok50_Shift08",
    font=("Arial", 15)
)
label_judul.pack(pady=50)

label_skor = tk.Label(
    window,
    text=f"Musuh = {a} - Kamu = 0",
    font=("Arial", 10)
)
label_skor.pack(pady=3)

button_batu = tk.Button(
    window,
    text="Batu",
    command=lambda: execute("batu")
)
button_batu.pack(pady=5)

button_gunting = tk.Button(
    window,
    text="Gunting",
    command=lambda: execute("gunting")
)
button_gunting.pack(pady=1)

button_kertas = tk.Button(
    window,
    text="Kertas",
    command=lambda: execute("kertas")
)
button_kertas.pack(pady=1)

label_hasil = tk.Label(
    window,
    text="",
    font=("Arial", 10)
)
label_hasil.pack(pady=5)

window.mainloop()