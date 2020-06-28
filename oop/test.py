from abc import ABCMeta, abstractmethod

class Currencies(metaclass=ABCMeta):
    def __init__(self,curr):
        self.set_curr = curr

    @abstractmethod
    def transfer(self):
        pass
    def sum(self,curr):
        return sum(cur)

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

def transfer_usd (*args): #добавить в каждфый класс метод чтобы туда передавался параметр сумма в юсд и возвращает сумму умножениию на валюту и добавить статические поля сколько стоит каждая валюта в долларах
    return sum(args)

def transfer_rub(summ_usd):
    return summ_usd*80

def transfer_eur(summ_usd):
    return summ_usd*0.89

def tran(method):
    return method.transfer()


cur = []
x = int(input('Введите колличество РУблей: '))
rub = Rub(x)
cur.append(rub)
x = int(input('Введите колличество Долларов: '))
usd = Usd(x)
cur.append(usd)
x = int(input('Введите колличество Еувро: '))
eur = Eur(x)
cur.append(eur)
y = input('В какую валюту хотите перевести свои деньги?: В рубли, доллары, евро?: ')
print(cur)
print(sum(cur.trnsfer()))
