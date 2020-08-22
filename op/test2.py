import struct
s = ['Мертвого человека','Волков','Пещеру','Осмотреться','Идти с Вирджилом']
for i in range(5):
    s_encode = s[i].encode("utf-8")
    len_s_encode = len(name_encode)
    binary_data = struct.pack (f'B{len_s_encode}s',len_s_encode,s_encode)
    bytes_file.write(binary_data)