
def summm(l):
    summ = 0
    for i in l:
        summ= summ + i
    return summ        


def main():
    print("enter how many element do you want to store" )
    n = int(input())
    l = []

    for i in range(n):
        no = int(input())
        l.append(no)

    result = summm(l)
    print(result)

if __name__ == "__main__":
    main()