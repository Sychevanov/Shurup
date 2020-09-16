from studentVisitor import StudentVisitor
from program import Program


class LowArchieverVisitor(StudentVisitor):
    def __init__(self):

        self.__low_archievers = []

    def start_visit(self):

        self.__has_students = False

    def visit_student(self, number, student):

        print(f"{number}. ", end="")
        #found = False
        #for mark in list(student.marks.values()):
        #    if mark == 2:
        #        found = True
        #if found:
        #    student.printShort()
        if sum(list(student.marks.values()))/len(list(student.marks.values())) <= 3:
            student.printShort()
        self.__has_students = True

    def finish_visit(self):

        if not self.__has_students:
            print("Студентов в базе данных нет")