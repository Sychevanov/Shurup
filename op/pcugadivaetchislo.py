left = 0
right = 100
a = int(input('vvedite a: '))
x=100
while a != x:
    
    if a < x:
        right = x
        x = (left + right)//2
    else: 
        left = x
        x = (left+right)//2
    print(x)
print (f'Vashe chislo {x}')
