from studentRegistry import StudentRegistry
from student import Student
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
        #list(student.getStudent(i).marks.values())
        pass

    @staticmethod
    def showLowArchiversCommand():
        pass


#if __name__ == "__main__":
#    student = Student('Ivanov','Ivan','Ivanovich','oop',{'russkiy': 5,'math':4})
#    student2 = Student('Ivanov','Ivan','Ivanovich','oop',{'russkiy': 5,'math':4})
#    
#    studentRegistry = StudentRegistry()
#    studentRegistry.addStudents(student)
#    studentRegistry.addStudents(student2)
#    Program().addStudentCommand()
#    Program().listStudentsCommand()
