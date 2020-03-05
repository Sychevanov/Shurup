import struct
def read():
    def read_val():
        binary_data = bytes_file.read(1)
        len_val, = struct.unpack("B",binary_data)
        binary_data = bytes_file.read(len_val)
        str_val, = struct.unpack(f'{len_val}s',binary_data)
        return str_val.decode("utf-8")
    vse = []
    ass_vse = {}
    with open ('all_op.','rb') as bytes_file:
        binary_data = bytes_file.read(2)
        k, = struct.unpack('H',binary_data)
        for i in range(k): 
            ass_vse['Фамилия'] = read_val()
            ass_vse['Имя'] = read_val()
            ass_vse['Отчество'] = read_val()
            ass_vse['Группа'] = read_val()
            ass_vse['Оценки'] = {}
            binary_data = bytes_file.read(2)
            n, = struct.unpack("H",binary_data)
            for i in range(n):
                binary_data = bytes_file.read(1)
                len_val, = struct.unpack("B",binary_data)
                binary_data = bytes_file.read(len_val+1)
                str_val = struct.unpack(f'{len_val}sB',binary_data)
                ass_vse['Оценки'][str_val[0].decode("utf-8")] = str_val[1]
            vse.append(ass_vse)  
            ass_vse = {}
    return vse 