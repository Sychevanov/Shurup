from equip import Equip
import random

class Weapon(Equip):
    def __init__(self, name, price, power, miss):
        super().__init__(name, price,flag=True)
        self.__power = power
        self.__miss = miss
        self.__name = name

    @property
    def power(self):
        return random.randint(self.__power[0],self.__power[1])

    @power.setter
    def power(self,power):
        self.__power = power

    @property
    def miss(self):
        return self.__miss

    @miss.setter
    def miss(self,miss):
        self.__miss = miss
    
    @property
    def name(self):
        return self.__name,self.__power[0],self.__power[1]
    
    @name.setter
    def name(self,name):
        self.__name = name 

    



# Sword = Weapon('Меч',10,[1,4],70)
# Sword.namePower()
