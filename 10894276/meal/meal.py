def main():
    time = input("What time is it? ")
    mealTime = convert(time)
    print("breakfast time") if (mealTime >=7 and mealTime) <=8 else print("lunch time") if (mealTime >=12 and mealTime <=13) else print ("dinner time") if mealTime >=18 and mealTime <=19 else None

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)/60
    mealTime = float(hours) + minutes
    #print(mealTime)
    return mealTime
7
if __name__ == "__main__":
    main()

"""
    if mealTime >=7 and mealTime <=8:
        print ("breakfast time")
    elif mealTime >=12 and mealTime <=13:
        print ("lunch time")
    elif mealTime >=18 and mealTime <=19:
        print ("dinner time")
    else:
        return None;
"""
