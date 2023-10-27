question=[["who is the prime minister of bangladesh?","mujib","hasina","zia","khaleda",2],["who is the prime minister of bangladesh?","mujib","hasina","zia","khaleda",2],["who is the prime minister of bangladesh?","mujib","hasina","zia","khaleda",2],["who is the prime minister of bangladesh?","mujib","hasina","zia","khaleda",2]]
level=[1000,2000,4000,8000,16000,32000]
money=0
for i in range(4):
    print(f"{question[i][0]}")
    print(f"a.{question[i][1]}      b.{question[i][2]} \nc.{question[i][3]}        d.{question[i][4]}")
    a=int(input("what is your answer?"))
    if(a==question[i][5]):
        money=level[i]
    else:
        break
print(money)