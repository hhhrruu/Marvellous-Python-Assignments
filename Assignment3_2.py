
def maxxx(l):
    maxx = 0
    for i in l:
        if maxx < i:
            maxx = i
    return maxx        


def main():
    print("enter how many element do you want to store" )
    n = int(input())
    l = []

    for i in range(n):
        no = int(input())
        l.append(no)

    result = maxxx(l)
    print(result)

if __name__ == "__main__":
    main()