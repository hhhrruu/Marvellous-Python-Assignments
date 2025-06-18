class BankAccount:
    ROI = 10.5
    def __init__(self,N,A):
        self.Name = N
        self.Amount = A 

    def Display(self):
        print("Name account",self.Name)
        print("Amount in bank",self.Amount)

    def Deposit(self,d):
        self.Amount = self.Amount + d 

    def withdraw(self,w):
        self.Amount = self.Amount - w 


    def Calculateintrest(self):
        SI = (self.Amount * BankAccount.ROI * 365) / 36500            


def main():
    obj1 = BankAccount("piyush",100000000)
    obj1.Deposit(10000)
    obj1.withdraw(50000)
    obj1.Calculateintrest()
    obj1.Display()
    

if __name__ == "__main__":
    main()    
