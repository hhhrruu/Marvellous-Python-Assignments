import os

print("enter file name")
filename = input()

have = os.path.exists(filename)

if have == True:
    f = open(filename, "r")
    data = f.read()
    if data != None:
        print("enter file name to copy existing file data")
        cfile = input()
        crfile = open(cfile,"w")
        crfile.write(data)
        crfile.close()
    f.close()
else:
    print("file is not exists")    



