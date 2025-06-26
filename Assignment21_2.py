import sys
import hashlib
import os

def wfile(data,path):
    pathh = path+"\log.txt"
   
    
    fobj = open(pathh,"w")

    for i in data:
        if len(data[i]) > 1:
            for j in range(1,len(data[i])):
                    wd = data[i][j].split(os.getcwd())
                    fobj.write(wd[1]+"\n")
    

def chksum(dictname):
    adc = os.path.abspath(dictname) 


    for foldername,subfoldernamesn,filenames in os.walk(adc):

        dataset = {}
        for Fn in filenames:
            Fn = os.path.join(foldername,Fn)
            fobj =  open(Fn,"rb")
            data = fobj.read(1024)
            hobj = hashlib.md5()

            while len(data) >0:
                hobj.update(data)
                data = fobj.read()

            chk = hobj.hexdigest()
            if chk in dataset:    
                dataset[chk].append(Fn)
            else:
                dataset[chk] = [Fn]     

        wfile(dataset,adc)          






def main():
    chksum(sys.argv[1])



if __name__ == "__main__":
    main()