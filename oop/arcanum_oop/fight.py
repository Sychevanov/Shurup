from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, beginLocation1, textLocation1,infoChar_menu
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from Dialogs import dialogVirgil
from charRegystry import CharRegystry
from Mob import Mobs

class Fight():
    def __init__(self,fight_menu):
        self.mob = Mobs('волк',100,2) #генератор мобов надо сделать
        self.char = CharRegystry()
        self.fight_menu = fight_menu
        #self.i = 0
        #self.i =+ 1

    

    def printStep(self,i=+1):
        #self.i += 1
        #i = 1
        print('----------------------------------------------------------------------------------------------------')
        print(f'                                                 Ваш ход {i}')
        print('------------------------------------------------------------------------------------------------------')
        i =+ 1
        

    def stepMob(self,i=0):
        #i = 1
        print('----------------------------------------------------------------------------------------------------')
        print(f'                                                 Ход врага {i}')
        print('------------------------------------------------------------------------------------------------------')
        i += 1
        
    def atack(self):
        print('\n Вы атакуете')
        self.mob.health -= self.char.atack()
        print(self.char.atack())
        
        
        print(self.mob.health)
        if self.mob.health <= 0:
            print('Вы Победили')
            self.fight_menu.forsed_command = True
            
            



def fight():
    
    fight_menu = Menu(noBack=False)
    fight = Fight(fight_menu)
    fight_menu.setStartupCommand(fight.printStep)
    fight_menu.setTearDownCommand(fight.stepMob)
    fight_menu.addItems('Атаковать',fight.atack)

    fight_menu.addItems('Попытаться договориться',foo)
    fight_menu.addItems('Сбежать',foo)
    fight_menu.add_existing_submenu(infoChar_menu())


    fight_menu.run()