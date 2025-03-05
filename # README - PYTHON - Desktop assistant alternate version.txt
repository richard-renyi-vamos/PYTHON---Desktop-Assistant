CHATGPT CONVERSATION

*****************

You said:
create a modular PYTHON code that acts as a desktop agent.
- link launcher
- settings
- app manager
ChatGPT said:
Here’s a modular Python-based desktop agent with the following features:

Link Launcher: Opens URLs or files/applications.
Settings: Basic configuration settings saved in a JSON file.
App Manager: Lists and runs installed applications.
This is designed to be expandable, allowing additional modules to be added easily.


Answer in chat instead
This script provides a simple GUI with buttons for launching links, managing apps, and updating settings. It uses Tkinter for the interface and JSON for configuration storage. Let me know if you want any modifications! 🚀

*****************

import os
import json
import webbrowser
import subprocess
from tkinter import Tk, Button, Label, filedialog

# Configuration file for settings
SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

def open_link():
    url = input("Enter URL or file path: ")
    if url.startswith("http"):
        webbrowser.open(url)
    elif os.path.exists(url):
        os.startfile(url)
    else:
        print("Invalid path or URL")

def manage_apps():
    print("Installed Applications:")
    installed_apps = ["notepad", "calc", "cmd"]  # Example apps, can be extended
    for idx, app in enumerate(installed_apps, start=1):
        print(f"{idx}. {app}")
    choice = input("Enter app number to launch: ")
    if choice.isdigit() and 1 <= int(choice) <= len(installed_apps):
        subprocess.run(installed_apps[int(choice)-1])
    else:
        print("Invalid choice")

def open_settings():
    settings = load_settings()
    print("Current Settings:", settings)
    key = input("Enter setting name to change: ")
    value = input("Enter new value: ")
    settings[key] = value
    save_settings(settings)
    print("Settings updated successfully!")

def create_gui():
    root = Tk()
    root.title("Desktop Agent")
    root.geometry("300x200")
    
    Label(root, text="Desktop Agent").pack()
    Button(root, text="Launch Link", command=open_link).pack()
    Button(root, text="Manage Apps", command=manage_apps).pack()
    Button(root, text="Settings", command=open_settings).pack()
    Button(root, text="Exit", command=root.quit).pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
