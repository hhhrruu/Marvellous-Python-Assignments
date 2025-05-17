print("ENTER NUMBER")
A = int(input())
j= 0 
for i in range(2,A):
    if A % i == 0:
        j = 1

if  j  == 0:
    print("this is prime number ")
else :
    print("this is not a prime")    



