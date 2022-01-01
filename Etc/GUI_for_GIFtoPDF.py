import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from GIFtoPDF import *

# Retrieved from: https://www.youtube.com/watch?v=jE-SpRI3K5g
# modified by: loop-by

root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("gif files", "*.gif"), ("all files", "*.*")))

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

def runApps():
    for app in apps:
        pathList = app.split("/")
        path = "\\".join(pathList[0:-2])
        messagebox.showinfo("Alert","Converting files in:\n" + path)
        makePdf(path)
        messagebox.showinfo("Alert","Conversion Complete!")

canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.07)

openFile = tk.Button(root, text="Open File", padx=13, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=12, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

root.mainloop()
