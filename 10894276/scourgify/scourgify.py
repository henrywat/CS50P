import csv, sys

args = sys.argv
if len(args) < 3:
    sys.exit("Too few command-line arguments")
elif len(args) > 3:
    sys.exit("Too many command-line arguments")

csvbefore = args[1]
csvafter = args[2]

afterdata = []

try :
    with open(csvbefore) as csvfile:
        reader = csv.DictReader(csvfile)
        with open(csvafter, "w", newline="") as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                name = row["name"]
                last, first = name.split(",")
                writer.writerow({"first":first.strip(), "last":last.strip(), "house":row["house"].strip()})

except FileNotFoundError:
    sys.exit(f"Could not read {filebefore}")
