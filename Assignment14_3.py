class Book:
    def __init__(self,p):
        self.__price = p
         

    def get(self):
        print("price of book is",self.__price)

    def seet(self,pp):
        print("inside set")
        self.__price = pp
        print(self.__price)
        


def main():
    obj1 = Book(101)
    obj1.get()
    obj1.seet(201)
    obj1.get()

if __name__ == "__main__":
    main()            
