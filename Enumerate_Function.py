num=[15,20,25,98,5,63]

"""
i=0
for number in num:
    print(number)
    if(i==3):
        print("Good boy")
    i+=1
"""
#we can write this code with another form
for j,number in enumerate(num):
    print(number)
    if(j==3):
        print("Good boy")