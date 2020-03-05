import random
n = int(input('Enter n: '))
m = int(input('Enter m: '))
a = [[random.randint(0,10) for i in range(n)] for j in range(0,m)]
#a = [[9, 5, 9], [9, 9, 9], [1, 8, 3]]
b = [0 for i in range(m)]
maxx = sum(a[0])
number = 0
#n =3
print (a)
for i in range(n):
    print(f'{i+1} команда - {a[i]}, суммa баллов {sum(a[i])}')
for j in range(1,n):
    if maxx < sum(a[j]):
        maxx = sum(a[j])
   
 
for j in range(n):
    if maxx == sum(a[j]):
        print(f'1 mesto comand {j+1}') 