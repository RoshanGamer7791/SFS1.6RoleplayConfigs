import tkinter as tk
from tkinter import messagebox, ttk

root = None

researchpoints = 0
bgval = tk.StringVar(value="gray7")
bg2val = tk.StringVar(value="gray12")
fgval = tk.StringVar(value="white")

print("1: Black Mode\n2: Normal Theme\n3: Light Mode")
themeinput = input("Input your choice: ")

if themeinput == "1":
    bgval.set("black")
    bg2val.set("gray5")
    fgval.set("white")
if themeinput == "2":
    bgval.set("gray7")
    bg2val.set("gray12")
    fgval.set("white")
if themeinput == "3":
    bgval.set("white")
    bg2val.set("gray75")
    fgval.set("black")

mainframe = tk.Frame(root, bg=bgval.get(), width=1200, height=800)
mainframe.grid_propagate(False)
mainframe.grid()

def rpchanger():
    rpchangerwin = tk.Toplevel(root, bg=bgval.get())
    rpchangerwin.title("Research Point Changer")
    entry = tk.Entry(rpchangerwin, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"))
    entry.pack(side="top", fill="x", expand=True)
    def add():
        global researchpoints
        value = int(entry.get())
        researchpoints += value
        rplabel.config(text=f"Research Points: {researchpoints}")
    addbtn = tk.Button(rpchangerwin, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), command=add, text="Add")
    addbtn.pack(side="top", fill="x", expand=True)
    def subtract():
        global researchpoints
        value = int(entry.get())
        researchpoints -= value
        rplabel.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            value = int(entry.get())
            researchpoints += value
            rplabel.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Research Points",
                message="You dont have enough research points"
            )
    subtractbtn = tk.Button(rpchangerwin, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), text="Subtract", command=subtract)
    subtractbtn.pack(side="top", fill="x", expand=True)

topbarframe = tk.Frame(mainframe, bg=bgval.get())
topbarframe.grid(row=0, sticky="nw")
rplabel = tk.Label(topbarframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), text=f"Research Points: {researchpoints}")
rplabel.grid(sticky="nw", row=0, column=0)
rpchangerbtn = tk.Button(topbarframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), command=rpchanger, text="RP Changer")
rpchangerbtn.grid(sticky="nw", row=0, column=1)

def pages(frame):
    frame.tkraise()

pagesframe = tk.Frame(mainframe, bg=bgval.get(), width=1200, height=100)
pagesframe.grid_propagate(False)
pagesframe.grid(row=1, sticky="nw")
t1frame = tk.Frame(mainframe, bg=bg2val.get(), width=800, height=1000)
t1frame.grid_propagate(False)
t1frame.grid(row=2, column=0, sticky="nw")
t1framebtn = tk.Button(pagesframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), text="Teir 1", command=lambda: pages(t1frame))
t1framebtn.grid(row=1, column=0, sticky="nw")
test = tk.Label(t1frame, bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), text="If you can see this your on the teir 1 page")
test.grid(sticky="nw", row=0, column=0)
t2frame = tk.Frame(mainframe, bg=bg2val.get(), width=800, height=1000)
t2frame.grid_propagate(False)
t2frame.grid(row=2, column=0, sticky="nw")
t2framebtn = tk.Button(pagesframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), command=lambda: pages(t2frame), text="Teir 2")
t2framebtn.grid(row=1, column=1, sticky="nw")