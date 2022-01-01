import os, glob
import pandas as pd



def toMinutes(args):
    return int(args[0])*60 + int(args[1])

def toHoursMins(args):
    if args > 60:
        return str(args//60) + ":" + str(args%60)
    else:
        return "00:" + str(args%60)

mycsvdir = r'C:\Users\David\Downloads\For DK\CSVExports'

csvfiles = glob.glob(os.path.join(mycsvdir, '2403.mtn.csv'))

for csvfile in csvfiles:
    df = open(csvfile, "r")
    lines = df.readlines()

    vig, mod, low, sed, total = 0, 0, 0, 0, 0

    for line in lines:
        if (line[0:2] == "1,"):
            data = line.split(",")
            vig += toMinutes(data[3].split(":"))
            mod += toMinutes(data[4].split(":"))
            low += toMinutes(data[5].split(":"))
            sed += toMinutes(data[6].split(":"))
            total += int(data[12])

        if (line[0:2] == "2,"):
            data = line.split(",")
            vig += toMinutes(data[3].split(":"))
            mod += toMinutes(data[4].split(":"))
            low += toMinutes(data[5].split(":"))
            sed += toMinutes(data[6].split(":"))
            total += int(data[12])




    fn = str(csvfile).split("\\")
    print("\n" + fn[-1] + ": " + toHoursMins(vig+mod+low+sed) + "\n")
    # print("\n" + fn[-1] + "\n")
    print("Vig\tMod\tLow\tSed\tTotal")
    print(toHoursMins(vig) + "\t" + toHoursMins(mod) + "\t" + toHoursMins(low) + "\t" + toHoursMins(sed) + "\t" + str(total) + "\t")


    df.close()

# print(dataframes)
