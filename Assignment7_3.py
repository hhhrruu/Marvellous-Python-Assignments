print("enter how many numbers do you want to store")
no = int(input())
l = []

ev = lambda a : a % 2 == 0 


for i in range(0,no):
    l.append(int(input()))


n  = list(filter(ev,l))

print(n)