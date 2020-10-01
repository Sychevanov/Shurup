from studentRegistry import StudentRegistry
from student import Student
from lowAchieverVisitor import LowArchieverVisitor
from hightAchieverVisitor import HightArchieverVisitor
from editContext import EditContext
class Program():

    @staticmethod
    def listStudentsCommand():
        lenStudents = studentRegistry.getStudentsCount()
        for i in range(0,lenStudents):
            print(i+1,end='. ')
            studentRegistry.getStudent(i).printShort() 
            print('\n')

    @staticmethod
    def addStudentCommand():
        last_name = input('Введите Фамилию: ')
        first_name = input('Введите Имя: ')
        middle_name = input('Введите Отчество: ')
        group = input('Введите группу: ')
        studentRegistry.addStudents(Student(last_name,first_name,middle_name,group))

    @staticmethod
    def removeStudentCommand():
        n = input('Введите номер ученика')
        studentRegistry.removeStudentsNumber(n)
    
    @staticmethod
    def showHighAchiversCommand():
        vis = HightArchieverVisitor()
        studentRegistry.visit_students(vis)
        
        

    @staticmethod
    def showLowArchiversCommand():
        vis = LowArchieverVisitor()
        studentRegistry.visit_students(vis)

    @staticmethod
    def SelectStudentCommand():

        lenStudents = studentRegistry.getStudentsCount()
        for i in range(0,lenStudents):
            print(i+1,end='. ')
            studentRegistry.getStudent(i).printShort() 
            print('\n')
        x = int(input('Введите номер студента: '))
        editContext.student = studentRegistry.getStudent(x-1)

    @staticmethod
    def ShowSelectedCommand():

        editContext.student.printShort

    @staticmethod
    def DeselectStudentCommand():

        editContext.student = None
    
    @staticmethod
    def EditFirstNameCommand():
        editContext.student.first_name = input('Введите Имя: ')

    @staticmethod
    def EditMidlleNameCommand():
        editContext.student.middle_name = input('Введите Отчество: ')
    
    @staticmethod
    def EditLastNameCommand():
        editContext.student.last_name = input('Введите Фамиллию: ')
    
    @staticmethod
    def EditGroupNameCommand():
        editContext.student.group = input('Введите Группу: ')

    @staticmethod
    def EditMarksCommand():
        for key, value in editContext.student.marks.items():            
            print(f"{key}: {value}")
        x = input('Введите предмет, чтобы изменить оценку: ')
        editContext.student.marks[x] = int(input('Введите оценку: '))


if __name__ == "__main__":
    student = Student('Ivanov','Ivan','Ivanovich','oop',{'russkiy': 2,'math':2})
    student2 = Student('Ivanov','Ivan','Ivanovich','oop',{'russkiy': 2,'math':2})
    studentRegistry = StudentRegistry()
    studentRegistry.addStudents(student)
    studentRegistry.addStudents(student2)
    #Program.addStudentCommand()
    #Program.listStudentsCommand()
    #Program.showHighAchiversCommand()
    #Program.showLowArchiversCommand()
    Program.listStudentsCommand()
    editContext = EditContext()
    editContext.student = studentRegistry.getStudent(0)
    #EditContext().student.printShort()
    Program.EditMarksCommand()
    Program.listStudentsCommand()
    editContext.student.printLong()





