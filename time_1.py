import time

time1 = time.strftime('%H:%M:%S')
print(time1)

time1 =int(time.strftime('%M'))
print(time1)
time1 =int(time.strftime('%S'))
print(time1)
time1 =int(time.strftime('%H'))
print(time1)

if (time1>=6 and time1 <=12):
    print('Good Morning')
elif (time1>=12 and time1 <=16):
    print('Good afternoon')
elif (time1>=4 and time1 <=6):
    print('Good evining')

else :
    print('Good night')