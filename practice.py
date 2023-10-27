a=int(input())
if(a%2==1):
    print(-1)
else:
    print("2 3")
    for i in range (3,a+1,2):
        print(f" {i+1} {i}")
        i=i+2

