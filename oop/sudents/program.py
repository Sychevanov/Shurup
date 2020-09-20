from studentRegistry import StudentRegistry
from student import Student
from lowAchieverVisitor import LowArchieverVisitor
from hightAchieverVisitor import HightArchieverVisitor
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


if __name__ == "__main__":
    student = Student('Ivanov','Ivan','Ivanovich','oop',{'russkiy': 2,'math':2})
    student2 = Student('Ivanov','Ivan','Ivanovich','oop',{'russkiy': 2,'math':2})
    studentRegistry = StudentRegistry()
    studentRegistry.addStudents(student)
    studentRegistry.addStudents(student2)
    #Program.addStudentCommand()
    #Program.listStudentsCommand()
    #Program.showHighAchiversCommand()
    Program.showLowArchiversCommand()



