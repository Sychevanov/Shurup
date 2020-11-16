from abc import ABCMeta, abstractmethod

class MobileObject(metaclass=ABCMeta):
    def __init__(self, name, health, atack):
        self.__name = name
        self.__health = health

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name 

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self,health):
        self.__health = health

    @property
    def atack(self):
        return self.__atack

    @atack.setter
    def atack(self,atack):
        self.__atack = atack

    def infoPrint(self):
        print(self.__name)
        print(self.__health)