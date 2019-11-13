n=5
for i in range(n):
    for j in range(n):
        if j==n-i-1 or i==j:
            print("* ", end = '')
        else:
            print("• ", end ='')
    print(' ')

print(' ')

for i in range(n):
    for j in range(n):
        if j<=(n-1)-i and i>=j:
            print("* ", end = '')
        else:
            print("• ", end ='')
    print(' ')

print(' ')

for i in range(n):
    for j in range(n):
        if j>=(n-1)-i and i>=j:
            print("* ", end = '')
        else:
            print("• ", end ='')
    print(' ')

print(' ')

for i in range(n):
    for j in range(n):
        if j>=(n-1)-i and i<=j  :
            print("* ", end = '')
        else:
            print("• ", end ='')
    print(' ')

print(' ')

for i in range(n):
    for j in range(n):
        if  j<=(n-1)-i and j<=i or j>=(n-1)-i and j>=i:
            print("* ", end = '')
        else:
            print("• ", end ='')
    print(' ')

print(' ')

for i in range(n):
    for j in range(n):
        if  j<=(n-1)-i and j>=i or j>=(n-1)-i and j<=i:
            print("* ", end = '')
        else:
            print("• ", end ='')
    print(' ')