import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        err_count=0
        x=generate_integer(level)
        y=generate_integer(level)
        z=x+y
        while True:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess==z:
                    score += 1
                    break
                else:
                    err_count += 1
                    print("EEE")
            except ValueError:
                err_count += 1
                print("EEE")
                pass

            if err_count==3:
                print(f"{x} + {y} = {z}")
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0<level<4:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)



if __name__ == "__main__":
    main()
