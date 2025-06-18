import marvellousnum

def main():
    print("enter how many element do you want to store" )
    n = int(input())
    l = []
    result = 0 
    t = None

    for i in range(n):
        no = int(input())
        l.append(no)

    for i in l:
        t = marvellousnum.prime(i)
        if t == True:
            result = result + i

    print(result)        

    

if __name__ == "__main__":
    main()