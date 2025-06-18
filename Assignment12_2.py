class circle:
    PI = 3.14
    def __init__(self):
        self.radius = 0.0 
        self.Area = 0.0
        self.circumferance = 0.0

    def accept(self):
        print("enter radius value")
        self.radius = float(input())

    def calculatearea(self):
        self.Area = circle.PI * (self.radius * self.radius)


    def calculatecircumferance(self): 
        self.circumferance = 2 * circle.PI * self.radius

    def display(self):
        print("radius is",self.radius)
        print("area of circle" , self.Area)
        print("circumfarance of circle is",self.circumfe rance)


def main():
    obj1 = circle()
    obj1.accept()
    obj1.calculatearea()
    obj1.calculatecircumferance()
    obj1.display()

if __name__ == "__main__":
    main()    