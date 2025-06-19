def writex(fname):

    fobj = open(fname,"w")
    print(" enter how many numbers to store into file")
    no = int(input())

    for i in range(no):
        fobj.write(input()+"\n")

    fobj.close()    

    


def main():
    print("enter file name")
    fname= input()
    writex(fname)
    

    print("file write succesfully")




if __name__ == "__main__":
    main()