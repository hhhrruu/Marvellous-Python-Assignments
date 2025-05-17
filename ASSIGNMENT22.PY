import ASSIGNMENT21 

print("choose whivh operation do you want to do ")
print("addition == 1")
print("subtraction == 2")
print("division == 3")
print(" multiplication == 4")

choice = int(input())

if choice == 1:
    print("enter two number")
    a = int(input())
    b=int(input())

    c = ASSIGNMENT21.ADD(a,b)
    print( "ADDITION IS " , c)

elif choice == 2:
    print("enter two number")
    a = int(input())
    b=int(input())

    if a > b:
        c = ASSIGNMENT21.SUB(V1 = a, V2=b)
        print("Subtraction is " ,c)
    else:
        c = ASSIGNMENT21.SUB(V1 = b, V2=a)
        print("Subtraction is " ,c)
elif choice == 3:
    print("enter two number")
    a =int(input())
    b=int(input())

    if a > b:
        c = ASSIGNMENT21.DIV(V1 = a, V2=b)
        print("Division is " ,c)
    else:
        c = ASSIGNMENT21.SUB(V1 = b, V2=a)
        print("Division is " ,c)

elif choice == 4:
    print("enter two number")
    a =int(input())
    b=int(input())

    c = ASSIGNMENT21.MULT(a,b)
    print("multiplication is",c)
else:
     print("please enter currect choice")


    