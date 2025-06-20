import os

def chekexists(FN):

    if os.path.exists(FN):
        print("file exists")
    else:
        print("file is not exists")



def main():
    print("enter file name")
    filename = input()

    chekexists(filename)


if __name__ == "__main__":
    main()    