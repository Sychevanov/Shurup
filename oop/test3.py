from abc import ABCMeta, abstractmethod

class Currencies(metaclass=ABCMeta):
    def __init__(self,curr):
        self.set_curr = curr

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def sum(self,sum):
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

def transfer_usd (*args): 
    return sum(args)

def tran(method):
    return method.transfer()



x = int(input('Введите колличество РУблей: '))
rub = Rub(x)
x = int(input('Введите колличество Долларов: '))
usd = Usd(x)
x = int(input('Введите колличество Еувро: '))
eur = Eur(x)
y = input('В какую валюту хотите перевести свои деньги?: В рубли, доллары, евро?: ')
summ_usd = transfer_usd(tran(rub),tran(usd),tran(eur))


if y == 'рубли':
    print(f'{rub.sum(summ_usd)} столько рублей' )
elif y=='доллары':
    print(f'{summ_usd} столько долларов' )
else:
    print(f'{eur.sum(summ_usd)} столько евро' )



