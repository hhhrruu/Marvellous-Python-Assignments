print("ENTER NUMBER i will return the count of how many numbers present in that number ")
N = int(input())

no = N
count = 0
while no != 0:
   
    p = int(no % 10)
    count = count +1
    no =int( no / 10)

print("digit are" , count)         