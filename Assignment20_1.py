import hashlib
import sys
import os

def chksum(dname):

    for FN , SF ,FNS in os.walk(dname):
        for fn in FNS:
            fobj = open(os.path.join(FN,fn),"rb")
            hobj = hashlib.md5()
            data = fobj.read(1024)
            while len(data) > 0:
                hobj.update(data)
                data = fobj.read(1024)

            fobj.close()
            print(hobj.hexdigest())    


def main():
    chksum(sys.argv[1])    

if __name__ == "__main__":
    main()