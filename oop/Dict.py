from Array import Array



class Dict:

    def __init__(self):
        self.dict = {} 

    def __repr__(self):
        return str(self.dict)

    def __len__(self):  
        return len(self.dict)

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value
                 
    def remove(self,key):                     
        del self.dict[key]


    

d = Dict()

d['rt']=Array(2)
print(d)