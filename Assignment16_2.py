def readX(fname):

    fobj = open(fname,)
    print(fobj.read())
    fobj.close()
    


def main():
    print("enter file name")
    fname= input()
    readX(fname)
    

    print("file read succesfully")




if __name__ == "__main__":
    main()