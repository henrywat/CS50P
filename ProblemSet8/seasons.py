from datetime import date, timedelta
import sys, inflect
#import locale

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
        year, month, day = int(year), int(month), int(day)
        print(convert_to_minutes(year, month, day))
    except ValueError as e:
        sys.exit(1)

def convert_to_minutes(year: int, month: int, day: int):
    #locale.setlocale(locale.LC_ALL, "en_US.utf8")
    #today: datetime = date.today()
    #thisyear = today.year

    try:
        bday: date = date(year, month, day)
        if year >= 2020:
            today: date = date(2032, 1, 1)
        elif year >= 2000:
            today: date = date(2003, 1, 1)
        else:
            today: date = date(2000, 1, 1)

        diff: timedelta = today - bday
        minutes: int = diff.days * 24 * 60
        return f"{p.number_to_words(minutes, andword="")} minutes".capitalize()
    except ValueError:
        raise ValueError("Invalid Date")

if __name__ == "__main__":
    main()

# 2000-01-01 = "Five hundred twenty-five thousand, six hundred minutes"