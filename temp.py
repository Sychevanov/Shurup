import random
n=int(input('Enter n: '))
a= [ random.randint(-5,10) for i in range(0,n)]
print(a)
temp=False
for i in range(len(a)):
    if a[i]<0:
        temp=True
        break

if temp:
    print('Yes')
else:
    print('No!')
