n=int(input('VVedite chislo: '))
def rev_number (n):
    if n==0:
        return
    print(n%10)
    n=n//10
    return rev_number(n)

#rev_number(n)
p=0
def rev_number2 (n,p):
    if n==0:
        return p
    p=(p*10)+n%10
    n=n//10
    
    return rev_number2(n,p)
#print (rev_number2(n,p))

p=0
u=2
def number_1(n,p,u):
    if u==-1:
        return p
    
    p=p*10 + ((n//10**u)+1)%10
    u=u-1
    print(p)
    return number_1(n,p,u)
#print (number_1(n,p,u))


def number_2(n,p):
    if n==0:
        return rev_number2(p,0)
    p=(p*10)+(n+1)%10
    n=n//10
    
    return number_2(n,p)

print (number_2(n,p))