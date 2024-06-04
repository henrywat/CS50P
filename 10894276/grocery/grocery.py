thisdict = {}
thisdict.clear()
while True:
    try:
        item = input().upper()
        if item=="END":
            break
        else:
            if item in thisdict:
                thisdict.update({item: thisdict.get(item)+1})
            else:
                thisdict.update({item: 1})
    except EOFError:
        break

sorted_dict = dict(sorted(thisdict.items()))

for x in sorted_dict:
    print(f"{sorted_dict.get(x)} {x}")
