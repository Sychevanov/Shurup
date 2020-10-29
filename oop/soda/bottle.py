from abc import ABCMeta, abstractmethod


class Bottle(metaclass=ABCMeta):
    @abstractmethod
    def pourSoda(self,soda):
        pass
    @abstractmethod
    def putLabel(self,label):
        pass
    @abstractmethod
    def seal(self,closer):
        pass
    @abstractmethod
    def copy(self):
        pass

