from  functools import reduce

f = lambda a : ((a >= 70) & (a<=90))

m = lambda a : a + 10

r = lambda a ,b : a*b
def main():
    print("enter how many element do you want to store")
    no = int(input())
    l = []

    for i in range(0,no):
        l.append(int(input()))

    fres = list(filter(f,l))
    print(fres)

    mres = list(map(m,fres))
    print(mres)
    rres = reduce(r,mres)

    print("FINAL RESULT is ",rres)


if __name__ == "__main__":
    main()