class demo:
    values = 0
    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b

    def fun(self):
        print("fun values ",self.no1 ,self.no2)

    def gun(self):
        print("gun values ",self.no1 ,self.no2)


def main():
    obj1 = demo(11,21)
    obj2 = demo(31,51)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()


if __name__ == "__main__":
    main()    