
import os
print("enter file name")
name = input()

if os.path.exists(name) == True:
    print ("file existes")
else:
    print("file not exists")    