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