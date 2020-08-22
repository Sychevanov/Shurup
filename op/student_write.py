import struct
def write(spisok_student):
    def write_val(val):
        val_by = val.encode("utf-8")
        len_val = len(val_by) 
        binary_data = struct.pack (f'B{len_val}s',len_val,val_by)
        bytes_file.write(binary_data)
    k = len(spisok_student)
    with open ('all_op.','wb') as bytes_file:
        binary_data = struct.pack ('H',k)
        bytes_file.write(binary_data)
        for i in range(k):                        
            val = spisok_student[i]['Фамилия']    
            write_val(val)
            val = spisok_student[i]['Имя']    
            write_val(val)
            val = spisok_student[i]['Отчество']    
            write_val(val)
            val = spisok_student[i]['Группа']    
            write_val(val) 
            n = len(spisok_student[i]['Оценки'])
            binary_data = struct.pack ('H',n)
            bytes_file.write(binary_data)
            for key,val in spisok_student[i]['Оценки'].items():
                key_by = key.encode("utf-8")
                len_key = len(key_by)
                binary_data = struct.pack (f'B{len_key}sB',len_key,key_by,val)
                bytes_file.write(binary_data)