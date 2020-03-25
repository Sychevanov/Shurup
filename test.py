import struct
def save(name,char,snaryajenie,bag):
    def write_val(key_str):
        if snaryajenie[key_str] != {}:   
            binary_data = struct.pack ('B',1)
            bytes_file.write(binary_data)      
            #не знал, как записывать если словарь пустой, можно было не делать пустых словарей, но так не хочу
            key = list(snaryajenie[key_str].items())[0][0]
            val_0 = int(list(snaryajenie[key_str].items())[0][1][0])
            val_1 = int(list(snaryajenie[key_str].items())[0][1][1])
            key_encode = key.encode("utf-8")
            len_key_encode = len(key_encode)
            binary_data = struct.pack (f'B{len_key_encode}sBB',len_key_encode,key_encode,val_0,val_1)
            bytes_file.write(binary_data)
        else:
            binary_data = struct.pack ('B',0)
            bytes_file.write(binary_data)            
    k = len(bag)
    with open ('arcanum_save.','wb') as bytes_file:
        name_encode = name.encode("utf-8")
        len_name_encode = len(name_encode)
        binary_data = struct.pack (f'B{len_name_encode}s',len_name_encode,name_encode)
        bytes_file.write(binary_data)

        val_healt = char['Здоровье']
        val_strange = char['Сила']
        val_agil = char['Ловкость']
        val_charm = char['Обаяние']
        val_tekh = char['Технологии']
        val_magic = char['Магия']
        binary_data = struct.pack ('BBBBBB',val_healt,val_strange,val_agil,val_charm,val_tekh,val_magic)
        bytes_file.write(binary_data)

        write_val('Голова')
        write_val('Куртка')
        write_val('Руки')
        write_val('Кольцо1')
        write_val('Кольцо2')
        write_val('Ожерелье')
        
        binary_data = struct.pack ('B',k)
        bytes_file.write(binary_data)
        for i in range(k):
            key = list(bag[i].items())[0][0]
            if len(list(bag[i].values())[0]) == 1:
                val_0 = int(list(bag[i].items())[0][1][0])
                val_1 = 0
                val_2 = 0
            if len(list(bag[i].values())[0]) == 2:
                val_0 = int(list(bag[i].items())[0][1][0])
                val_1 = int(list(bag[i].items())[0][1][1])
                val_2 = 0
            if len(list(bag[i].values())[0]) == 3:
                val_0 = int(list(bag[i].items())[0][1][0])
                val_1 = int(list(bag[i].items())[0][1][1])
                val_2 = int(list(bag[i].items())[0][1][2])
            key_encode = key.encode("utf-8")
            len_key_encode = len(key_encode)
            binary_data = struct.pack (f'B{len_key_encode}sBBB',len_key_encode,key_encode,val_0,val_1,val_2)
            bytes_file.write(binary_data)
def load():
    def read_val():
        binary_data = bytes_file.read(1)
        chek, = struct.unpack('B',binary_data)
        if chek:
            binary_data = bytes_file.read(1)
            len_key_encode, = struct.unpack('B',binary_data)
            binary_data = bytes_file.read(len_key_encode+2)
            dict_ = struct.unpack(f'{len_key_encode}sBB',binary_data)
            item = {dict_[0].decode("utf-8"): [dict_[1],dict_[2]]}
        else:
            item = {}
        return item 
    snaryajenie = {}
    char = {}
    bag = []
    with open ('arcanum_save.','rb') as bytes_file:
        binary_data = bytes_file.read(1)
        len_name_encode, = struct.unpack('B',binary_data)
        binary_data = bytes_file.read(len_name_encode)
        name_encode, = struct.unpack(f'{len_name_encode}s',binary_data)
        name  = name_encode.decode("utf-8")

        binary_data = bytes_file.read(6)
        val = struct.unpack("BBBBBB",binary_data)
        char['Здоровье'] = val[0]
        char['Сила'] = val[1]
        char['Ловкость']= val[2]
        char['Обаяние']= val[3]
        char['Технологии']= val[4]
        char['Магия']= val[5]

        snaryajenie['Голова'] = read_val()
        snaryajenie['Куртка'] = read_val()
        snaryajenie['Руки'] = read_val()
        snaryajenie['Кольцо1'] = read_val()
        snaryajenie['Кольцо2'] = read_val()
        snaryajenie['Ожерелье'] = read_val()

        binary_data = bytes_file.read(1)
        k, = struct.unpack('B',binary_data)
        for i in range(k):
            binary_data = bytes_file.read(1)
            len_key_encode, = struct.unpack('B',binary_data)
            binary_data = bytes_file.read(len_key_encode+3)
            dict_ = struct.unpack(f'{len_key_encode}sBBB',binary_data)
            if dict_[2] and dict_[3] != 0:
                item = {dict_[0].decode("utf-8"): [dict_[1],dict_[2],dict_[3]]}
                bag.append(item) 
            elif dict_[2] !=0 and dict_[3] == 0:
                item = {dict_[0].decode("utf-8"): [dict_[1],dict_[2]]}
                bag.append(item)
            else:
                item = {dict_[0].decode("utf-8"): [dict_[1]]}
                bag.append(item) 
        return name,char,snaryajenie,bag

    