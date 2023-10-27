import string
import random

a=input("Enter your msg : ")
p=input("encoding press 1 ,for decoding press 0")
coding=True
nword=[]
N=3
coding=True if(p=="1") else False
words=a.split()
if(coding):
    for word in words:

        if(len(word)>=3):
            r=''.join(random.choices(string.ascii_letters, k=N))
            q=''.join(random.choices(string.ascii_letters, k=N))
            
            
            stnew=r+word[1:]+word[0]+q
        else:
            stnew=word[::-1]
        nword.append(stnew)
    print(" ".join(nword))
else:
    for word in words:

        if(len(word)>=3):
            
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
        else:
            stnew=word[::-1]
        nword.append(stnew)
    print(" ".join(nword))