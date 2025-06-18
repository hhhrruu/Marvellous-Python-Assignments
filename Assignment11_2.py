i = 1
mul = 1
def fact(no):
    global i
    global mul 
    if no >= i:
        mul = mul * no
        no = no - 1
        fact(no)
    return mul     
    


def main():
    res = fact(5)
    print("factorial is ", res)



if __name__ == "__main__":
    main()