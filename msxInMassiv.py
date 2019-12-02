import random
n=int(input('Enter n: '))
a= [ random.randint(-5,10) for i in range(0,n)]
c=a[0]
print(a)
for i in range(0,len(a)):
    if c<a[i]:
        c=a[i]
j=0    
while c!=a[j]:
    j=j+1
print(f'{j}. {c}')
