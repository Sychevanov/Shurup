
from abc import ABCMeta, abstractmethod
class Soda(metaclass=ABCMeta):

    @abstractmethod
    def copy(self):
        pass