import tkinter as tk
from tkinter import messagebox

root = None

researchpoints = 0
upvar = tk.StringVar(value="Unlocked Parts:")

canvas = tk.Canvas(root, bg="black", borderwidth=0)
sb = tk.Scrollbar(root, orient="horizontal", command=canvas.xview, bg="black", troughcolor="white", width=10)
canvas.configure(xscrollcommand=sb.set)
sb.pack(side="bottom", fill="x", expand=True)
canvas.pack(side="top", fill="both", expand=True)
btns = tk.Frame(canvas, bg="black")
windowid = canvas.create_window((0, 0), window=btns, anchor="nw")
ttn = tk.Frame(btns, bg="black")
ttn.pack(side="top", fill="both", expand=True)

rpcounter = tk.Label(btns, text=f"Research Points: {researchpoints}", bg="black", fg="white", font=("Segoe UI", 15, "bold"))
rpcounter.pack(side="top")

def rp_changer():
    rpcw = tk.Toplevel(root)
    rpcw.title("Research Point Changer"),
    rpcw.geometry("490x490")
    def add1():
        global researchpoints
        researchpoints += 1
        rpcounter.config(text=f"Research Points: {researchpoints}")
    
    def add10():
        global researchpoints
        researchpoints += 10
        rpcounter.config(text=f"Research Points: {researchpoints}")
    
    def add100():
        global researchpoints
        researchpoints += 100
        rpcounter.config(text=f"Research Points: {researchpoints}")
    
    def add250():
        global researchpoints
        researchpoints += 250
        rpcounter.config(text=f"Research Points: {researchpoints}")
        
    def add500():
        global researchpoints
        researchpoints += 500
        rpcounter.config(text=f"Research Points: {researchpoints}")
            
    add1b = tk.Button(rpcw, text="+1", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=add1)
    add1b.pack(side="top", fill="x")
    add10b = tk.Button(rpcw, text="+10", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=add10)
    add10b.pack(side="top", fill="x") 
    add100b = tk.Button(rpcw, text="+100", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=add100)
    add100b.pack(side="top", fill="x")
    add250b = tk.Button(rpcw, text="+250", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=add250)
    add250b.pack(side="top", fill="x")
    add500b = tk.Button(rpcw, text="+500", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=add500)
    add500b.pack(side="top", fill="x")
    
    def remove1():
        global researchpoints
        researchpoints -= 1
        rpcounter.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            researchpoints += 1
            rpcounter.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Not enough research",
                message="You dont have enough research points for this"
            )
            return
    
    def remove10():
        global researchpoints
        researchpoints -= 10
        rpcounter.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            researchpoints += 10
            rpcounter.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Not enough research",
                message="You dont have enough research points for this"
            )
            return
        
    def remove100():
        global researchpoints
        researchpoints -= 100
        rpcounter.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            researchpoints += 100
            rpcounter.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Not enough research",
                message="You dont have enough research points for this"
            )
            return
        
    def remove250():
        global researchpoints
        researchpoints -= 250
        rpcounter.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            researchpoints += 250
            rpcounter.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Not enough research",
                message="You dont have enough research points for this"
            )
            return
    
    def remove500():
        global researchpoints
        researchpoints -= 500
        rpcounter.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            researchpoints += 500
            rpcounter.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Not enough research",
                message="You dont have enough research points for this"
            )
            return
    
    remove1b = tk.Button(rpcw, text="-1", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=remove1)
    remove1b.pack(side="top", fill="x")
    remove10b = tk.Button(rpcw, text="-10", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=remove10)
    remove10b.pack(side="top", fill="x")
    remove100b = tk.Button(rpcw, text="-100", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=remove100)
    remove100b.pack(side="top", fill="x")
    remove250b = tk.Button(rpcw, text="-250", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=remove250)
    remove250b.pack(side="top", fill="x")
    remove500b = tk.Button(rpcw, text="-500", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=remove500)
    remove500b.pack(side="top", fill="x")

rpbutton = tk.Button(btns, text="Research Points Changer", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=rp_changer)
rpbutton.pack(side="top", padx=10)

def upui():
    upuiwin = tk.Toplevel(root, bg="black")
    upuiwin.title("Unlocked Parts")
    upuiwin.geometry("500x500")
    upmsg = tk.Message(upuiwin, bg="black", fg="white", font=("Segoe UI", 15, "bold"), textvariable=upvar, width=500)
    upmsg.pack(fill="both", expand=True)
    
