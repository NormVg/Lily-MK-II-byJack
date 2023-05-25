# Lily MK 2.0 - Bootloader

import os

print(f"Lily Bootloader: Loaded virtual environment...")

print(f"Lily Bootloader: Which client? (Discord, Ultron, Whisper, GUI, server, hologram, monitor, or Basic)")
client = input("Client: ")
client = client.lower()

def Options(client):
    if client == "discord":
        print("Initializing...")
        try:
            os.system("python3 Discord_client.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 Discord_client.py")
    elif client == "ultron":
        print("Initializing...")
        try:
            os.system("python3 Discord_Ultron_client.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 Discord_Ultron_client.py")
    elif client == "whisper":
        print("Initializing...")
        try:
            os.system("python3 Speech_client.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 Speech_client.py")
    elif client == "gui":
        print("Initializing...")
        try:
            os.system("python3 tkinter_client.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 tkinter_client.py")
    elif client == "hologram":
        print("Initializing...")
        try:
            os.system("python3 hologram_client.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 hologram_client.py")
    elif client == "basic":
        print("Initializing...")
        try:
            os.system("python3 basic_client.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 basic_client.py")
    elif client == "server":
        print("Initializing...")
        try:
            os.system("python3 server.py")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("python3 server.py")
    elif client == "monitor":
        print("Initializing...")
        try:
            os.system("node monitor.js")
            os.system("node SpotifyRead.js")
        except:
            print("")
            print("Client crashed. Rebooting...")
            os.system("node monitor.js")
            os.system("node SpotifyRead.js")
    else:
        print("Unrecognised Input.")
        Options()

print(" ")
print(" ")
print(" ")
print(" ")

e = 2

while True:
    try:
        Options(client)
    except:
        Options(client)
