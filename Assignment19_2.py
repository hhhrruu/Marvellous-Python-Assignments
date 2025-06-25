import os
import sys

def changeexe(dname,ext,cext):

    flag = os.path.isabs(dname)
    if flag == False:
        dname = os.path.abspath(dname)

    flag = os.path.exists(dname)
    if flag == False:
        print("the path is invalid")  
        exit()

    flag = os.path.isdir(dname)
    if flag == False:
        print("path is valid but target is not directory")
        exit()
   
    
    Nfilename ="."+cext
    for Foldername,subfoldername,filename in os.walk(dname):
        for FN in filename:
            #print(os.path.join(Foldername,FN)) got full path of file
            oldfilepath = os.path.join(Foldername,FN)
            
            CRNF = FN.split(".")
            if CRNF[1] == ext:
                Newname  = CRNF[0]+"."+cext # creating new file name
                newfilepath =  os.path.join(Foldername,Newname) # creating new file path 
                os.replace(oldfilepath,newfilepath) #replacing new path to old path
                     

def main():
    changeexe(sys.argv[1],sys.argv[2],sys.argv[3])
    
    

if __name__ == "__main__":
    main()