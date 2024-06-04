import sys, os, PIL
from PIL import Image

args = sys.argv
if len(args) < 3:
    sys.exit("Too few command-line arguments")
elif len(args) > 3:
    sys.exit("Too many command-line arguments")

filein = args[1].strip()
fileout = args[2].strip()
filemask = "shirt.png" #595x176
suffixin = os.path.splitext(filein)[1].lower()
suffixout = os.path.splitext(fileout)[1].lower()
suffixlist = [".jpg", ".jpeg", ".png"]
if not suffixout in suffixlist or not suffixin in suffixlist:
    sys.exit("Invalid input ")
elif suffixin != suffixout:
    sys.exit("Input and output have different extensions")

try:
    imgshirt = Image.open(filemask)
    imgin = Image.open(filein)
    imgout = PIL.ImageOps.fit(imgin, imgshirt.size)
    imgout.paste(imgshirt, imgshirt)
    imgout.save(fileout)
except FileNotFoundError:
    sys.exit(f"{filein} Not Found")

sys.exit()
