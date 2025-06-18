class employee:
    def __init__(self,n,e,s):
        self.name = n
        self.emp_id = e 
        self.salary = s 

    def display(self):
        print(self.name,self.emp_id,self.salary)

def main():
    obj1 = employee("rohit",101,15000)
    obj1.display()

if __name__ == "__main__":
    main()            
