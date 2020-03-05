def calc(n):
    try:
        n = int(n)
    except:
        print('трай не смог и выполнился except')    
    else:
        print('трай смог и выполнилось елсе')
        return n/10


print(calc(100))

def calc2(n):
    try:
        n = int(n)
    except:
        print('jopa')
        n = 100      #если трай не смог то делается except и делается ретурн
    return n/10

#print(calc2('100l'))