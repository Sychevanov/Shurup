from studentVisitor import StudentVisitor



class HightArchieverVisitor():
    def __init__(self):

        self.__hight_archievers = []

    def start_visit(self):

        self.__has_students = False

    def visit_student(self, number, student):

        print(f"{number+1}. ", end="")
        if sum(list(student.marks.values()))/len(list(student.marks.values())) == 5:
            student.printShort() 
        self.__has_students = True

    def finish_visit(self):

        if not self.__has_students:
            print("Отличников в базе данных нет")