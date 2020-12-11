from abc import ABCMeta, abstractmethod

class Equip(metaclass=ABCMeta):
    def __init__(self, name, price, flag = True):
        self.__name = name
        self.__price = price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name 
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,price):
        self.__price = price 

    def printName(self):
        print(self.name)