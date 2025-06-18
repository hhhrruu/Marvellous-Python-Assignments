print("enter string")
s = input()
l = len(s) - 1
f =True

print(l)
for i in range(0,len(s)):
    print(s[i] ,s[l])
    if s[i] != s[l]:
        f = False
        break

    l = l-1    

if f == True:
    print("it is pallendrome")
else:
    print("its not pallendrome")        