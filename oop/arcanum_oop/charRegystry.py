from fx import raceName
class Singleton(type):

    instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls.instances:

            cls.instances[cls] = super().__call__(*args, **kwargs)

        return cls.instances[cls]

class CharRegystry(metaclass=Singleton):

    def __init__(self):

        self.__char = None

    def addChar(self, char):
        self.__char = char

    def printChar(self):
        print(self.__char.name)
        print(self.__char.strength)

    def raceCorrect(self,race):
        self.__char.health += raceName[race][1][0]
        self.__char.strength += raceName[race][1][1]
        self.__char.agility += raceName[race][1][2]
        self.__char.charm  += raceName[race][1][3]
        self.__char.technology += raceName[race][1][4]
        self.__char.magic += raceName[race][1][5]
