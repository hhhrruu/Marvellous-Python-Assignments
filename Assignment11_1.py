i = 5

def display(no):
    global i 
    if no <= i:
        print(no)
        no = no+1
        display(no)    

def main():

    display(1)



if __name__ == "__main__":
    main()
