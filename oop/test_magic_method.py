class Array:

    def __init__(self, n):
        self.array = [0 for x in range(0,n)]

    def __repr__(self): #вывод всего массива
        return str(self.array)

    def __len__(self): # не понимаю что делает
        return len(self.array)

    def __getitem__(self, key): # чтобы обращаться к эелементу массива сразу через экземпляр класса, я так понимаю
        return self.array[key]

    def __setitem__(self, key, value):# чтобы изменить значение по ключу
        self.array[key] = value

    def __delitem__(self, key):#удаляет
        del self.array[key]

    def __iter__(self): #  не успел разобраться 
        return iter(self.array)

    def __missing__(self, key): #не успел разобраться, как раотает и что писать в ретерне
        pass
    def __contains__(self,val): #не успел разобраться, как раотает и что писать в ретерне
        pass
    def append(self,val):
        return self.array.append(val)

#итог что я понял, я сделал из класса костяк массива со всеми его методами как и обычный массив?

def __contains__(self, val):
  for x in self.array:
    if x == val:
      return True
  return False



def __iter__(self):
  for x in self.array:
    yield x




a = Array(3)

print(a)
print(a[0])
a[0]=2
print(a[0])
del a[0]
print(a[0])
a.append(2)
for x in a:
    print(x)
print(a)
 