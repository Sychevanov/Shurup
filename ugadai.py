import random
x = random.randint(1,100)
a = int(input('Vvedite a: '))
# 6-7 попыток 
p=1
while a != x:
    if x < a:
        print (f'x < {a}')
    else:
        print (f'x > {a}')
    a = int(input('Vvedite a: '))
    p=p+1
print(f'popitok {p} ')

