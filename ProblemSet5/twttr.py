vowels="aeiouAEIOU"
s = input("Input: ")

for c in s:
    print(c, end="") if not c in vowels else None
print()