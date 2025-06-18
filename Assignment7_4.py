from functools import reduce

print("enter how many numbers do you want to store")
no = int(input())
l = []

pr = lambda a , b: a * b 


for i in range(0,no):
    l.append(int(input()))


n  = reduce(pr,l)

print(n)
