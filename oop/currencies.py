from abc import ABCMeta, abstractmethod

class Currencies(metaclass=ABCMeta):
    def __init__(self,curr):
        self.set_curr = curr

    @abstractmethod
    def get_curr(self):
        pass
    @abstractmethod
    def transfer(self):
        pass

class Rub(Currencies):
    
    @property
    def get_curr(self):
        return self.__curr

    @get_curr.setter
    def set_curr(self,curr):
        self.__curr = curr

    def transfer(self):
        return self.__curr / 80


class Usd(Currencies):

    @property
    def get_curr(self):
        return self.__curr

    @get_curr.setter
    def set_curr(self,curr):
        self.__curr = curr
    
    def transfer(self):
        return self.__curr * 1

class Eur(Currencies):

    @property
    def get_curr(self):
        return self.__curr

    @get_curr.setter
    def set_curr(self,curr):
        self.__curr = curr
    
    def transfer(self):
        return self.__curr * 1.12

def transfer (a,b,c):
    return a.transfer() + b.transfer() + c.transfer()



x = int(input('Введите колличество РУблей: '))
rub = Rub(x)
x = int(input('Введите колличество Долларов: '))
usd = Usd(x)
x = int(input('Введите колличество Еувро: '))
eur = Eur(x)
summ_usd = transfer(rub,usd,eur)
#print(rub.get_curr)
print(summ_usd)
#print(rub.transfer())
#print(usd.transfer())
#print(eur.transfer())

