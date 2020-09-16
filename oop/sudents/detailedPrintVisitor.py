from studentVisitor import StudentVisitor

class DetailedPrintVisitor(StudentVisitor):

    def startVisit(self): 
        
        self.__has_students = False

    
    def visitStudent(self, number, student): 

        print(f"{number}. ", end="")
        student.printLong()
        self.__has_students = True

    
    def finish_visit(self):

        if not self.__has_students:
            print("Студентов в базе данных нет")
            