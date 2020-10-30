from abc import ABCMeta, abstractmethod

class Closer(metaclass=ABCMeta):
    @abstractmethod
    def copy(self):
        pass
