"""
x=10
def pk():
    y=5
    print(x)

#print(y) #this will gives us error .we cannot print this y


"""
#if we want to change X variable value

x=15
def ck():
    global x
    x=7
    print(f"this is in the function {x}")


ck()
print(f"this is in the global {x}")
