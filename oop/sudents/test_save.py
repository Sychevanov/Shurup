import json
from student import Student
from studentRegistry import StudentRegistry 
person = [4,5,6]

with open ('person.json','w') as f:
    json.dump(person, f)

with open ('person.json','r') as f:
    person2 = json.load(f)

print(person2)