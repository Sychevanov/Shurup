from bottle import Bottle


class ColaBottle(Bottle):
    def __init__(self):
        self.soda = None
        self.label = None
        self.closer = None
    def ColaBottle(self):
        print('Создали бутылку Cola')

    def pourSoda(self, soda):
        if self.closer == None:
            self.soda = soda
            print('Налили газировку')
        else:
            print('Бутылка закрыта')
    def putLabel(self,label):
        self.label = label
        print('Наклеили этикетку')
    def seal(self, closer):
        self.closer = closer
        print('Закрыли крышкой')

    def copy(self):
        result = ColaBottle()
        result.soda = self.soda.copy()
        result.label = self.label.copy()
        result.closer = self.closer.copy()
        return result
