n=int(input('Vedite n: '))
a = list(range(2, n+1))
#b  = [ 0 for i in range(10) ] 
print(a)
s=2
r=0

y=int(n**0.5)
for i in range (1,y):
    for i in range(2+r,n-1,s):
        if a[i]>0:
            a[i]=0
        
    print(a)
    s=s+1
    r=r+2
#for i in range(1,len(a)):
#    if a[i]>0:
#        v=v+1
    
#print(v)
# b = [ 0 for i in range(v) ]
# for i in range(1,n):
#     if a[u]>0:
#         b[j]=a[u]
#         j=j+1
#         print(b)
#     u=u+1
b = [ x for x in a if x != 0 ]
#b= [ x for x in a]
print(f' massiv {b}')





