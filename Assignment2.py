

def ChkNum(number):
    if(number %2 == 0):
        print("this number is even number")
    else:
        print("this is odd number")     




def main():
    print("enter number i will check it is even or odd")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()    


