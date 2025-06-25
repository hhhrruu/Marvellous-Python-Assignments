import os
import sys

def display(DNAME,ext):
    for FN,SFN,FNN in os.walk(DNAME):
        for fn in FNN:
           # print(fn.split(".")) [filename , extension ]
            data = fn.split(".")            
            if data[1] == ext:
                print(fn)



def main():
    display(sys.argv[1],sys.argv[2])
    

if __name__ == "__main__":
    main()