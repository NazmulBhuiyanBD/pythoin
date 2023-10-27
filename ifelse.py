"""
a=int(input("Enter Your age"))
if(a>18):
    print("you can drive")
else:
    print("No")
print(a>18)
print(a<18)
print(a==18)
print(a!=18)


appl=20
budget=25
if(appl<=budget):print("YEs")
elif(budget-appl>=0):print("Yes")
else:print("NO")


a=int(input("Enter your age"))
b=input("enter your gender")
if(a>18):
    if(b=="male"):
        print("YEs Your drive")
    elif(a>25):
        print("Yes You can drive")
    else:
        print("You cannot drive")
else:
    print("You cannot drive")"""




#short-hand if else

s=10
t=20
print("A")if(s>t) else print("B")if(s==t)else print("A+B")

c=9 if s>t else 0
print(c)
