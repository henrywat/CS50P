months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    try:
        iDate = input("Date: ").strip()
        if "/" in iDate:
            month, date, year = iDate.split("/")
        elif "," in iDate:
            iDate = iDate.replace(",","")
            iDate = iDate.replace(". "," ")
            month, date, year = iDate.split(" ")
            month = months.index(month)+1
        month=int(month)
        date=int(date)
        #print(f"{year}-{month:02d}-{date:02d}")
        if 0 < month < 13 and 0 < date < 32:
            print(f"{year}-{month:02d}-{date:02d}")
            break
        else:
            raise ValueError
    except (ValueError, NameError):
        pass


