
def com(f,w):
    fobj = open(f,"r")
    data = fobj.read()
    
    if w in data:
        print("successful")
    else:
        print("failuer")    

    

def main():
    print("enter filename")
    filename = input()
    print("enter search word in file")
    word = input()
    com(filename,word)


if __name__ == "__main__":
    main()
