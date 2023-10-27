"""
p=open('pok.txt','r')   #open('pok.txt') ->this can work.default mode is reading
#print(p)
text=p.read()
print(text)
p.close()

#for writing
p=open('pok.txt','w')
text2=p.write("hello this is nazmul .nice to meet you.")
p.close()


p=open('pok.txt','a')
text3=p.write(" again write this file.")
p.close()

p=open('pok.txt','r')
while True:
    line=p.readline()
    if not line:
        break
    print(line)

f=open('marks.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"{i} student math marks {m1}")
    print(f"{i} student  physics marks {m2}")
    print(f"{i} student  english marks {m3}")
    print(line)"""


#seek()
p=open('pok.txt','r')
p.seek(10) #first 10 will not print
data=p.read(15)
print(data)