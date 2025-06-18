print("enter how many numbers do you want to store")
no = int(input())
l = []
n = []
def prime(noo):
    
    for i  in range(2,no):
        if noo % i ==0:
            return False

    return True        


for i in range(0,no):
    l.append(int(input("enter number")))

for i in range(0,no):
    f = prime(l[i])
    if f == True:
        n.append(l[i])

print(n)        
