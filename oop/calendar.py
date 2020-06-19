from time_props import Time

class Calendar(Time):
    def __init__(self,hour,minut,sec,year,month,day):
        Time.__init__(self,hour,minut,sec)
        #super().__init__(self,hour,minut,sec)
        self.year = year
        self.month = month
        self.day = day
        
    @property
    def year(self):
        return self.__year
    @property
    def month(self):
        return self.__month
    @property
    def day(self):
        return self.__day

    @year.setter
    def year(self,year):
        self.__year = year #проверку
    @month.setter
    def month(self,month):
        self.__month = month
    @day.setter
    def day(self,day):
        self.__day = day

  
    def sdvig(self,change_sec):
        super().sdvig(change_sec)
        if self.__hour > 24:
            d = (self.__hour + change_sec //3600) //24
        return d
        


    def shift_day(self,change_day): #переписать високосный год и тд
        found = True
        #change_day = int(input('Введите сколько дней хотите добавить: '))
        if change_day < 0:
            change_day = -change_day
            found = False
        y = change_day // 360
        m = change_day // 30 % 12
        d  = change_day % 30 
        if not found:
            y=-y
            m=-m
            d=-d        
        self.__day = self.__day + d
        if self.__day >= 30:
            self.__day = self.__day - 30
            self.__month = self.__month + 1
        self.__month = self.__month + m
        if self.__month >= 12:
            self.__month = self.__month - 12
            self.__year = self.__year + 1
        self.__year = self.__year + y 


    



calendar = Calendar(22,45,34,0,0,0)

print(calendar.hour)
#x = int(input('Введите сколько секунд хотите добавить: '))
#calendar.sdvig(x)
y = int(input('Введите сколько дней хотите добавить: '))
calendar.shift_day(y)
print(calendar.hour)
print(calendar.minut)
print(calendar.sec)
print(calendar.year)
print(calendar.month)
print(calendar.day)