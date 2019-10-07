n=5
m=n
y=5
t=0
q=1
g=0
o=0
p=0

p=(n/2)
p=int(p)
for i in range(0,n):
    if g<=(p-1):
        for i in range (0,m):  
            print('*', end=' ')
        t=t+1
        m=m-2
        g=g+1
        print (' ')
        for i in range (0,t):
            print(end='  ')
for i in range (0,n):
    if o<=p:
        for i in range(0,q):
            print('*', end=' ')
        q=q+2
        print(' ')
        for i in range(1,t):
            print(end='  ')
        t=t-1
        o=o+1
            




