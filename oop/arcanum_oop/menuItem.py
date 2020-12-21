from abc import ABCMeta, abstractmethod

class Menu_item(metaclass=ABCMeta):
    def __init__(self,title):
        self.__title = title

    @abstractmethod
    def run(self): #execute
        pass
    
    def get_title(self):
        return self.__title
    def editTitle(self):
        self.__title = self.__title + '(Осмотрено)'