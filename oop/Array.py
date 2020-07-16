#Создать класс Массив. Конструктор принимает кол-во элементов массива. 
# Реализовать методы size() -- размер массива, add() -- добавляет элемент массива,
#  remove(номер) -- удаляет элемент массива, insert(номер, значение) -- вставляет новый элемент по заданному номеру.
#  оператор [] -- для доступа к элементу, или методы getValue(номер) и setValue(номер, значение)
#Для статически типизированных языков -- тип элементов массива -- int



class Array:

    def __init__(self, n):
        self.array = [0 for x in range(0,n)] #про геттеры и сеттеры мне унжно здесь их делать если есть гет айтем и сет айтем и делать ли array __array

    def __repr__(self):
        return str(self.array)

    def __len__(self):  #size
        return len(self.array)

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value
                 
    def remove(self,key):                     
        del self.array[key]


    def append(self,val):#add
        return self.array.append(val)
    
    def insert(self,key,val):
        self.array.insert(key, val)











a = Array(3)
a.remove(1)
a.insert(0,34)
print(list(a))
