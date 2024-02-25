import sys

def main():
    args = sys.argv
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        count=0
        lines_pass=""
        line_count=""
        lines=""
        with open(args[1]) as file:
            for line in file:
                line = line.lstrip()
                lines += line
                if line.startswith("#") or line=="":
                    lines_pass += line
                    pass
                else:
                    line_count += line
                    count += 1
        print(count)
        #print()
        #print(f"lines => {lines}")
        #print(f"pass => {lines_pass}")
        #print(f"count => {line_count}")
    except FileNotFoundError:
        sys.exit("File does not exist")


main()