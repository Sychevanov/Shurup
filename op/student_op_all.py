import struct
#from myprogramm.student_write import write 
#from myprogramm.student_read import read
def menu1():
    print('')
    print('1. Список студентов')
    print('2. Добавить студента')
    print('3. Редаактировать студента')
    print('4. Удалить студента')
    print('5. Показать отличников')
    print('6. Показать неуспевающих')
    print('7. Выход')
def menu2():
    print('')
    print('1. Изменить фамилию')
    print('2. Изменить имя')
    print('3. Изменить отчество')
    print('4. Изменить группу')
    print('5. Добавить оценку ')
    print('6. Изменить оценку')
    print('7. Удалить оценку')
    print('8. Назад')
def menu3(a):
    print('---------------------')
    for i in range(len(a)):
        print(i+1, a[i]['Фамилия'], a[i]['Имя'], a[i]['Отчество'], a[i]['Группа'] )
    print('---------------------')
def menu4(spisok_student,i):
    
    print('')
    print(f"Фамилия: {spisok_student[i]['Фамилия']}")
    print(f"Имя: {spisok_student[i]['Имя']}")
    print(f"Отчество : {spisok_student[i]['Отчество']}")
    print(f"Группа: {spisok_student[i]['Группа']}")
    print('Оценки:')
    for key in spisok_student[i]['Оценки']:        
        print(f"   {key} - {spisok_student[i]['Оценки'][key]}")
def re_menu(y,spisok_student,i):
    if y == 1:
        spisok_student[i]['Фамилия'] = input('Введите новую фамилию: ')
        print('Фамилия измененна')
    if y == 2:
        spisok_student[i]['Имя'] = input('Введите новое имя: ')
        print('Имя измененно')    
    if y == 3:
        spisok_student[i]['Отчество'] = input('Введите новое отчество: ')
        print('Фамилия измененна')
    if y == 4:
        spisok_student[i]['Группа'] = input('Введите новую группу: ')
        print('Группа измененна') 
    if y == 5:
        predmet = [input('Введите предмет: ')] 
        spisok_student[i]['Оценки'][predmet] = int(input('Введите оценку: '))
        while not(spisok_student[i]['Оценки'][predmet] >= 2 and spisok_student[i]['Оценки'][predmet] <= 5):
            print('Введите корректно')
            spisok_student[i]['Оценки'][predmet] = int(input('Введите оценку: '))
    if y == 6:
        for key in spisok_student[i]['Оценки']:
            print(key, ' ', spisok_student[i]['Оценки'][key])
        predmet = input('Введите предмет, оценку у которого хотите изменить: ')
        spisok_student[i]['Оценки'][predmet] = int(input('Введите оценку: '))
        while not(spisok_student[i]['Оценки'][predmet] >= 2 and spisok_student[i]['Оценки'][predmet] <= 5):
            print('Введите корректно')
            spisok_student[i]['Оценки'][predmet] = int(input('Введите оценку: '))
        
    if y == 7:
        predmet = input('Введите предмет, который хотите удалить: ')
        del spisok_student[i]['Оценки'][predmet]      
def exit2():
    exit = input('Вы уверенны, что хотите выйти?: ')
    if exit == 'да' or exit == 'yes' or exit == 'y' :
        return True
    else:
        return False    
y = 0
found = False
exit = ''
#spisok_student = read()
x = 0
while True:
    if x == 7:        
        if exit2():
            break
    menu1()
    x = (input('Введите цифру: '))
    while not x.isdigit():
        x = (input('Введите цифру, а не букву: '))
    x = int(x)
    while not (x>0 and x<9  ):
        x = int(input('Введите цифру корректно: '))        
    if x == 1:
        for i in range(len(spisok_student)):
            menu4(spisok_student,i)
    if x == 2:
        sp = {}
        sp['Фамилия'] = input('Введите Фамилию студента: ')
        sp['Имя'] = input('Введите Имя студента: ')
        sp['Отчество'] = input('Введите Отчество студента: ')
        sp['Группа'] = input('Введите Группу студента: ')
        sp['Оценки'] = {}
        while True:            
            subject = input('Введите предмет, exit для выхода: ')
            if subject == 'exit':
                if exit2():
                    break
            assessments = int(input(f'Введите оценку по {subject}, exit для выхода: '))
            while not(assessments >= 2 and assessments <= 5):
                if assessments == 'exit':
                    if exit2():
                        break
                print('Введите корректно')    
                assessments = int(input(f'Введите оценку по {subject}, exit для выхода: '))    
            if assessments == 'exit':
                break
            sp['Оценки'][f'{subject}'] = assessments
        spisok_student.append(sp)
        write(spisok_student)    
    if x == 3:
        while True:
            menu3(spisok_student)
            exit = input('Напиишите номер студента, которого хотите редактировать, если хотите выйти напишите exit: ')       
            if exit == 'exit':
                exit = ''
                if exit2():
                    break            
            

            while y != 8 :                        
                menu2() 
                y = int(input('Введите цифру: '))
                re_menu(y,spisok_student,int(exit)-1) 
            y = 0                      

            write(spisok_student)        
    if x == 4:
        while True:
            menu3(spisok_student)
            
            exit = input('Напиишите номер студента, которого хотите удалить, если хотите выйти напишите exit: ')
            if exit == 'exit':
                if exit2():
                    break
            del spisok_student[int(exit)-1]
            print('Студент удален')
            write(spisok_student)
                    
    if x == 5:
        found = False
        for i in range(len(spisok_student)):
            asses5=True
            for key in spisok_student[i]['Оценки']:
                if spisok_student[i]['Оценки'][key] != 5:
                    asses5=False
            if asses5:
                menu4(spisok_student,i) 
                found = True 
        if not found:
            print('Отличников нет')                      
    if x == 6:
        found = False
        for i in range(len(spisok_student)):
            asses2=False
            for key in spisok_student[i]['Оценки']:
                if spisok_student[i]['Оценки'][key] == 2:
                    asses2=True
            if asses2:
                menu4(spisok_student,i) 
                found = True                 
        if not found:
            print('Неуспевающих нет')
            
