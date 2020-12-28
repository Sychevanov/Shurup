from equip import Equip

class Armor(Equip):
    def __init__(self, name, price, armor):
        super().__init__(self, armor)
        self.__armor = armor
        
    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,armor):
        self.__armor = armor