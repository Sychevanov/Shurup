from time_props import Time
# Вопрос, куда применить
class InvalidTimeException(Exception): #создаем свою ошибку, через роительский лкасс ошибок
    pass

def failing():
    raise InvalidTimeException("Неверный формат времени") # не до конца понимаю, что делает родительский класс, то что имя свое и написать, что в ошибке это да, а вот что именно делает класс не ясно

def recovering():
    try:
        failing() #попробуй эту фнкцию///// Она будет выполняться же всегда с ошибкой? если то тогда зачем вся эта коснструкция?
    except InvalidTimeException as e: #если возникла такая ошибка тогда этьо
        print(e)


def eror_date(month): #Это так для првоерки
    while True:
        try:
            if month >12 and month <=0:
                print('в году не может быть меньше или больше 12 меясцев ')
        except:
            print('Введите цифры а не буквы')
        else:
            self.__month = month


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
        self.__year = year
    @month.setter
    def month(self,month):
        if month < 12 and month > 0:
            self.__month = month
        else:
            recovering() #если здесь, то я моуг просто принтом написать, что ошибка при вводе даты, зачем ексепт? Если делать, то корректность ввода бесконечным циклом, чтобы введено было правильно
        #if month <=0 or month >12:
        #    recovering()
        #self.__month = month
    @day.setter
    def day(self,day):
        if day <= Calendar.chek_day_method(self.month,self.year):
            self.__day = day
        else:
           recovering()       

    #def sdvig(self,change_sec):
    #    super().sdvig(change_sec)
    #    if self.__hour > 24:
    #        d = (self.__hour + change_sec //3600) //24
    #    return d
    
   
    @staticmethod
    def is_leap(year): 
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    @staticmethod
    def chek_day_method(month,year): 
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        else:
            if Calendar.is_leap(year): # здесь же не нужен self.year?
                return 29
            else:
                return 28
            


    def shift_day(self,change_day):
        #вызвать функцию сдвиг, чтобы отдала, на сколько дней еще добавить и прибавить к чейндж дей
        #change_day = Time.sdvig(change_sec)
        found = True
        #change_day = int(input('Введите сколько дней хотите добавить: '))
        chek_day = Calendar.chek_day_method(self.month,self.year)
        if change_day < 0:
            change_day = -change_day
            found = False
        if Calendar.is_leap(self.year):
            chek_year = 366
        else:
            chek_year = 365
        y = change_day // chek_year
        m = change_day // chek_day % 12
        d =  change_day % chek_day 
        if not found:
            y=-y
            m=-m
            d=-d        
        self.__day = self.__day + d
        if self.__day >= chek_day:
            self.__day = self.__day - chek_day + 1
            self.__month = self.__month + 1
        self.__month = self.__month + m
        if self.__month > 12:
            self.__month = self.__month - 12
            self.__year = self.__year + 1
        self.__year = self.__year + y 


    



calendar = Calendar(24,45,34,1,1,1)

print(calendar.hour)
x = int(input('Введите сколько секунд хотите добавить: '))
calendar.sdvig(x)

y = int(input('Введите сколько дней хотите добавить: '))
calendar.shift_day(y)
print(calendar.hour)
print(calendar.minut)
print(calendar.sec)
print(calendar.year)
print(calendar.month)
print(calendar.day)