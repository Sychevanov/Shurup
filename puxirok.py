import random
n = int(input('Enter n: '))
a = [random.randint(0,10) for i in range(0,n)]
print(a)
c=0
found=False
#for i in range(0,n+1):
while not found:
    found = True
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
            found = False

    
print(a)