n=int(input('VVedite chislo n: '))
u=0
o=int(n/2)
k=int((n ** 0.5))
for i in range(2,k+1): 
    c=n%i 
    print(c)
    if c==0:
        u=u+1       
    if u>=1:
        print('chislo sostavnoe')
        break
if u==0:
    print('chislo prostoe')
        


#a = [ 0 for i in range(10) ]
