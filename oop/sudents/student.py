class Student():
    def __init__(self, last_name, first_name, middle_name, group, marks={}):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.group = group
        self.marks = marks


    def printLong(self): 
        print(f'Фамилия:{self.last_name}')
        print(f'Имя:{self.first_name}')
        print(f'Отчество:{self.middle_name}')
        print(f'Группа:{self.group}')
        print('Оценки:')
        for key, value in self.marks.items():
            print(f"  {key}: {value}")
        
    def printShort(self):
        print(f'Фамилия:{self.last_name}')
        print(f'Имя:{self.first_name}')
        print(f'Отчество:{self.middle_name}')
        print(f'Группа:{self.group}')

    def printSubjects(self):
        print('Оценки:')
        for key, value in self.marks.items():
            print(f"  {key}: {value}")
