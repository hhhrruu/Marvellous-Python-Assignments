
from functools import reduce

def con(a):
    flag = True
    for i in range(2,a):
        if a %i == 0 :
            flag=False
           
    if flag == True:
        print(a)
        return True
    else :
        return False        

mul = lambda a : a * 2

def maxx(a,b):
    if a > b:
        return A
    else:
        return b    


def main():
    a = []
    print("enter how many element do you want to store")
    n = int(input())

    for i in range(n): 
        a.append(int(input()))

    f = list(filter(con,a)) 
    print(f)  

    m = list(map(mul,f))
    print(m)

    f = reduce(maxx,m)
    print(f)

if __name__ == "__main__":
    main()
