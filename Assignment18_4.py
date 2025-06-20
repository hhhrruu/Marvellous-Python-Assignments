import os
import hashlib

def checkksum(f1,f2):
    fobj1 = open(f1,"rb")
    fobj2 = open(f2,"rb")

    hobj1 = hashlib.md5()
    hobj2 = hashlib.md5()


    buffer1 = fobj1.read(1024)
    buffer2 = fobj2.read(1024)

    while(len(buffer1) > 0 and  len(buffer2) >0):
        hobj1.update(buffer1)
        hobj2.update(buffer2)

        buffer1 =fobj1.read(1024)
        buffer2 = fobj2.read(1024)

    print(hobj1.hexdigest())
    print(hobj2.hexdigest())
    if hobj1.hexdigest() == hobj2.hexdigest():
        print("successfull")
    else:
        print("failuar")    
    


def main():
    print("enter file name")
    file1 = input()
    file2 = input()
    checkksum(file1,file2)


if  __name__ == "__main__":
    main()