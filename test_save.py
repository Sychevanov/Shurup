import struct
import datetime

now = datetime.datetime.now()
time = str(now.strftime("%d-%m-%Y %H;%M"))
name = input('ввеите имя: ')
save = 'arcanum_fx/saves/' + name + ' ' + time + '.'
def saves(name):
    with open(save, 'wb') as bf:
        name_encode = name.encode("utf-8")
        len_name_encode = len(name_encode)
        binary_data = struct.pack (f'B{len_name_encode}s',len_name_encode,name_encode)
        bf.write(binary_data)
    with open ('arcanum_fx/saves/saves_info.txt','a') as y:
        y.write(name + ' ' + time +'\n')
saves(name)
saves = []
with open ('arcanum_fx/saves/saves_info.txt','r') as y:
    while True:
        s = y.readline()
        if not s:
            break
        s = s.split('\n')
        saves.append(s[0])
for i in range(0,len(saves)):
    print(i+1,saves[i])
x = int(input('Выберете сохранеие: '))
save_load = 'arcanum_fx/saves/' + saves[x-1]
with open(save_load, 'rb') as bytes_file:
    binary_data = bytes_file.read(1)
    len_name_encode, = struct.unpack('B',binary_data)
    binary_data = bytes_file.read(len_name_encode)
    name_encode, = struct.unpack(f'{len_name_encode}s',binary_data)
    name2  = name_encode.decode("utf-8")

print( name2)
