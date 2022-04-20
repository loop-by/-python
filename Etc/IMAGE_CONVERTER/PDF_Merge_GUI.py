import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from PDF_Merge import *

root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    foldername= filedialog.askdirectory(initialdir=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'),
    title="Select Folder",)

    apps.append(foldername)
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

def runApps():
    for app in apps:
        makePDF(app)

    messagebox.showinfo("Alert","Conversion Complete!")

canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.07)

openFile = tk.Button(root, text="Select File", padx=13, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack(fill=tk.X, padx=40, pady=5, side=tk.LEFT)

runApps = tk.Button(root, text="Run", padx=12, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack(fill=tk.X, padx=40, pady=2, side=tk.RIGHT)

root.mainloop()
