import os

print("enter first file name")
filename1 = input()

print("enter second file name")
filename2 = input()

if os.path.exists(filename1) == True  & os.path.exists(filename2):
    flag = True
    fopen = open(filename1,"r")
    data = fopen.readlines()

    fopen1 = open(filename2,"r")
    data1= fopen1.readlines()

    

    if len(data) == len(data1):
        for i in range(len(data)):
            if data[i] != data1[i]:
                flag = False
                break
        if flag == True:
            print("similar")
        else:
            print("not similar")                          
else:
    print("not exists")

