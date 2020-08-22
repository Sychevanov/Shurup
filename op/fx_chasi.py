def chasi(n,s):
    m=n
    t=s
    p=int(n/2)
    
    for j in range(0,p):

        for i in range (0,t):
            print(end='  ')
        for i in range (0,m):  
            print('*', end=' ')
        t=t+1
        m=m-2
        print (' ')
        

    for j in range (0,p+1):  
        for i in range(0,t):
            print(end='  ')
        t=t-1
        for i in range(0,m):
            print('*', end=' ')
        m=m+2
        print(' ')
        
    return 0        
n=int(input('Vvedite ne chetnoe n: ')) 
i=n
s=0
while n>=3:
    
    chasi(n,s)
    
    n=n-2
    s=s+1
    
while n<=i:
    chasi(n,s)
    
    n=n+2
    s=s-1


