from abc import ABCMeta, abstractmethod

class Figure(metaclass=ABCMeta):
    @abstractmethod
    def point_in(self, x,y):
        pass


class Square(Figure):
    def __init__(self,a):
        self.a = a # нужны ли сеттеры и геттеры?

    def point_in(self,x,y):
        if (x <= self.a and y <= self.a) and (x >= 0 and y >= 0): #квадрат в начале координат
            return True
        else:
            return False

class Ring(Figure):
    def __init__(self,r):
        self.r = r

    def point_in(self,x,y):
        if self.r >= (x**2 + y**2)**0.5: #уитывая что круг в начале координат
            return True
        else:
            return False

def foo(figure,x,y):
    if figure.point_in(x,y):
        print('точка попадает')
    else:
        print('Точка не попадает')


figure  = input('Какую фигуру хотите, круг или квадрат: ')
if figure == 'квадрат':# корректность ввода пока не буду делать
    a = int(input('Введите сторону квадрата: '))
    figure = Square(a)
elif figure == 'круг':
    r = int(input('Введите радиус окружности: '))
    figure = Ring(r)
x = int(input('введите координату х: '))
y = int(input('введите координату y: '))
foo(figure,x,y)