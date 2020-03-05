import random
n = int(input('Enter n: '))
m = int(input('Enter m: '))
a = [[random.randint(0,10) for i in range(n)] for j in range(0,m)]
#a = [[9, 5, 9], [9, 5, 9], [1, 8, 3]]
b = [0 for i in range(m)]
maxx = sum(a[0])
number = 0
#n =3
found=False
print (a)
for i in range(n):
    print(f'{i+1} команда - {a[i]}, суммa баллов {sum(a[i])}')
       
for k in range(n):                           
    b[k]=[k+1,sum(a[k])]
    
while not found:
    found = True    
    for i in range(len(a)-1):
            if b[i][1]<b[i+1][1]:    
                b[i],b[i+1]=b[i+1],b[i]
                found = False
print(b)
for o in range(n):
    print(f'{o+1} mesto comanda {b[o][0]}')