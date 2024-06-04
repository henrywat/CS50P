s = input("camelCase: ")


for c in s:
    print(c, end="") if c.islower() else print("_", c.lower(), sep="", end="")
print()
