

class Array:

    def __init__(self, n):
        self.array = [0 for x in range(0,n)] 

    def __repr__(self):
        return str(self.array)

    def __len__(self):  
        return len(self.array)

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value
                 
    def remove(self,key):                     
        del self.array[key]


    def append(self,val):
        return self.array.append(val)
    
    def insert(self,key,val):
        self.array.insert(key, val)



    def __iadd__(self, right):
        self.array.append(right)
        return self
    def __isub__(self, right):
        self.array.remove(right)
        return self









a = Array(3)
a.remove(1)
a.insert(0,34)
a+=20
a-=20
print(a)
