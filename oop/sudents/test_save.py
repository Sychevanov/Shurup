import json
from student import Student
from program import Program
from studentRegistry import StudentRegistry 
#Program.addStudentCommand()
#Program.addStudentCommand()
StudentRegistry().load()
print(StudentRegistry().getStudent(0))
print(StudentRegistry().getStudent(1))

#StudentRegistry().save()
