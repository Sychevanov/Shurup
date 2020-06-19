#класс Время. поля: часы, минуты, секунды. методы: сеттеры и геттеры для всех полей
#  + метод сдвинуть время на заданное количество секунд, т.е. 15:16:17, сдвинуть на 120 сек -> 15:18:17
class Time():
    def __init__(self,hour,minut,sec):

        self.hour = hour
        self.minut = minut
        self.sec = sec

    def shift_day(self,chanche_day):
        pass

    @property
    def hour(self):
        return self.__hour

    @property
    def minut(self):
        return self.__minut

    @property
    def sec(self):
        return self.__sec

    @hour.setter
    def hour(self,hour):
        if hour > 0 and hour < 25:
            self.__hour = hour
        else:
            print('Некорректно')
    @minut.setter
    def minut(self,minut):
        if minut > 0 and minut < 61:
            self.__minut = minut
        else:
            print('Некорректно')
    @sec.setter
    def sec(self,sec):
        if sec > 0 and sec < 61:
            self.__sec = sec
        else:
            print('Некорректно')
    

    def sdvig(self,change_sec): 
        found = True
        #change_sec = int(input('Введите сколько секунд хотите добавить: '))
        if change_sec < 0:
            change_sec = -change_sec
            found = False
        h = change_sec // 3600 % 24
        m = change_sec // 60 % 60
        s  = change_sec % 60
        if not found:
            h=-h
            m=-m
            s=-s        
        self.__sec = self.__sec + s
        if self.__sec >= 60:
            self.__sec = self.__sec - 60
            self.__minut = self.__minut + 1
        self.__minut = self.__minut + m
        if self.__minut >= 60:
            self.__minut = self.__minut - 60
            self.__hour = self.__hour + 1
        self.__hour = self.__hour + h 
        if self.__hour >= 24:                     
            chanche_day = (self.__hour + change_sec //3600) //24
            self.__hour = self.__hour - 24  
            Time.shift_day(self,chanche_day) # хотел чтобы добавлялся 1 день в метод Календаря
        
        






#time = Time(22,45,34)
#print(time.hour)
#print(time.minut)
#print(time.sec)
#print('jjjj')
#x = int(input('Введите сколько секунд хотите добавить: '))
#time.sdvig(x)
#print(time.hour)
#print(time.minut)
#print(time.sec)

