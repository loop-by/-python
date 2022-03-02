import tkinter as tk
import csv
from tkinter import filedialog, Text, messagebox

def data_manipulation(csvfile):
    # Open file
    df = open(csvfile, "r")
    lines = df.readlines()

    # Close file
    df.close()

    output = []

    for line in lines:
        if (line[0:2] == "2,"):
            data = line.split(",")
            output.append(data[3])
            output.append(data[4])
            output.append(data[5])
            output.append(data[6])
            output.append(data[12])

    return(output)

def addFiles():
    for widget in frame.winfo_children():
        widget.destroy()

    filenames = filedialog.askopenfilenames(initialdir = "/", title = "Select File", filetypes = [("CSV files", "*.csv")])

    for file in filenames:
        files.append(file)
        label = tk.Label(frame, text=file)
        label.pack(fill=tk.X)

def showOutput():
    for file in files:
        output = data_manipulation(file)

        fn = str(file).split("/")
        textOut = fn[-1] + "\n"

        textOut += "Vig\t\tMod\t\tLow\t\tSed\t\tTotal\n"

        for s in output:
            if len(s) > 7:
                s = str(s) + "\t"
            else:
                s = str(s) + "\t\t"
            textOut += s

        print(textOut + "\n")

def writeOutput():
    header = ["filename", "Vig", "Mod", "Low", "Sed", "Total"]
    with open('output.csv', 'w', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for file in files:
            fn = str(file).split("/")
            output = [fn[-1]]
            output = output + data_manipulation(file)
            writer.writerow(output)

root = tk.Tk()
root.title(string="Day 2 Activity Collecter")
files = []

canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.07)

openFile = tk.Button(root, text="Open File(s)", padx=13, pady=5, fg="white", bg="#263D42", command=addFiles)
openFile.pack(fill=tk.X, padx=40, pady=5)

show = tk.Button(root, text="Show", padx=30, pady=5, fg="white", bg="#263D42", command=showOutput)
show.pack(fill=tk.X, padx=40, pady=5, side=tk.LEFT)

export = tk.Button(root, text="Export", padx=30, pady=5, fg="white", bg="#263D42", command=writeOutput)
export.pack(fill=tk.X, padx=40, pady=2, side=tk.RIGHT)

root.mainloop()
