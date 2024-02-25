def main ():
    due=50
    while due>1:
        while True:
            print("Amount Due:",due)
            coin = 0
            coin = int(input ("Insert Coin: "))
            if (coin==25 or coin==10 or coin==5):
                due -= coin
                break
    print("Change Owed:", abs(due))





main()