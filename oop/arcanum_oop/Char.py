from MobileObject import MobileObject
from  Weapon import Weapon
class Char(MobileObject):

    def __init__(self,name,race):
        super().__init__(name)
        self.__race = race
        self.__name = name
        self.__head = None
        self.__body = None
        self.__boots = None
        self.__hands = None
        self.health = 100
        self.strength = 1
        self.agility = 1
        self.charm = 1
        self.technology = 1
        self.magic = 1
        self.bag = [Weapon('Кремневый пистолет',10,[2,3],70)]


    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self,head):
        self.__head = head 

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self,body):
        self.__body = body 

    @property
    def boots(self):
        return self.__boots

    @boots.setter
    def boots(self,boots):
        self.__boots = boots 
    
    @property
    def hands(self):
        return self.__hands

    @hands.setter
    def hands(self,hands):
        self.__hands = hands 

    def printHands(self):
        print(self.__hands.name[0],'(',self.__hands.name[1],'-',self.__hands.name[2],')')
    
    def addWeapon(self,weapon):
        self.__hands = weapon

    def atack(self):
        if self.__hands != None:
            atack = int(self.__hands.power + self.strength + self.agility)
            return atack
        else:
            print('Вы бьете рукой')
            atack = int(self.strength + self.agility)
            return atack
        


