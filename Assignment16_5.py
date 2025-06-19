def displayx(fname):

    fobj = open(fname,)
    data = fobj.readline()
    
    while data != "":
        j = 0
        for i in data:
            j = j + 1

        if j >5:
            print(data)

        data = fobj.readline()
    
    fobj.close()
    


def main():
    print("enter file name")
    fname= input()
    displayx(fname)
    

    print("file read succesfully")




if __name__ == "__main__":
    main()