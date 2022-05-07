import tkinter as tk
import csv
import os
from tkinter import filedialog, Text, messagebox

def toMinutes(args):
    time = args.split(":")
    return int(time[0])*60 + int(time[1])
def toHoursMins(args):
    if args < 0:
        raise ValueError
    if args > 60:
        return str(args//60) + ":" + str(args%60)
    else:
        return "00:" + str(args%60)
def validate24hrs(vig, mod, low, sed):
    totalHour = vig + mod + low + sed
    if totalHour == 1440:
        return True
    else:
        raise ValueError("Total_Minutes: " + str(totalHour))
def calculation(data):
    cell = data.split(",")

    # Getting rid of seconds from data (it should always be ":00")
    for i in range(3, 9):
        cell[i] = cell[i][0:cell[i].rfind(":")]

    tVig = toMinutes(cell[3])
    tMod = toMinutes(cell[4])
    tLow = toMinutes(cell[5])
    tSed = toMinutes(cell[6])

    validate24hrs(tVig, tMod, tLow, tSed)

    cVig = toMinutes(cell[7])
    # Temporarily implemented due to "appeared to be bug" from MW
    cMod = toMinutes(cell[8]) - cVig
    # Parentheses are not required.
    updatedLow = tLow + (tVig - cVig) + (tMod - cMod)

    return [cell[1], toHoursMins(tVig), toHoursMins(tMod), toHoursMins(tLow), toHoursMins(tSed), toHoursMins(cVig), toHoursMins(cMod), toHoursMins(updatedLow), cell[12]]

def data_manipulation(csvfile):
    # Open file
    df = open(csvfile, "r")
    lines = df.readlines()
    # Close file
    df.close()

    for line in lines:
        if (line[0:2] == "2,"):
            try:
                return calculation(line)
            except ValueError:
                messagebox.showinfo("Alert","Invalid Data Detected:\n"  + csvfile)
def addFiles():
    for widget in frame.winfo_children():
        widget.destroy()

    filenames = filedialog.askopenfilenames(initialdir=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'), title = "Select File", filetypes = [("CSV files", "*.csv")])

    for file in filenames:
        files.append(file)

    for file in files:
        label = tk.Label(frame, text=file)
        label.pack(fill=tk.X)
def showOutput():
    for file in files:
        output = data_manipulation(file)

        fn = str(file).split("/")
        textOut = fn[-1] + "\n"

        textOut += "Date\t\tTotal Vig.\tTotal Mod.\tTotal Low\tTotal Sed.\tCon. Vig\tCon. Mod.\tUpdated Low\tTotal\n"

        for s in output:
            if len(str(s)) > 7:
                s = str(s) + "\t"
            else:
                s = str(s) + "\t\t"
            textOut += s

        print(textOut + "\n")
def writeOutput():
    header = ["filename", "Date", "Total Vig.", "Total Mod.", "Total Low", "Total Sed.", "Con. Vig", "Con. Mod.", "Updated Low", "Total"]
    with open('output.csv', 'w', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for file in files:
            fn = str(file).split("/")
            output = [fn[-1]]
            output = output + data_manipulation(file)
            writer.writerow(output)

    messagebox.showinfo("Alert","Export Complete!")

files = []

root = tk.Tk()
root.title(string="Day 2 Activity Collecter")

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
