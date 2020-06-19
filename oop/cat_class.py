class Cat():
    def __init__(self,name,age,color):
        self.name = name # просто объявление перменной
        #if age >=0 and age <=30:
        #    self.__age = age
        #else:
        #    print('Некорректно')
        self.set_age(age) # вызов метода -сеттер, 

        self.__color = color # защищенная перменная

    def get_age(self):
        return self.__age # метод геттер, чтобы получить возраст кота, потму что незименяемая 

    def get_color(self):
        return self.__color #тоже самое

    def set_age(self,age):
        if age >=0 and age <=30: # проверка корректности возраста 
            self.__age = age
        else:
            print('Некорректно')
    def mew(self):
        print('Кот мяукает')
    def sleep(self):
        print('Кот спит')
    def eat(self):
        print('Кот ест')

