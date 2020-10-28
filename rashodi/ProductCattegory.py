
class Singleton(type):

    instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls.instances:

            cls.instances[cls] = super().__call__(*args, **kwargs)

        return cls.instances[cls]

class ProductCattegory(metaclass=Singleton):
    def __init__(self):
        
        self.__productCattegory = {}


    
    def products(self):
        return self.__productCattegory
    

    def add(self,product):
        for key in ProductCattegory().products().keys():
            print('\n',key)
        name = input('Напишите наименование каттегории, если каттегории нет, впишите название: ')
        if name in self.__productCattegory.keys():

            self.__productCattegory[name].append(product)
        else:
            self.__productCattegory[name]=[product]

    





        


        