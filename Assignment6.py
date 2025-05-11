 

def ChkNum(number):
    if(number == 0):
        print("Zero")
    elif(number <= -1):
        print("Negative")
    elif(number > 0):
        print("positive")





def main():
    print("enter number i will check it is even or odd")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()    


