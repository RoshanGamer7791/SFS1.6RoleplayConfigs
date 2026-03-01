import tkinter as tk
from tkinter import messagebox

root = None

mainframe = tk.Frame(root, bg="black", width=1200, height=800)
mainframe.grid_propagate(False)
mainframe.grid()

def rpchanger():
    rpchangerwin = tk.Toplevel(root)
    rpchangerwin.title("Research Point Changer")
    rpchangerwin.geometry("500x500")