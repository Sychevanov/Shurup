import random
n = int(input('Enter n: '))
a = [random.randint(2,5) for i in range(0,n)]
print(a)
asses2=False
asses5=True
for i in range(0,len(a)):
    if a[i]==2:
        asses2=True
        break
    elif a[i]!=5:
        asses5=False
        break

if asses2:
    print('2')    
elif asses5 :
    print('5')
else:
    print('norm')

