
from functools import reduce

def cond(l):
    if  l >= 70 and l <=  90:
        return True  

add = lambda a : a+10

mull = lambda A ,B : A * B 

def main():
    a = []
    print("enter how many element do you want to store")
    n = int(input())

    for i in range(n):
        a.append(int(input()))

    f = list(filter(cond,a)) 
    print(f)  

    m = list(map(add,f))
    print(m)

    f = reduce(mull,m)
    print(f)

if __name__ == "__main__":
    main()
