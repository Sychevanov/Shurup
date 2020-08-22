n = int(input('Enter n: '))
s = ""
i = 1
k = 1
def treg(s,i,n,k):
    if len(s) == 2 * n:
        return s[1::]
    s = s + ' ' + str(i)
    if k == i:
        k = 0
        i = i + 1
    return treg(s,i,n,k+1)

print(treg(s,i,n,k))

print((n*(n+1))/2)




        
        
        
   






