import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    if re.search(r"^[0-9]+\.[0-9]+\.+[0-9]+\.[0-9]+$", ip):
        temp = ip.split(".")
        result = True
        for i in temp:
            i = int(i)
            if i < 0 or i > 255:
                result = False
        return result
    else:
        return False


if __name__ == "__main__":
    main()