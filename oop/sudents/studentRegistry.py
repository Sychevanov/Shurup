from student import Student
import json
#from program import Program

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
        person = []
        for i in range(0,StudentRegistry().getStudentsCount()):
            person.append(StudentRegistry().studetInDict(StudentRegistry().getStudent(i+1)))
            
        with open ('person.json','w') as f:
            json.dump(person, f)

    def load(self):
        with open ('person.json','r') as f:
            person2 = json.load(f)
            StudentRegistry().dictInStudent(person2)

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
            



