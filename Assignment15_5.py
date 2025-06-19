import os
print("enter filename")
fname = input()

print("enter string to check file it contains or not")
data = input()

if os.path.exists(fname) == True:
    count = 0
    f = open(fname,"r")
    com= f.readlines()
    
    for i in com:
        words = i.split()
        
        for j in range(len(words)):
            if words[j] == data:
                count = count+1
   

    if count == 0:
        print("not contains")
    else:
        print("contains")
        print("frequency is " , count)    


