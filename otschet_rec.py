def rec(x,n):
    
    print(x, end = ' ')
    if x == n:
        print(' ')
        print('otschet okonchen')
        return 0
    x = x + 1
    return rec(x,n)
x = int(input('vvedite s kakogo nachat otschet: '))
n = int(input('vvedite do kakogo schitat '))
rec (x,n)