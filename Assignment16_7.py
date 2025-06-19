
def display(filename):
    fobj = open(filename,"r")
    data=fobj.readline()

    while data != "":
        d = data.split("=")
        #print(d[1]) get marks here
        #print(type(d[1])) need to typecast 
        if int(d[1]) > 75:
            print("stude name who scored more than 75",d[0])
        
        data = fobj.readline()



def main():
    fobj = open("marks.txt","w")

    fobj.writelines("prakash"+"=" + "78" +"\n")
    fobj.writelines("mahesh" +"="+ "70"+"\n")
    fobj.writelines("omkar"+"="+"76"+"\n")
    fobj.close()
    display("marks.txt")


if __name__ == "__main__":
    main()