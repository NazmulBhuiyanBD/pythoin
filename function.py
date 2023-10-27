
def area(a,b):
    rectangle=a*b
    print(rectangle)

a=10
b=20
area(a,b)


def average(a=10,b=20):
    print((a+b)/2)

average(a=5)        #we can pass only one argument
average(b=5)        #we can pass only one argument

def name(fname,mname="Haque",lname="bhuiyan"):
    print("Your name is ",fname,mname,lname)

name("Nazmul ")
name("Nazmul ",lname="sayeem")


def avg(*marks):    #here marks will be use as a tuple
    sum=0
    print(type(marks))
    for i in marks:
        sum=sum+i
    print(sum)
avg(5,10,25,30)     


def word(**word):
    print(type(word))
    print("hello this is dictionary \n",word["cat"],word["dog"],word["fish"])

word(cat="biral",dog="kutta",fish="mas")
