import random
n = int(input('Enter n: '))
a = [random.randint(-5,10) for i in range(0,n)]
for i in range(1,len(a)):
    j=i
    while a[j]<a[j-1] and j!=0:
        a[j],a[j-1]=a[j-1],a[j]
        j=j-1
print(a)

number = int(input('Enter number: '))
x=n//2
left = 0
right = n
found = True
#for i in range(0,n//2): #вместо n логорифм основание 2 тело n
while len(a[left:right])>1:
    if a[x]==number:
        print(a[x])
        found = False
        break
    elif number < a[x]:
        right = x    
    elif number > a[x]: 
        left = x    
    x = (left+right)//2  
if found:
    print('No!')