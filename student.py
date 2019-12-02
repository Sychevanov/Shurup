import random
n = int(input('Enter n: '))
a = [random.randint(2,5) for i in range(0,n)]
print(a)
assesNorm=False
asses2=False
for i in range(0,len(a)):
    if a[i]==2:
        asses2=True
        break
    elif a[i]==3 or a[i]==4:
        assesNorm=True
    
if asses2:
    print('2')    
elif assesNorm :
    print('norm')
else:
    print('5')

#if assesNorm and not asses2:
#    print('norm')
#elif asses2:
#    print('2')
#else:
#    print('5')