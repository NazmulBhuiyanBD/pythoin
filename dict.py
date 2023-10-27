
"""
dict={
    "nazmul":"human ",
    "haque":"student",
    "bhuian":"worker"
}
print(dict["nazmul"])
print(dict.get("nazmul2")) #if we dont want to get error then we need to use this one
print(dict.keys()) #this will show all keys
print(dict.values()) #this will show all values

for key in dict.keys():
    print(dict[key])
"""

ep1={1:"nazmul",2:"haque",3:"bhuiyan"}
ep2={4:"sayem",5:"NHB"}
#ep1.update(ep2)
#ep1.pop(2)
#ep1.clear()
#del ep1 ->delete ep1
del ep1[1]
print(ep1)
ep1.popitem() #->this will remove last element
print(ep1)