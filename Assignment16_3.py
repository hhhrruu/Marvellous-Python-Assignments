def readX(fname):
#to count how many characters in the files    
    char = 0
    fobj = open(fname,)
    l = fobj.read()
    for i in l:
        char = char +1
    fobj.close()

# to count how many lines in the file
    fobj = open(fname,)
    f = fobj.readline()
    rl=0
    while f != "":
        rl = rl + 1
        f = fobj.readline()
    fobj.close()

# to count how many words in file
    fobj = open(fname,)
    data = fobj.readlines()
    rw = 0
    for i in data:
        words = i.split()
        rw = rw + len(words)   
    fobj.close()

    print("words  presents count in the file is " , rw) 
    print("lines  presents count in the file is " , rl)    
    print("characters presents count in the file is " , char)
    
    
def main():
    print("enter file name")
    fname= input()
    readX(fname)
    print("file read succesfully")
 
if __name__ == "__main__":
    main()