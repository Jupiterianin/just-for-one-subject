import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

# Create the main window
root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")
style = Style(theme='journal')
style = ttk.Style()

# Configure the tab font to be bold
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# Create the notebook to hold the notes
notebook = ttk.Notebook(root, style="TNotebook")

# Load saved notes
notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

