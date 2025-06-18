class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        print("enter number")
        no = int(input())
        no1 = int(input())
        self.value1 = no
        self.value2 = no1

    def addition(self):
        return self.value1 + self.value2

    def subtraction(self):
        return self.value1 - self.value2    

    def mult(self):
        return self.value1 * self.value2 

    def division(self):
        return self.value1 / self.value2

def main():
    obj1 = Arithmatic()
    obj1.Accept()

    res = obj1.addition()
    print("addition is",res)

    res = obj1.subtraction()
    print("subtraction is",res)

    res = obj1.mult()
    print("multipliction is",res)

    res = obj1.division()
    print("division is ",res)

if __name__ == "__main__":
    main()                         

