import os

def writeX(fname):
    print("enter how many student data you want to store into file")
    no =int(input())
    NL = []
    for i in range(no):
        NL.append(input())

    if os.path.exists(fname) == True:
        fobj = open(fname , "a")
        
        for i in range(no):
            fobj.write("\n"+NL[i])

        fobj.close()    


def createX(fname):

    fobj = open(fname,"w")
    fobj.close()
    


def main():
    print("enter file name")
    fname= input()
    createX(fname)
    writeX(fname)

    print("file create and data written succesfully")




if __name__ == "__main__":
    main()