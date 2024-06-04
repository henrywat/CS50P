def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    slist = list(s)
    if (len(slist)<2 or len(slist)>6):
        return False

    pos=1
    for c in slist:
        if (pos==1 or pos==2) and (not c.isalpha()):
            return False
        elif pos==3 and c=="0":
            return False
        elif c in [',','.','!','?',' ']:
            return False
        elif pos>3 and c.isalpha() and slist[pos-2].isnumeric():
            return False
        elif c.islower():
            return False
        pos += 1

    return True

main()
