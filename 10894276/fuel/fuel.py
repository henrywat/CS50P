def main():

    while True:
        try:
            s=input("Fraction: ")
            listx = s.split("/")
            x=int(listx[0])
            y=int(listx[1])
            if x>y:
                raise ValueError
            z=x/y
            print("F") if z>0.89 else print("E") if z<0.11 else print (f"{(z*100):.0f}%")
            #print (f"{z:.0f}%")
        except (ValueError, IndexError, ZeroDivisionError):
            pass
        else:
            break







main()
