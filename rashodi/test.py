import json
def save(student):
    with​ open('student.json', 'w') ​ as​ f: 
        json.dump(student, f)

def load():
    with​ open('student.json', 'r') ​ as​ f: 
        json.load(student, f)

with open ('all_op.','wb') as bytes_file:
        binary_data = struct.pack ('H',k)
        bytes_file.write(binary_data)


student = [45,45,18]

save(student)