
from abc import ABCMeta, abstractmethod
class SodaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createBottle(self):
        pass
    @abstractmethod
    def createSoda(self):
        pass
    @abstractmethod
    def createLabel(self):
        pass
    @abstractmethod
    def createCloser(self):
        pass
