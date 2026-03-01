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

rpchangerbtn = tk.Button(root, bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=rpchanger, text="Reasearch Point Changer")
rpchangerbtn.grid(row=0, column=0)