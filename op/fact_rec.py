
def rec(x,p):
    if p==1:
        print (x)
        return 
    p=p-1
    x = x * p
    
    return rec(x,p)
x = int(input('vvedite x:  '))
p=x
rec (x,p)