from abc import ABCMeta, abstractmethod

#class Animal():
#    def say(self):
#        raise NotImplementedError('Метод абстрактный')

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass # можно даже определить поведение по-умолчанию


class Cat(Animal):
    def say(self):
        print('Mew')

class Dog(Animal):
    def say(self):
        print('WOW')

class Moo(Animal):
    def say(self):
        print('MOO')


def call(animal):
    animal.say()
#def call(a: Animal) зачем через вдоеточие писать класс?




cat = Cat()
dog = Dog()
Caw = Moo()

call(cat)

