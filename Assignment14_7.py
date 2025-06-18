class person:
    def __init__(self , n,a):
        self.name = n 
        self.age = a 


class teacher(person):
    
    def __init__(self,s,ss):
        self.subject = s 
        self.salary = ss
        super().__init__("piyush",55)
        
    def display(self):
        print(self.subject,self.salary)
        print(self.name,self.age)



obj1=teacher("It","infinite")

obj1.display()
