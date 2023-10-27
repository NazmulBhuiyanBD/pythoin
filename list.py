"""list1=[10,25,35,"nazmul",True,22,55,98,15]

print(type(list1))
print(list1[0])

print(list1[-3]) #len(5-3)=index ->2

if 10 in list1:
    print("yes")
else:
    print("NO")
    

print(list1)
print(list1[1:])    #[1:len(list)] automatically 
print(list1[:4])    #[0:4]
print(list1[1:-2])  #[1:5-2=3] 
print(list1[1:9:2])  #[1:5-2=3] 


list2=[i for i in range(4)] 
print(list2)

list2=[i*i for i in range(8) if i%2==0]
print(list2) 


l=[10,22,36,5,6,9,35]
print(l)
print(l.index(36))
l.append(12)
print(l)

l.sort()
print(l)
l.sort(reverse=True)    #decending order
print(l)"""


lis=[10,25,322,25,4,54]
m=lis
m[0]=5
print(lis)

lis.insert(1,12) #insert at 1 index value->12
print(lis)

p=[100,200,3000]
lis.extend(p)   #it will add p value into the lis
print(lis)      #we can use k=lis+p

