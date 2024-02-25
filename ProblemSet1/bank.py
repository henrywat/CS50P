ans = input("Greeting: ")
ans = ans.lower().strip()

if (not ans.startswith("h")):
    print("$100")
elif (ans.startswith("hello")):
    print("$0")
else:
    print("$20")