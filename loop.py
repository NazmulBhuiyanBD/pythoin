"""
    name="Nazmul"
for i in name:
    print(i)
    if i=="a":
        print("Thank you")
for i in name:
    print(i,end=",")
colors=["red","green","blue","yellow"]
for color in colors:
    print(color)
for color in colors:
    print(color)
    for i in color:
        print(i)
for k in range(5):
    print(k)        #this will print 0-4
for k in range(5,10):
    print(k)        #this will print 5 to 9
   
for i in range(1,12,2):
    print(i)
    
    

#while loop
i=0
while(i<=30):
    print(i)
    i=i+1
else:
    print("I am in the else estatement")
"""
for i in range(1,12):
    if(i==10):
        break
    print(i)
for i in range(1,12):
    if(i==10):
       continue
    print(i)
"""for i in range(5):
    print(i)
else:
    print("NO i remaining")
    """

for i in []:
    print(i)
else:
    print("NO ")

i=0
while(i<7):
    print(i)
    if(i==4):
        break
    i=i+1
else:
    print("this is outisde the loop")