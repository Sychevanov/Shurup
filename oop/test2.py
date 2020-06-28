from abc import ABCMeta, abstractmethod

class Currencies(metaclass=ABCMeta):
    def __init__(self,curr):
        self.set_curr = curr

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def sum(self,seum):
        pass
    
    def sum_usd(self,curr): #можно ли в абстрактном классе оставить один обычный метод?
        return sum(curr)

class Rub(Currencies):
    
    @property
    def get_curr(self):
        return self.__curr

    @get_curr.setter
    def set_curr(self,curr):
        self.__curr = curr

    def transfer(self):
        return self.__curr / 80

    def sum(self,sum):
        return sum * 80



class Usd(Currencies):

    @property
    def get_curr(self):
        return self.__curr

    @get_curr.setter
    def set_curr(self,curr):
        self.__curr = curr
    
    def transfer(self):
        return self.__curr * 1
    
    def sum(self,sum):
        return sum 

class Eur(Currencies):

    @property
    def get_curr(self):
        return self.__curr

    @get_curr.setter
    def set_curr(self,curr):
        self.__curr = curr
    
    def transfer(self):
        return self.__curr * 1.12

    def sum(self,sum):
            return sum * 0.89


curr = []

x = int(input('Введите колличество РУблей: '))
rub = Rub(x)
curr.append(rub.transfer())
x = int(input('Введите колличество Долларов: '))
usd = Usd(x)
curr.append(usd.transfer())
x = int(input('Введите колличество Еувро: '))
eur = Eur(x)
curr.append(eur.transfer())
y = input('В какую валюту хотите перевести свои деньги?: В рубли, доллары, евро?: ')

summ_usd = usd.sum_usd(curr)


if y == 'рубли':
    print(f'{rub.sum(summ_usd)} столько рублей' )
elif y=='доллары':
    print(f'{summ_usd} столько долларов' )
else:
    print(f'{eur.sum(summ_usd)} столько евро' )


