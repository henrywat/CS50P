from pyfiglet import Figlet
import sys

#print(len(sys.argv))
#print(sys.argv)
font=""
figlet = Figlet()
if len(sys.argv)==1:
    pass
elif (sys.argv[1]=="-f" or sys.argv[1]=="--font") and len(sys.argv)==3 and (sys.argv[2] in figlet.getFonts()):
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

str = input("Input: ")

#print(figlet.getFonts())
if font!="":
    figlet.setFont(font=font)
print(figlet.renderText(str))
#figlet.figlet_format(str, font=font)
