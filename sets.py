
"""
#sets are defined as the collection of objects ->unorder 
s={5,10,25,5}
print(s) #only one 5 will print
s2={10,12,"BMW","toyota",11,12}
print(s2,s)

for i in s2:
    print(i)

#empty sets
empt=set()
print(type(empt))

print(s.union(s2)) #now it will print s sets and s2
s.update(s2)
print(s)

cities1={"dhaka","delhi","islamabad"}
cities2={"tokyo","seoul","kabul","madrid","barlin","dhaka"}
cities1.add("Colombo")

cities3=cities1.union(cities2)
print(cities3)
cities3=cities1.intersection(cities2)
print(cities3)
cities3=cities1.symmetric_difference(cities2)
print(cities3)
#disjoint sets
print(cities1.isdisjoint(cities2))
print(cities1.issuperset(cities2))

cities2.remove("tokyo") #if it doesnt find the then it will show error
print(cities2)
#or we can use discard
cities2.discard("tokyogg") #if it doesnt find the then it will show error
print(cities2)"""

p={10,22,35,25}
item=p.pop()
print(p)
print(item)