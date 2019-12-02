s=input('Vvedite polindrom s: ')
p=0
j=len(s)
i=0
found=False
#а муза рада музе без ума да разума
while j>i:
    j=j-1
    i=i+1
    while s[i-1]==' ':
        i=i+1
    while s[j]==' ':
        j=j-1
    
    if s[j]!=s[i-1]:
        print('ne polindrom')
        found=True
        break
if not found:
    print('polindrom')
    
    



