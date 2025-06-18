print("enter first number ")
num = int(input())

print("enter second number ")
num1 = int(input())

print("enter third number ")
num2 = int(input())

if num > num1 and num > num2:
    print("gretest number is",num)
elif num1 > num2 and num > num:
     print("gretest number is",num1) 
else:
    print("gretest number is",num2)                  