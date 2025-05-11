 

def ChkNum(number):
    if(number % 5 ==0):
        return  True
    else:
        return False    





def main():
    print("enter number i will check it is even or odd")
    num = int(input())
    val=ChkNum(num)
    print(val)
if __name__ == "__main__":
    main()    


