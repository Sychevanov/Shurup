d = {}
b = []
lname=''
fname=''
age= 0
d = {'Фамилия': fname, 'Имя': lname, 'Возраст':age}

while True:
    fname = input('ВВедите фамилию: ')
    if fname == 'exit':
        break
    d['Фамилия']=fname
    lname = input('ВВедите имя: ')
    if lname == 'exit':
        break
    d['Имя']=lname
    age = input('ВВедите возраст: ')
    if age == 'exit':
        break
    d['Возраст']=int(age)
    b.append(d)
    d={}
print(b)
n = int(input('Введите критерий возраста: '))
for i in range(len(b)):
    if b[i]['Возраст']<=n:
        print(f"Фамилия: {b[i]['Фамилия']}\nИмя: {b[i]['Имя']}\nВозраст: {b[i]['Возраст']}")




