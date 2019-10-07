print('Hello')
a=input("Введите число 1: ")
a=int(a)
c=a%2

print (f'{c}')
if a == 0:
    print("Вы ввели ноль")
else:
    
    if c == 1:
        print ('Нечетное')
    elif c == 0:
        print ('Четное')
    else:
        print('Что-то пошло не так')

    