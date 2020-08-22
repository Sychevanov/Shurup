n=int(input('Enter n poka ne nol: '))
a=[]
summ=0
i=0
while n!=0:
    a.append(n)
    summ=summ+a[i]
    i=i+1
    n=int(input('Enter n poka ne nol: '))   
print(f'Summ = {summ}')
j=0
while j!=len(a): 
    print(f'{j}. {a[j]}')
    j=j+1

