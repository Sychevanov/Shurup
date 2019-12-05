import random
n = int(input('Enter n: '))
a = [random.randint(0,10) for i in range(0,n)]
#a = [2,7,5,3,1,6,9]
print(a)

for i in range(1,len(a)):
    j=i
    while a[j]<a[j-1] and j!=0:
        a[j],a[j-1]=a[j-1],a[j]
        j=j-1
print(a)
