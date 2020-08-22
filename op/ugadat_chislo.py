left = 0
right = 100
print ('zagadaite chislo')

x=50
while True:
    a = input(f'vashe chislo bolshe, menshe ili ravno, - {x} napishite znaki > < = ')
    if a == '=':
        print(f'vashe chislo {x}')
        break
    elif a == '<':
        right = x
        x = (left + right)//2
    else: 
        left = x
        x = (left+right)//2
    print(x)

