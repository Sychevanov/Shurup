from studentVisitor import StudentVisitor
from program import Program


class HightArchieverVisitor(StudentVisitor):
    def __init__(self):

        self.__hight_archievers = []

    def start_visit(self):

        self.__has_students = False

    def visit_student(self, number, student):

        print(f"{number}. ", end="")
        if sum(list(student.marks.values()))/len(list(student.marks.values())) == 5:
            student.printShort() 
        self.__has_students = True

    def finish_visit(self):

        if not self.__has_students:
            print("Студентов в базе данных нет")