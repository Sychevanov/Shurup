class student():
    def __init__(self, first_name, middle_name, last_name, group, marks):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.group = group
        self.marks = marks


    def printLong(self): #доделаю
        print(f'Фамилия:{self.last_name}\n')
        print(f'Имя:{self.first_name}\n')
        print(f'Отчество:{self.middle_name}\n')
        print(f'Группа:{self.group}\n')
        print('Оценки:')
        for i in self.marks:
            print('   ',i,':',self.marks[i])

        
        
        

    def printShort(self):
        print(f'Фамилия:{self.last_name}\n')
        print(f'Имя:{self.first_name}\n')
        print(f'Отчество:{self.middle_name}\n')
        print(f'Группа:{self.group}\n')

    def printSubjects(self):#тоже
        print('Оценки:')
        for i in self.marks:
            print('   ',i,':',self.marks[i])
