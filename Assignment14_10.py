class employee:
    def __init__(self,name,salary,department):
        self.name=name
        self._department = department
        self.__salary = salary

    def privaccess(self):
        print("private access " , self.__salary)

class man(employee):

    def __init__(slef ,a,b,c):
        super().__init__(a,b,c)

    def protected(self):
        print("access protected",self._department)
        #print(self.__salary)


def main():
    obj1 = man("hk",150000,"IT")
    print(obj1._department) #access
    #print(obj1.__salary) no access
    obj1.protected()
    obj1.privaccess()

main()