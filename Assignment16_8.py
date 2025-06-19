
def display(filename):
    fobj = open(filename,"r")
    nobj = open("neww.txt","w")
    data=fobj.read()

    for i in data:

        if i == "\n":
            nobj.write("\n")
        else :
            nobj.write(i)



def main():
    fobj = open("marks.txt","w")

    fobj.writelines("prakash"+"=" + "78" +"\n")
    fobj.writelines("mahesh" +"="+ "70"+"\n")
    fobj.writelines("omkar"+"="+"76"+"\n")
    fobj.close()
    display("marks.txt")


if __name__ == "__main__":
    main()