from studentRegistry import StudentRegistry
from student import Student
from lowAchieverVisitor import LowArchieverVisitor
from hightAchieverVisitor import HightArchieverVisitor
from briefPrintVisitor import BriefPrintVisitor
from editContext import EditContext
class Program():

    @staticmethod
    def listStudentsCommand():
        StudentRegistry().visit_students(BriefPrintVisitor())
        

    @staticmethod
    def addStudentCommand():
        last_name = input('Введите Фамилию: ')
        first_name = input('Введите Имя: ')
        middle_name = input('Введите Отчество: ')
        group = input('Введите группу: ')
        StudentRegistry().addStudents(Student(last_name,first_name,middle_name,group))

    @staticmethod
    def removeStudentCommand():
        StudentRegistry().visit_students(BriefPrintVisitor()) #подтверждение 
        if StudentRegistry().getStudentsCount() != 0:

            n = int(input('Введите номер ученика'))
            StudentRegistry().removeStudentsNumber(n) 

    
    @staticmethod
    def showHighAchiversCommand():
        vis = HightArchieverVisitor()
        StudentRegistry().visit_students(vis)
        
        
        

    @staticmethod
    def showLowArchiversCommand():
        vis = LowArchieverVisitor()
        StudentRegistry().visit_students(vis)
        

    @staticmethod
    def SelectStudentCommand():

        lenStudents = StudentRegistry().getStudentsCount()
        for i in range(0,lenStudents):
            print(i+1,end='. ')
            StudentRegistry().getStudent(i).printShort() 
            print('\n')
        x = int(input('Введите номер студента: '))
        EditContext().student = StudentRegistry().getStudent(x-1)

    @staticmethod
    def ShowSelectedCommand():

        EditContext().student.printShort()

    @staticmethod
    def DeselectStudentCommand():

        EditContext().student = None
    
    @staticmethod
    def EditFirstNameCommand():
        EditContext().student.first_name = input('Введите Имя: ')

    @staticmethod
    def EditMidlleNameCommand():
        EditContext().student.middle_name = input('Введите Отчество: ')
    
    @staticmethod
    def EditLastNameCommand():
        EditContext().student.last_name = input('Введите Фамиллию: ')
    
    @staticmethod
    def EditGroupNameCommand():
        EditContext().student.group = input('Введите Группу: ')

    @staticmethod
    def EditMarksCommand():
        for key, value in EditContext().student.marks.items():            
            print(f"{key}: {value}")
        x = input('Введите предмет, чтобы изменить оценку: ')
        EditContext().student.marks[x] = int(input('Введите оценку: ')) #проверку сделать если ли предмет

    @staticmethod
    def AddMarksCommand():
        subject = input('Введите наименование предмета: ')
        mark = int(input('Введите оценку'))

        EditContext().student.marks[subject] = mark  
        print('оценка добавлена') 
    
    @staticmethod
    def DeleteMarksCommand():
        for key, value in EditContext().student.marks.items():            
            print(f"{key}: {value}")
        x = input('Введите предмет, чтобы удалить оценку: ')
        yORn = input(f'Вы уверены что хотите удалить оценку {x}?')
        #проверка на коррекность ввода предмета
        if yORn == 'yes' or 'да':

            EditContext().student.marks[x] = ''
            print('Вы удалил оценку')

    @staticmethod
    def studetInDict(student):
        studentDict = []
        studentDict.append(student.last_name)
        studentDict.append(student.first_name)
        studentDict.append(student.middle_name)
        studentDict.append(student.group)
        studentDict.append(student.marks)   
        return studentDict
    @staticmethod
    def dictInStudent(studentsInDict):
        for i in range(0,len(studentsInDict)):
            student = Student(studentsInDict[i][0],studentsInDict[i][1],studentsInDict[i][2],studentsInDict[i][3],studentsInDict[i][4])
            StudentRegistry().addStudents(student)

    
            
    








