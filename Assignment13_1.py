class BookStore:
    NoofBooks = 0  
    def __init__(self ,N,A):
        self.name = N 
        self.author = A
        BookStore.NoofBooks = BookStore.NoofBooks + 1

    def Display(self):
        print(f"{self.name} By {self.author} No of books is{BookStore.NoofBooks}")    




def main():
    obj1 = BookStore("Linux system programming","Robert love")
    obj1.Display()

    obj2 = BookStore("c programming ","dennis ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()    
