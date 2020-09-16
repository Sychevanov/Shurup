
main_menu = Menu()
main_menu.add_submenu("Список студентов", Program.listStudentsCommand)


registry = StudentRegistry()
# используем registry
StudentRegistry().add_student(student)


class BriefPrintVisitor : StudentVisitor
{
  private bool _hasStudents = false;

  public void StartVisit()
  {0
    _hasStudents = false;
  }

  // ...
}



class BriefPrintVisitor(StudentVisitor):
  def start_visit(self):
    self.__has_students = False

  def visit_student(self, number, student):
    print(f"{number}. ", end="")
    student.print_short()
    self.__has_students = True

  def finish_visit(self):
    if not self.__has_students:
      print("Студентов в базе данных нет")

vis = BriefPrintVisitor()
StudentRegistry().visit_students(vis)


def visit_students(self, visitor):]
  visitor.start_visit()
  for i, student in enumerate(self.__students):
    visitor.visit_student(i, student)
  visitor.finish_visit()