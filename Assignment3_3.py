
def minnn(l):
    minn = l[0]
    for i in range(1,len(l)):
        if minn > l[i] :
            minn = l[i]
    return minn        


def main():
    print("enter how many element do you want to store" )
    n = int(input())
    l = []

    for i in range(n):
        no = int(input())
        l.append(no)

    result = minnn(l)
    print(result)

if __name__ == "__main__":
    main()