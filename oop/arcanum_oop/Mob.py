from MobileObject import MobileObject
class Mobs(MobileObject):
    def __init__(self,name,health,atack,agro = False):
        super().__init__(name)
        self.__agro = agro
        self.health = health
        self.atack = atack

    @property
    def agro(self):
        return self.__agro

    @agro.setter
    def agro(self,agro):
        self.__agro = agro

    
