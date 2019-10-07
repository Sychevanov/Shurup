#import math
#from math import sqrt импорт библиотеки
#from othermath import sqrt as sq AS это для того чтобы переимновать название функции 

a=(input('Vvedite a: '))
b=(input('Vvedite b: '))
c=(input('Vvedite c: '))
a=float(a)
b=float(b)
c=float(c)
d=(b*b-4*a*c)

if  a==0:
    x=-c/b
    print(f'ne kvadratnoe uravnenie {x}')
    
elif d>0:
    x1=((-b)+(d ** 0.5))/(2*a)
    x2=((-b)-(d ** 0.5))/(2*a)
    
    print(f'x1={x1}, x2={x2}')
elif d==0:
    x1=(-b)/(2*a)
    print(f'x={x1}')
else:
    print('d<0')



