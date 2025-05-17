print("ENTER NUMBER i will return the count of how many numbers present in that number ")
N = int(input())

no = N
summ = 0
while no != 0:
   
    p = int(no % 10)
    summ = summ + p
    no =int( no / 10)

print("digit total is" , summ)         