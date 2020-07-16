class Myint():
    def __init__(self,val):
        self.val = val
    def __add__(self,right):
        return self.val+right 
        #return self.val + right 
    def __float__(self):
        return float(self.val)
    def __str__(self):
        return str(self.val)
    def __index__(self):
        return self.val
        
a = Myint(4)
a = float(a)
print(a + 6)
a = str(a)
print(a + 'f')

