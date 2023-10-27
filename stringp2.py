"""
 #string formating
letter="MY name is {} & i am from {}"
country="bangladesh"
name="nazmul"
print(letter.format(name,country))

letter="MY name is {1} & i am from {0}"
print(letter.format(name,country))

print(f"MY name is {name} & i am from {country}")   #or we can write this way

txt="this is only{price:.2f} dollar"
print(txt.format(price=20.49996))

#if we want to print {} then we need another {}
print(f"MY name is {{name}} & i am from {{country}}")
"""


#docstring 
#docstring will be right below the function name
def square(n):
    '''helo this is nazmul.i am in the docstring now'''
    print(n**2)
square(5)
print(square.__doc__)