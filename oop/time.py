#класс Время. поля: часы, минуты, секунды. методы: сеттеры и геттеры для всех полей
#  + метод сдвинуть время на заданное количество секунд, т.е. 15:16:17, сдвинуть на 120 сек -> 15:18:17
class Time():
    def __init__(self,hour,minut,sec):

        self.set_hour(hour)
        self.set_minut(minut)
        self.set_sec(sec)

    def set_hour(self,hour):
        if hour > 0 and hour < 25:
            self.__hour = hour
        else:
            print('Некорректно') # как избежать ошибки, если некорректно?

    def set_minut(self,minut):
        if minut > 0 and minut < 61:
            self.__minut = minut
        else:
            print('Некорректно')

    def set_sec(self,sec):
        if sec > 0 and sec < 61:
            self.__sec = sec
        else:
            print('Некорректно')
    
    def get_hour(self): #почему здесь мы не вводим параметр часы минуты секунды?
        return self.__hour
    def get_minut(self):
        return self.__minut
    def get_sec(self):
        return self.__sec

    def sdvig(self): #здесь лучше параметр, а не инпут?
        change_sec = int(input('Введите сколько секунд хотите добавить: '))
        h = change_sec // 3600 % 24
        m = change_sec // 60 % 60
        s  = change_sec % 60

        self.__hour = self.__hour + h # и еще переводы если больше 60 или 24
        self.__minut = self.__minut + m
        self.__sec = self.__sec + s





time = Time(23,56,34)
print(time.get_hour())
print(time.get_minut())
print(time.get_sec())
time.sdvig()
print(time.get_hour())
print(time.get_minut())
print(time.get_sec())

