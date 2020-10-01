from studentVisitor import StudentVisitor



class LowArchieverVisitor():
    def __init__(self):

        self.__low_archievers = []

    def start_visit(self):

        self.__has_students = False

    def visit_student(self, number, student): #сколько разныъ обьектов столько и визитов дожно быть

        print(f"{number+1}. ", end="")
        #found = False
        #for mark in list(student.marks.values()):
        #    if mark == 2:
        #        found = True
        #        break
        #if found:
        #    student.printShort()
        if sum(list(student.marks.values()))/len(list(student.marks.values())) <= 3:
            student.printShort()
        self.__has_students = True

    def finish_visit(self):

        if not self.__has_students:
            print("Неуспевающих в базе данных нет")