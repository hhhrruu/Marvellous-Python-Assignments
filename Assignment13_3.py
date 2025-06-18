class Numbers:
    NoofBooks = 0  
    def __init__(self ,N):
        self.value = N

    def chkprime(self):
        flag = True
        for i in range(2,self.value):
            if self.value % i == 0:
                flag = False
                break
        return flag        

    def chkperfect(self , j= 0):
        flag = True
        add = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                add = add +i

        if j == 1 :
            return add

        if add == self.value:
            flag = True
        else:
            flag = False

        

        return flag              


    def factor(self):

        for i in range(1,self.value):
            if self.value % i == 0:
                print( f"factor of {self.value} is " ,i )
       

    def sumfactor(self):   
        return self.chkperfect(1)         



def main():
    print("enter number")
    no = int(input())
    obj1 = Numbers(no)
    
    print("ststus of number is prime or not  :=  ",obj1.chkprime())
    print("status of number is perfect or not := ",obj1.chkperfect())
    obj1.factor()
    print("sum of factor is := ",obj1.sumfactor())

if __name__ == "__main__":
    main()    