upuib = tk.Button(btns, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="Unlocked Parts", command=upui)
upuib.pack(side="top")

def startnode():
    global upvar
    current = upvar.get()
    if " Mystery Goo, Kolibri Engine, 4x2 Fuel Tank" not in current:
        upvar.set(current + " Mystery Goo, Kolibri Engine, 4x2 Fuel Tank")
    else:
        messagebox.showinfo(
            title="Node already unlocked",
            message="You already unlocked this node"
        )
        return
    
startb = tk.Button(ttn, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="Start", command=startnode)
startb.grid(row=50, column=0)

def seperators():
    global upvar, researchpoints
    current = upvar.get()
    if ", Seperators, Thermometers, Valiant Engine" not in current:
        researchpoints -= 10
        rpcounter.config(text=f"Research Points: {researchpoints}")
        upvar.set(current + ", Seperators, Thermometers, Valiant Engine")
    else:
        messagebox.showinfo(
            title="Node already unlocked",
            message="You already unlocked this node"
        )
        return
    if researchpoints <= -1:
        researchpoints += 10
        rpcounter.config(text=f"Research Points: {researchpoints}")
        messagebox.showerror(
            title="Not enough Research",
            message="You dont have enough research for this"
        )
        return
    
seperatorsb = tk.Button(ttn, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="Seperators", command=seperators)
seperatorsb.grid(row=50, column=5)

def general_rocketry():
    global upvar, researchpoints
    current = upvar.get()
    if ", Hawk Engine, 4x4 Fuel Tank, 4x8 Fuel Tank" not in current:
        researchpoints -= 45
        rpcounter.config(text=f"Research Points: {researchpoints}")
        upvar.set(current + ", Hawk Engine, 4x4 Fuel Tank, 4x8 Fuel Tank")
    else:
        messagebox.showinfo(
            title="Node already unlocked",
            message="You already unlocked this node"
        )
        return
    if researchpoints <= -1:
        researchpoints += 45
        rpcounter.config(text=f"Research Points: {researchpoints}")
        messagebox.showerror(
            title="Not enough Research",
            message="You dont have enough research for this"
        )
        return
    
general_rocketryb = tk.Button(ttn, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="General Rocketry", command=general_rocketry)
general_rocketryb.grid(row=45, column=10)

def generalsolidrocketmotors():
    global upvar, researchpoints
    current = upvar.get
    if "4 wide Solid Rocket Boosters" not in current:
        researchpoints -= 45
        rpcounter.config(text=f"Research Points: {researchpoints}")
        upvar.set(current + ", 4 wide Solid Rocket boosters")
    else:
        messagebox.showinfo(
            title="Node already unlocked",
            message="You already unlocked this node"
        )
    if researchpoints <= -1:
        researchpoints += 45
        rpcounter.config(text=f"Research Points: {researchpoints}")
        messagebox.showerror(
            title="Not enough Research",
            message="You dont have enough research for this"
        )
        return
    
generalsolidrocketmotorsb = tk.Button(ttn, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="General Solid Rocket Motors", command=generalsolidrocketmotors)
generalsolidrocketmotorsb.grid(row=55, column=10)

def advanced_rocketry():
    global upvar, researchpoints
    current = upvar.get()
    if ", Titan Engine, 6x2 Fuel Tank, 6x4 Fuel Tank, 6x6 Fuel Tank, 6x8 Fuel Tank" not in current:
        researchpoints -= 90
        rpcounter.config(text=f"Research Points: {researchpoints}")
        upvar.set(current + ", Titan Engine, 6x2 Fuel Tank, 6x4 Fuel Tank, 6x6 Fuel Tank, 6x8 Fuel Tank")
    else:
        messagebox.showinfo(
            title="You already unlocked",
            message="You already unlocked this node"
        )
        return
    if researchpoints <= -1:
        researchpoints += 90
        rpcounter.config(text=f"Research Points: {researchpoints}")
        messagebox.showerror(
            title="Not enough Research",
            message="You dont have enough research for this"
        )
        return
    
advanced_rocketryb = tk.Button(ttn, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="Advanced Rocketry", command=advanced_rocketry)
advanced_rocketryb.grid(row=50, column=15)