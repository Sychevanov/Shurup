def fib(n):
    f1=1
    f2=1
    f=1
    for i in range(2,n):
        f = f1 + f2
        f1 = f2
        f2 = f
    #print(f' - {f}')
    return f

n = int(input('Vvedite n: '))
x = fib (n)

print(x)