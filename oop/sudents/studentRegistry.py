from student import student

class Singleton(type):

    instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls.instances:

            cls.instances[cls] = super().__call__(*args, **kwargs)

            return cls.instances[cls]

class StudentRegistry(metaclass=Singleton):

    def __init__(self):

        self.__students = [] 

    def addStudents(self, student):
        self.__students.append(student)
        
    def removeStudentsNumber(self,number):
        del self.__students[number]
        
    def removeStudents(self,val):
        for i in range(len(self.__students)):
            if self.__students[i].first_name == val:
                del self.__students[i]
                break

    def getStudents(self,number):
        return self.__students[number-1]

    def getStudentsCount(self):
        return len(self.__students)



student = student('Ivan','Ivanov','Ivanovich','oop',{'russkiy': 5})
studentRegistry = StudentRegistry()
studentRegistry.addStudents(student)
st2 = StudentRegistry()
student.printShort()
print(studentRegistry)
#studentRegistry.removeStudents('Ivan')
