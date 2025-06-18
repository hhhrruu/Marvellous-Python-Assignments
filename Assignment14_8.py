class vehical:
    def start(self):
        print("start from base")


class car(vehical):
    def start(self):
        print("start from car")


obj1 = car()
obj1.start()