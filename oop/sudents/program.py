from studentRegistry import StudentRegistry
from student import Student
from lowAchieverVisitor import LowArchieverVisitor
from hightAchieverVisitor import HightArchieverVisitor
from editContext import EditContext
class Program():

    @staticmethod
    def listStudentsCommand():
        lenStudents = StudentRegistry().getStudentsCount()
        for i in range(0,lenStudents):
            print(i+1,end='. ')
            StudentRegistry().getStudent(i).printShort() 
            print('\n')

    @staticmethod
    def addStudentCommand():
        last_name = input('Введите Фамилию: ')
        first_name = input('Введите Имя: ')
        middle_name = input('Введите Отчество: ')
        group = input('Введите группу: ')
        StudentRegistry().addStudents(Student(last_name,first_name,middle_name,group))

    @staticmethod
    def removeStudentCommand():
        n = input('Введите номер ученика')
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

        EditContext().student.printShort

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
        EditContext().student.marks[x] = int(input('Введите оценку: '))







