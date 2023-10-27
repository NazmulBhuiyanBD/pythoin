x=int(input("Enter Your age"))

match x:
    case 0:
        print("zero")
    case _ if x>=10:
        print(x," is greater than 10")
    case _ if x>100:
        print(x,"is greater than 100")
    case _:
        print(x)