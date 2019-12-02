import random
n=int(input('Enter n: '))
number=int(input('Number in massiv number: '))
a= [ random.randint(-5,10) for i in range(0,n)]
print(a)
found = False
for j,elem in enumerate(a):
    print(f'{j}. {elem}')
for k in range(len(a)):
    if a[k]==number:
        print(k)
        found = True
        break
if not found:
    print('No')
