print("enter number")
num = int(input())

f = True
for i in range(2,num):
    if num % i == 0:
        f = False


if f == True:
    print("prime number")
else:
    print("not prime number")

