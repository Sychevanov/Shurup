number = int(input('enter: '))
str_1=''
while number != 0:
    result = number%2
    number = number//2
    str_1 = str_1+str(result)
    
#print(str_1[::-1])


def dvoich(number,str_1):
    if number==0:
        return str_1[::-1]
    str_1=str_1+str(number%2)
    return dvoich(number//2,str_1)

print (dvoich(number,str_1))