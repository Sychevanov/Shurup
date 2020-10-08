from student import Student
import json

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
        del self.__students[number-1]

        
    def removeStudents(self,student):

        self.__students.remove(student)

    def getStudent(self,number):
        return self.__students[number-1]

    def getStudentsCount(self):
        return len(self.__students)

    def visit_students(self, visitor):

        visitor.start_visit()

        for i, student in enumerate(self.__students):
            visitor.visit_student(i, student)
        
        visitor.finish_visit()

    def save(self):
        with open ('students.json','w') as f:
            json.dump(self.__students, f)

    def load(self):
        with open ('students.json','r') as f:
            self.__students = json.load(f)



