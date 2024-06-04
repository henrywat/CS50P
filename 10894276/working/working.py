import re


def main():
    print(convert(input("Hours: ")))
    #print(convert("9:00 AM to 5:00 PM"))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        time = standardize(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError

def standardize(hr, min, x):
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()

    """
    9:00 AM to 5:00 PM == 09:00 to 17:00
    9:00 AM to 5:00 PM == 09:00 to 17:00
    10:30 PM to 8:50 AM == 22:30 to 08:50

    9 AM to 5 PM == 09:00 to 17:00
    9 AM to 5:30 PM == 09:00 to 17:30
    10 PM to 8 AM == 22:00 to 08:00

    9:60 AM to 5:60 PM == ValueErro
    9 AM - 5 PM == ValueErro
    09:00 AM - 17:00 PM == ValueErro
    """
