def main():
    ans = input("Greeting: ")
    print(value(ans))


def value(greeting):
    greeting = greeting.lower().strip()
    if (not greeting.startswith("h")):
        return 100
    elif (greeting.startswith("hello")):
        return 0
    else:
        return 20


if __name__ == "__main__":
    main()







