import tkinter as tk
from tkinter import filedialog, Text
import os
import json

config = "save.json"

# ── ➊ LOAD AT STARTUP ──
if os.path.exists(config):
    with open(config, "r") as f:
        appsCat = json.load(f)
        
else:
    appsCat = {
        "Work":        [],
        "Games":       [],
        "Utilities":   [],
        "Uncategorized": []
}
currentCat = "Uncategorized"




def refresh():
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()
        
    # Recreate the category buttons
    for path in appsCat[currentCat]:
        label = tk.Label(frame, text=path, bg="gray").pack(fill="x", padx=5, pady=5)


def addApp():      
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    
    if not filename:
        return
    appsCat[currentCat].append(filename)
    saveConfig()
    refresh()

def saveConfig():
    with open(config, "w") as f:
        json.dump(appsCat, f, indent=4)
    print("Configuration saved.")
    
def runApps():
    for app in appsCat[currentCat]:
        os.startfile(app)

def categorySelect(evt):
    global currentCat
    selected = catList.curselection()
    if selected:
        currentCat = catList.get(selected[0])
        refresh()



#---Building the GUI---
root = tk.Tk()
root.title("Jalen's Launcher")
root.geometry("600x400")


# 1) Sidebar + Main pane
sidebar = tk.Frame(root, width=150, bg="#95A5A6")
sidebar.pack(side="left", fill="y")
main    = tk.Frame(root, bg="white")
main.pack(side="right", fill="both", expand=True)


# 2) category list
catList = tk.Listbox(sidebar)
catList.pack(fill="y", padx=5, pady=5)
for cat in appsCat:
    catList.insert(tk.END, cat)
catList.selection_set(0)
catList.bind("<<ListboxSelect>>", categorySelect)

#3) controls
tk.Button(sidebar, text="Add App", command=addApp).pack(fill="x", padx=5, pady=2)
tk.Button(sidebar, text="Run All", command=runApps).pack(fill="x", padx=5, pady=2)


#4) App display frame
frame = tk.Frame(main, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#5) kick off the app
refresh()
root.mainloop()



 






