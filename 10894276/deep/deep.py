ans = input ("What is the Answer to the Great Question of Life, the Universe, and Everything?")

ans = ans.upper().replace("-","").replace(" ","")
if (ans=="42" or ans=="FORTYTWO"):
    print ("Yes")
else:
    print ("No")
