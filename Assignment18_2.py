import os

def redX(FN):

    fobj = open(FN,"r")
    print(fobj.read())



def main():
    print("enter file name")
    filename = input()

    redX(filename)


if __name__ == "__main__":
    main()    