from fx import raceName, proverka
from singletone import Singleton

class CharRegystry(metaclass=Singleton):

    def __init__(self):

        self.__char = None

    def addChar(self, char):
        self.__char = char

    def health(self):
        return self.__char.health

    def healthCorrect(self,correct):
        self.__char.health -= correct

    def atack(self):
        return self.__char.atack()

    def printChar(self):
        print('\nИмя',self.__char.name)
        print("Здоровье",self.__char.health)
        print("Сила",self.__char.strength)
        print("Ловкость",self.__char.agility)
        print("Шарм",self.__char.charm)
        print("Технология",self.__char.technology)
        print("Магия",self.__char.magic)
        self.__char.printHands()
        print('Атака', self.__char.atack())

    def raceCorrect(self,race):
        self.__char.health += raceName[race][1][0]
        self.__char.strength += raceName[race][1][1]
        self.__char.agility += raceName[race][1][2]
        self.__char.charm  += raceName[race][1][3]
        self.__char.technology += raceName[race][1][4]
        self.__char.magic += raceName[race][1][5]

    def addItem(self,item):
        self.__char.bag.append(item)


    def bagToHands(self):
        for i,item in enumerate(self.__char.bag): #доделать, меню"что сделать с предметом" выкинуть, надеть, почитать описание и тд"
            print(i+1, end='')
            item.printName()
        print(len(self.__char.bag)+1, 'Назад')
        #x = int(input('Введите номе предмета, котоырй хотите взять в руки: '))
        x = proverka('Введите номе предмета, котоырй хотите взять в руки: ',1,len(self.__char.bag)+1)
        if x == len(self.__char.bag)+1:
            return
        self.addItem(self.__char.hands)
        self.__char.addWeapon(self.__char.bag[x-1])
        del self.__char.bag[x-1]

    def infoChar(self):
        print('\nИмя',self.__char.name)
        print("Здоровье",self.__char.health)
        print("Сила",self.__char.strength)
        print("Ловкость",self.__char.agility)
        print("Шарм",self.__char.charm)
        print("Технология",self.__char.technology)
        print("Магия",self.__char.magic)
        print('Экипировка: ',end='')
        self.__char.printHands()
        #print('Атака', self.__char.atack())