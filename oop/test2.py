from abc import ABCMeta, abstractmethod

class Currencies(metaclass=ABCMeta):
    def __init__(self,curr):

        self.curr = curr

    @abstractmethod
    def transfer(self):
        pass

    @abstractmethod
    def sum(self,seum):
        pass
   
    def sum_usd(self,curr): #можно ли в абстрактном классе оставить один обычный метод?
        return sum(curr)

    def summm(self):
        pass

class Rub(Currencies):
    @property
    def curr(self):
        return self.__curr

    @curr.setter
    def curr(self,curr):
        self.__curr = curr
    
    def transfer(self):
        return self.__curr / 80

    def sum(self,sum):
        return sum * 80



class Usd(Currencies):
    @property
    def curr(self):
        return self.__curr
    @curr.setter
    def curr(self,curr):
        self.__curr = curr

    def transfer(self):
        return self.__curr * 1
    
    def sum(self,sum):
        return sum 

class Eur(Currencies):
    @property
    def curr(self):
        return self.__curr
    @curr.setter
    def curr(self,curr):
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

#сначала выбрать в какую валюту перевести а потом в сумму добавляется другие валюты
