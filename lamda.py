"""
def dbl(x):
    return x*2
print(dbl(10))

"""
dbl=lambda x:x*2
print(dbl(10))

avg=lambda a,b:(a+b)/2
print(avg(10,12))

def app(a,gx):
    return a+ gx(a)

#print(app(10,dbl))
print(app(2,lambda x:x*x))

