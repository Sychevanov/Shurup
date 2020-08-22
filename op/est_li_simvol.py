s=input('Vvedite stroku s: ')
ch=input('Vvedite simvol: ch: ')
i=0
while s[i]!=ch:
    if i+1==len(s):
        print ('net simvola') 
        break
    i=i+1
else:
    print (s[i], i)

#for i in range(0,len(s)):
#    if s[i]==ch:
#        print(s[i],i+1)
#        break
#    elif i==len(s)-1:
#        
#        print ('net simvola')
#        break