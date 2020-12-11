from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, beginLocation1, textLocation1,infoChar_menu
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from Dialogs import dialogVirgil
from charRegystry import CharRegystry
class Fight():
    def __init__(self,mob):
        self.mob = mob

    def run(self):
        while True:
            pass


fight_menu = Menu(noBack=False)
fight_menu.addItems('Атаковать',foo)

fight_menu.addItems('Попытаться договориться',foo)
fight_menu.addItems('Сбежать',foo)
fight_menu.add_existing_submenu(infoChar_menu())


fight_menu.run()