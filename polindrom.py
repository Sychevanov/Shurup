s=input('Vvedite polindrom s: ')
p=1
print(int((len(s)/2)))
for i in range(1,int(len(s))):
    if s[-i]==s[i-1]:
        p=p+1
    if s[-i]!=s[i-1]:
        print('ne polindrom')
        break
    if p==int((len(s)/2)):
        print('polinrom')
        break
print(p)


#i=1
#while s[-i]==s[i-1]:
#    if i+1>int(len(s)/2):
#        print('ne polindrom')
#        break
#        
#    i=i+1
#if i+1<int(len(s)):
#    print('polindrom')