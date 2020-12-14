from menuItem import Menu_item
from Char import Char
from charRegystry import CharRegystry
from fx import raceName, human
from Weapon import Weapon

class Simple_menu_item_fight(Menu_item):

    def __init__(self,title,mob):       
        super().__init__(title)
        self.menu = mob



    def run(self):
        print('act1')