class product:
    def __init__(self ,a,b):
        self.name = a 
        self.price = b 

    def __eq__(self,other):
        return self.price == other.price    


obj1 = product("laptop",25000)
obj2 = product("mobile",25000)
obj3 = product("earburds",2500)

print(obj1 == obj2)
print(obj1 == obj3)