def main():
    while True:
        try:
            s=input("Fraction: ")
            z=convert(s)
            #print(z)
            print(gauge(z))
        except (ValueError, IndexError, ZeroDivisionError):
            pass
        else:
            break

def convert(fraction):
    listx = fraction.split("/")
    x=int(listx[0])
    y=int(listx[1])
    if y==0:
        raise ZeroDivisionError
    if x>y:
        raise ValueError

    return round(x/y*100, 0)

def gauge(percentage):
    if percentage>89:
        return "F"
    elif percentage<11:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
