
from functools import reduce

cond = lambda a : not(a % 2)

sqr = lambda a : a * a

red = lambda A ,B : A + B 

def main():
    a = []
    print("enter how many element do you want to store")
    n = int(input())

    for i in range(n):
        a.append(int(input()))

    f = list(filter(cond,a)) 
    print(f)  

    m = list(map(sqr,f))
    print(m)

    f = reduce(red,m)
    print(f)

if __name__ == "__main__":
    main()
