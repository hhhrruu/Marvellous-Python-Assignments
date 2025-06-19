
import os
print("enter file name")
name = input()

if os.path.exists(name) == True:
    f = open(name,'r')
    data = f.read()
    print(data)

else:
    print("file not exists")    