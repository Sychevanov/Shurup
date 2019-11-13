s=input('Vvedite polindrom s: ')
i=1
p=1
while s[-i]==s[i-1]:
    if i==int(len(s)/2):
        print('polindrom')
        break
    i=i+1
else:
    print('ne polindrom')