with open ('test2.txt','r') as y:
    s = y.readline()
    a = s.split(' ')
for i in range(len(a)-1):
    m=int(a[i])
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    tens = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    other = ['','thousand','million','billion']

    n = m
    s = ''
    s1 = ''
    p = 0
    boo = False

    if m < 0:
        m = -m
        boo = True
    while m != 0: 

        n = m%1000
        if n//100 != 0:
            s = s + ones[n//100] + ' hundred '
            n = n%100
        if n%100 <= 19 and n%100 >= 10:
            s = s + ' '+teens[(n%100)-10]
        elif n%100 < 10:
            s = s +  ones[n%10] 
        elif n%100 > 19 and n%100 < 100:
            s = s  + tens[n//10] + ' ' + ones[n%10] 
        m = m//1000
        if s: 
            s1 = s +  ' ' + other[p]  + ' ' + s1
        s = ""
        p = p + 1
    if s1[0]==' ':
        s1 = s1[1:]
    if boo:
        s1 = 'minus ' + s1
    i = 1
    while True:
        if s1[i]==' ' and s1[i+1]==' ':
            s1 = s1[0:i] + s1[i+1:len(s1)]
            break
        i = i + 1

        



    print(s1)
