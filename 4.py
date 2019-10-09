n=int(input('VVedite chislo n: '))
u=0
o=int(n/2)
for i in range(2,o+1): 
    c=n%i 
    print(c)
    if c==0:
        u=u+1       
    if u>=1:
        print('chislo sostavnoe')
        break
if u==0:
    print('chislo prostoe')
        
