from menuItem import Menu_item
from Char import Char
from charRegystry import CharRegystry
from fx import raceName, human
class Simple_menu_item_char(Menu_item):

    def __init__(self,title):       
        super().__init__(title)



    def run(self):
        race = self.get_title()
        raceName[race]()
        x = input('Хотите продолжить этой расой?')
        if x == 'Да':
            name = input('Введите имя персонажа')
        
            char = Char(name,race)
            CharRegystry().addChar(char)
