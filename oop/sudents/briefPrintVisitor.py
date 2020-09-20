from studentVisitor import StudentVisitor

class BriefPrintVisitor():
  
    def start_visit(self):

        self.__has_students = False

    def visit_student(self, number, student):

        print(f"{number}. ", end="")
        student.printShort()
        self.__has_students = True

    def finish_visit(self):

        if not self.__has_students:
            print("Студентов в базе данных нет")