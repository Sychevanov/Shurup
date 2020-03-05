import struct
a = {}

while True: 
    x=input('введите название команды: ')
    if x=='exit':
        break
    y=input('введите баллы: ')
    if y=='exit':
        break
    a[x]=int(y)
#for key in a:
    
#    print(f'Команда "{key}" - {a[key]} баллов')
#    print(len(key))


#n = int(input('Enter n: '))
with open ('bytesComand.','wb') as bytes_file:
    for key in a:
        key_by = key.encode("utf-8")
        len_key = len(key)
        binary_data = struct.pack (f'H{len_key}sB',len_key, key_by,a[key])
        bytes_file.write(binary_data)
        print(binary_data)
        #print(len(binary_data))
        
len_bt2 = len(binary_data) 
print(len_bt2)  
 
with open ('bytesComand.','rb') as bytes_file2:
    while True:
        binary_data2 = bytes_file2.read(2)
        if not binary_data2:
            break               
        len_key, = struct.unpack(f"H",binary_data2)
        binary_data2 = bytes_file2.read(len_key+1)
        num = struct.unpack(f'{len_key}sB',binary_data2)        
        print(f'team - {num[0].decode("utf-8")} points - {num[1]}')
        #print(binary_data2)