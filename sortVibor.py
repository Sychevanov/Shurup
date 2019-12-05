import random
#n = int(input('Enter n: '))
#a = [random.randint(0,10) for i in range(0,n)]
a = [2,7,5,3,1,6,9]
print(a)
minn=0
for i in range(len(a)):
    m=i 
    for j in range(i,len(a)):
        if a[m]>a[j]:
            m=j       
    print(a)
    #minn=a[i]
    #a[i]=a[m]
    #a[m]=minn
    a[i],a[m]=a[m],a[i]
    
            
            
print(a)
