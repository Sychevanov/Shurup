from equip import Equip

class Weapon(Equip):
    def __init__(self, name, price, power, miss):
        super.__init__(self, power, miss)
        self.__power = power
        self.__miss = miss

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self,power):
        self.__power = power

    @property
    def miss(self):
        return self.__miss

    @miss.setter
    def miss(self,miss):
        self.__miss = miss