n=int(input('Vvedite n: '))
m=n
t=0
p=int(n/2)
for i in range(0,p):
    for i in range (0,m):  
        print('*', end=' ')
    t=t+1
    m=m-2
    print (' ')
    for i in range (0,t):
        print(end='  ')
for i in range (0,p+1):   
    for i in range(0,m):
        print('*', end=' ')
    m=m+2
    print(' ')
    for i in range(1,t):
        print(end='  ')
    t=t-1
    
            




