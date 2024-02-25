import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s=s.strip()
    if re.search(r"^<iframe.+[s][r][c].+[h][t][t][p].+[y][o][u][t][u][b][e].+iframe>$", s):
        temp = s.split("src")
        temp = temp[1].replace("=", "")
        temp = temp.split("\"")
        temp = temp[1]
        temp = temp.split("embed/")
        temp = temp[1]
        return (f"https://youtu.be/{temp}")
    else:
        return None



if __name__ == "__main__":
    main()