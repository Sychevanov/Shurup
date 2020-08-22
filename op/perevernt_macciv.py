n=3
def massiv (n):
    print(f'vvedite {n} chisla' )
    b  = [ 0 for i in range(n) ] 
    i=0
    while i<n:
        b[i]=int(input(f'chislo {i+1}: '))
        i=i+1
    return b



def rev_number(b,i):
    if i<0:
        return 
    print (b[i])
    i=i-1
    return rev_number(b,i)

#rev_number(massiv(n),n-1)

#p=b[2]
def rev_number2(b,i,p):
    
    if i<0:
        b[i+1]=p
        return b
    b[i]=b[2-i]
    i=i-1
    
    return rev_number2(b,i,p)

#print(rev_number2(b,2,p))

def number_plus1(b,i):
    if i>n-1:
        return
    b[i]=b[i]+1
    if b[i]==10:
        b[i]=0
    print(b[i])
    i=i+1
    return number_plus1(b,i)
#number_plus1(massiv(n),0)

def number_plus2(b,i):
    if i>n-1:
        return b
    b[i]=b[i]+1
    if b[i]==10:
        b[i]=0
    i=i+1
    return number_plus2(b,i)

print(number_plus2(massiv(n),0))
    
