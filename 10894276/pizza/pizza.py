import csv
import sys
from tabulate import tabulate

args = sys.argv
if len(args) < 2:
    sys.exit("Too few command-line arguments")
elif len(args) > 2:
    sys.exit("Too many command-line arguments")
elif not args[1].endswith(".csv"):
    sys.exit("Not a CSV file")

file = args[1]
tableheader = []
tablerows = []

try:
    with open(file, newline='') as csvfile:
        headers = csv.reader(csvfile, delimiter=',')
        for header in headers.__next__():
            tableheader.append(header)

    with open(file, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            tablerow = []
            for header in tableheader:
                tablerow.append(row[header])
            tablerows.append(tablerow)
except FileNotFoundError:
    sys.exit(f"{file} Not Found Error")

print(tabulate(tablerows, tableheader, tablefmt="grid"))
