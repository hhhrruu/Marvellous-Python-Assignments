import sys
import os

def copyX(FN):

    fobj = open(FN,"r")
    data = fobj.read()

    cobj = open("Demo.txt","w")
    cobj.write(data)

    fobj.close()
    cobj.close()


def main():
    
    copyX(sys.argv[1])


if __name__ == "__main__":
    main()    