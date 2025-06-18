l = []
print("enter how many bnumbers do you want to store")
num = int(input())

for i in range(0,num):
    l.append(int(input())) 

max = l[0] 

for i in range(1,num):
    if max < l[i]:
        max = l[i]


print(max)        



