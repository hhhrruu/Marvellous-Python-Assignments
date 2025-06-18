print("enter how many numbers do you want to store")
no = int(input())
l = []

d = lambda a :a + a


for i in range(0,no):
    l.append(int(input()))


n  = list(map(d,l))

print(n)