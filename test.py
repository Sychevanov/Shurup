import struct
bag = []
bag.append({'1-Старый меч':[1,5]})
bag.append({'2-Старый меч2':[1,4]})
bag.append({'3-Старый меч34':[1,4]})
bag.append({'4-Старый меч':[1]})
bag.append({'5-Старый меч':[5,4,6]})

#binary_data = struct.pack ('B',1)
#bytes_file.write(binary_data)      
#не знал, как записывать если словарь пустой, можно было не делать пустых словарей, но так не хочу
#key = list(snaryajenie[key_str].items())[0][0]
#val_0 = int(list(snaryajenie[key_str].items())[0][1][0])
#val_1 = int(list(snaryajenie[key_str].items())[0][1][1])
#key_encode = key.encode("utf-8")
#len_key_encode = len(key_encode)
#binary_data = struct.pack (f'B{len_key_encode}sBB',len_key_encode,key_encode,val_0,val_1)
#bytes_file.write(binary_data)
#binary_data = struct.pack ('B',0)
#bytes_file.write(binary_data)   
print(int(list(bag[3].values())[0][0]))
def sortirovka(bag):
  found=False
  while not found:
      found = True
      for i in range(len(bag)-1):
          if len(list(bag[i].values())[0])>len(list(bag[i+1].values())[0]):
            bag[i],bag[i+1] = bag[i+1],bag[i]
            found = False
#sortirovka(bag)
#print(bag)
def save(bag):
   k = len(bag)
   
   with open ('arcanum_save_test.','wb') as bytes_file:
      binary_data = struct.pack ('B',k)
      bytes_file.write(binary_data)
      for i in range(k):
         key = list(bag[i].items())[0][0]
         if len(list(bag[i].values())[0]) == 1:
            val_0 = int(list(bag[i].values())[0][0])
            val_1 = 0
            val_2 = 0
         if len(list(bag[i].values())[0]) == 2:
            val_0 = int(list(bag[i].values())[0][0])
            val_1 = int(list(bag[i].values())[0][1])
            val_2 = 0
         if len(list(bag[i].values())[0]) == 3:
            val_0 = int(list(bag[i].values())[0][0])
            val_1 = int(list(bag[i].values())[0][1])
            val_2 = int(list(bag[i].values())[0][2])
         key_encode = key.encode("utf-8")
         len_key_encode = len(key_encode)
         binary_data = struct.pack (f'B{len_key_encode}sBBB',len_key_encode,key_encode,val_0,val_1,val_2)
         bytes_file.write(binary_data)
save(bag)
def load():
   bag = []
   with open ('arcanum_save_test.','rb') as bytes_file:
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
         
                

   return bag

print(load())



        



       
       
       


    