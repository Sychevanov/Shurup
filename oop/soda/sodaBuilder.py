
from abc import ABCMeta, abstractmethod
class SodaBuilder(metaclass=ABCMeta):
    def __init__(self,factory):
        self.__factory = factory
        self.__bottle = factory.createBottle()

    def pourSoda(self):
        self.__bottle.pourSoda(self.__factory.createSoda())

    def putLabel(self):
        self.__bottle.putLabel(self.__factory.createLabel())

    def seal(self):
        self.__bottle.seal(self.__factory.createCloser())

    def build(self):
        return self.__bottle.copy()



