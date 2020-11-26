from MobileObject import MobileObject
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
        return self.__name

    @hands.setter
    def hands(self,hands):
        self.__hands = hands 

