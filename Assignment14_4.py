class student:
    school_name= "marvellous info system"

    def __init__(self,n,r):
        self.name=n 
        self.roll_no = r 

    def display(self):
        print(f"schoolname is {student.school_name} student name is {self.name} and roll number is {self.roll_no}")




obj1 = student("hrushikesh",101)
obj1.display()            