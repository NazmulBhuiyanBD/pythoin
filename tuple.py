"""
tup=(10,12,23,"green","yellow")
print(type(tup))
print(tup[-2]) #5(len)-2
print(type(tup),tup)
#tup[0]=15 ->this will show error.
#we can change list element bt we cannot change tuple element 


tup1=(10)   #this will show int class type.so we need comma(,) to tup(10,)
print(type(tup1))


tup2=tup[1:5:2] #start:end:jump index
print(tup2)

#if we want to change tuple ,so we need to convert into list then we can change it
tple=(25,"germany","canada",100,255,52,36,54,"blue","banan","fish")
temp=list(tple)
temp.pop(3)
temp.append("bangladesh")
tple=tuple(temp)
print(tple)

country1=("bangladesh","india","srilanka","nepal","vietnam")
country2=("Australia","canda","America","germany")
country=country1+country2 #we can add tuple 
print(country)
"""

digit=(2,3,5,2,3,5,6,3,5,9,3,6,3,5,3)
result=digit.count(3)
print(result)
result=digit.index(3)
print(result)
result=digit.index(3,5,12) #elemet:start:end 
print(result)
