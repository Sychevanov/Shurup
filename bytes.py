import struct
n = int(input('Enter n: '))
with open ('bytes.','wb') as bytes_file:
    for i in range(1,n+1):
        binary_data = struct.pack ('H', i)
        bytes_file.write(binary_data)
        print(binary_data)


with open ('bytes.','rb') as bytes_file2:
    while True:
        binary_data2 = bytes_file2.read(2)
        if not binary_data2:
            break
        num, = struct.unpack('H',binary_data2)
        num = int(num)*2
        print(num)