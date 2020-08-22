
n=int(input('Vvedite n: '))

for i in range (1,n+1):
    
    print(i)
    
for i in range (1,n+1):
    
    
    print (f'{i} ', end="")

for i in range (1,n+1):
    
    if i<n:
        print (f'{i}, ', end="")
    else:print (n)
#print (n)

for i in range (1,n+1):    
    print ('*', end="")

    
for i in range (1,n+1):    
    print ('*')

for i in range (1,n+1):
    print (' ')
    for i in range (1,n+1):
        print ('* ', end='')

print (' ')

for i  in range (n,0,-1):
    print (i)
for i in range (2,n+1):
    print (i)
        
print (' ')
m=n+1
for j in range (1,n+1):
    print (' ')
    m=m-1
    for i in range (1,m+1):
        print ('* ', end='')
m=1
for i in range (1,n):
    print (' ')
    m=m+1
    for i in range (m,0,-1):
        print ('* ', end='')

print (" ")

         
