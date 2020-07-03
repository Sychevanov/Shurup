from abc import ABCMeta, abstractmethod
 
class Currencies(metaclass=ABCMeta):
    def __init__(self,curr):
        self.wallet = 0
        self.curr = curr
 
    @abstractmethod
    def transfer(self):
        pass
 
    @abstractmethod
    def add(self):
        pass
   
    @abstractmethod
    def get_wallet(self):
        pass
 
 
   
 
 
 
class Rub(Currencies):
 
    course = 80
 
 
    @property
    def curr(self):
        return self.__curr
   
    @curr.setter
    def curr(self,curr):
        self.__curr = curr
   
    def transfer(self):
        return self.__curr / Rub.course
   
    def add(self,curr):
        self.wallet = self.wallet + curr.curr / curr.course
 
    def get_wallet(self):
        return self.wallet * 80
 
 
 
 
class Usd(Currencies):
 
    course = 1
 
 
    @property
    def curr(self):
        return self.__curr
    @curr.setter
    def curr(self,curr):
        self.__curr = curr
 
    def transfer(self):
        return self.__curr * Usd.course
   
    def add(self,curr):
        self.wallet = self.wallet + curr.curr * curr.course
 
 
    def get_wallet(self):
        return self.wallet
   
 
 
class Eur(Currencies):
 
    course = 1.12
 
   
    @property
    def curr(self):
        return self.__curr
 
    @curr.setter
    def curr(self,curr):
        self.__curr = curr
   
    def transfer(self):
        return self.__curr * Eur.course
   
    def add(self,curr):
        self.wallet = self.wallet + curr.curr * curr.course
 

 
    def get_wallet(self):
        return self.wallet/0.89
 
 
 
x = int(input('Введите колличество РУблей: '))
rub = Rub(x)
 
x = int(input('Введите колличество Долларов: '))
usd = Usd(x)
 
x = int(input('Введите колличество Еувро: '))
eur = Eur(x)

x = int(input('Выберите в какой валюте будут храниться деньги: 1. Рубли, 2. Доллары, 3. Евро'))
if x == 1:
    rub.add(rub)
    rub.add(usd)
    rub.add(eur)
    print(rub.get_wallet())    
elif x == 2:
    usd.add(rub)
    usd.add(usd)
    usd.add(eur)
    print(usd.get_wallet())
else:
    eur.add(rub)
    eur.add(usd)
    eur.add(eur)
    print(eur.get_wallet())