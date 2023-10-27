"""

n=int(input())
print(f"You enter {n} digit")
try:
    for i in range(n):
        print(i)
except Exception as e:
    print("You are wrong ")
print("thanksg")


try:
    num=int(input("entrer your digit"))
    a=[5,3]
    print(a[num])
except ValueError:
    print("enter a correct value")
except IndexError:
    print("enter a correct index")



def fun():
    try:
        l=[1,2,3,4]
        i=int(input())
        print(l[i])
        return 1
    except:
        print("please try other digit")
        return 0
    #finally:
        print("I am always executed")


fun()"""



p=int(input())
if(p<5 or p>10):
    raise ValueError("Your should enter your value between 5 to 10")