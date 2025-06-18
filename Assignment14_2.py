class rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w 
         

    def area(self):
        print("are of rectangle is",self.length * self.width)

    def perimeter(self):  
        print("perimeter of rectangle is",2 * (self.length + self.width))  
        


def main():
    obj1 = rectangle(5,6)
    obj1.area()
    obj1.perimeter()

if __name__ == "__main__":
    main()            
