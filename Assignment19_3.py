import os
import sys


def changedirectory(presentdir,changedir):

    d =os.path.abspath(presentdir)
    if not os.path.isabs(presentdir):
        d =os.path.abspath(presentdir)
        
        
        

    if not os.path.exists(presentdir):
        print("path is not exists")
        exit()

    if not os.path.isdir(presentdir):
        prinT("its not a directory")
        exit()


    for Foldername , SubFoldername,Filename in os.walk(presentdir):
       # new = d.replace(presentdir,changedir)
        #print(new)
        #print(new)
        for fn in Filename:
            odp =os.path.join(d,fn) 
            np = odp.replace(presentdir,changedir)
            os.replace(odp,np)
            print(np)    




def main():
    changedirectory(sys.argv[1],sys.argv[2]) 


if __name__ == "__main__":
    main()