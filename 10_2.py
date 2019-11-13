import random
import math
#x = random.randint(1,100)
a = int(input('Vvedite ot 1-100 a: '))
# 6-7 попыток 
p=1
x=int(50)
#while a != x :
y=0
y=int(y)

for i in range(1,11):
    p=p+1
    
    if a < x:
        x=int(x-(x/2))

    elif a > x:
        
        x=int(((100-x)/2)+x)
   
    if p>=9:
        
        break
    print(x)
print(f'popitok {p} ')
print (x)