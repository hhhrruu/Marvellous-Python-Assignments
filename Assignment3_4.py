
def occurance(l,no):
    count =0
    for i in l:
        if i == no :
            count = count +1
    return count          


def main():
    print("enter how many element do you want to store" )
    n = int(input())
    l = []

    for i in range(n):
        no = int(input())
        l.append(no)

    print("element to search")
    s = int(input())


    result = occurance(l,s)
    print(result)

if __name__ == "__main__":
    main()