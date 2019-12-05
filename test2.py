import random
#n = int(input('Enter n: '))
#a = [random.randint(0,10) for i in range(0,n)]
a = [2,7,5,3,1,6,9]
print(a)
c=0
minn=0
for j in range(1,len(a)):
    if a[0]>a[j]:
        minn=a[j]

    print(minn)
print(minn)
