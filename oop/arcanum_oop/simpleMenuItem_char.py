from menuItem import Menu_item
from Char import Char
from charRegystry import CharRegystry
from fx import raceName, human
class Simple_menu_item_char(Menu_item):

    def __init__(self,title):       
        super().__init__(title)



    def run(self):
        race = self.get_title()
        raceName[race][0]()
        print('Хотите продолжить этой расой?\n')
        print('1. Да')
        print('2. Нет')
        x = int(input('Введите число: '))
        if x == 1:
            name = input('Введите имя персонажа')
        
            char = Char(name,race)
            CharRegystry().addChar(char)
            CharRegystry().raceCorrect(race)
            CharRegystry().printChar()
