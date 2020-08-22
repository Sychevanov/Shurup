n = int(input(' Vvedite chislo n: '))
f1=1
f2=1
i=0
f=1

for i in range(2,n):
    
    f = f1 + f2
    f1 = f2
    f2 = f
    
    print (f)
print(f' - {f}')