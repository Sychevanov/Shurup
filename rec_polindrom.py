
def polindrom (s):
    if len(s)<=1:
        print ('Yes!')
        return
    if s[0]==' ':
        s=s[1:len(s)]
        return polindrom (s)  
    if s[-1]==' ':
        s=s[0:-1]
        return polindrom (s) 
    if s[0]!=s[-1]:
        print ('No!')
        return 
    s=s[1:-1]
    return polindrom(s)

s = input('Enter string: ')
polindrom(s)