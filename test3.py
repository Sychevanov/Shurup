import struct
lname = 'Роман'
fname = 'Сычеванов'
patronymic = 'Андреевич'
group = 'А1'
math = 5
subject = ''
spisok_student = []
sp = {
                  'Фамилия': fname, 
                      'Имя': lname,
                 'Отчество': patronymic,
                   'Группа': group,
                   'Оценки': {'Математика': math, 'Русский': 5},
                 }
spisok_student.append(sp)
sp = {}
def write(spisok_student):
    j = 0
    with open ('all_op.','wb') as bytes_file:
        for i in range(len(spisok_student)):
            znak3 = 'll' 
            flag3 = znak3.encode("utf-8")
            binary_data = struct.pack ('2s',flag3)
            bytes_file.write(binary_data)
            for key in spisok_student[i].values():
                j = j + 1             
                if j == 5:
                    for key,val in spisok_student[i]['Оценки'].items():
                        key_by = key.encode("utf-8")
                        len_key = len(key_by)
                        binary_data = struct.pack (f'H{len_key}sB',len_key,key_by,val)
                        bytes_file.write(binary_data)
                else:      
                    key_by = key.encode("utf-8")
                    len_key = len(key_by)
                    binary_data = struct.pack (f'H{len_key}s',len_key,key_by)
                    bytes_file.write(binary_data)
                if j ==5:
                    break     
            j = 0
            znak = 'kk'        
            flag = znak.encode("utf-8")
            binary_data = struct.pack ('2s',flag)
            bytes_file.write(binary_data)  
        znak2 = 'lj' 
        flag2 = znak2.encode("utf-8")
        binary_data = struct.pack ('2s',flag2)
        bytes_file.write(binary_data)
write(spisok_student)

        