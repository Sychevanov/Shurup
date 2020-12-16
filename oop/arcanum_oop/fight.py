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
import os

class Fight():
    def __init__(self,fight_menu):
        self.mob = Mobs('волк',100,2) #генератор мобов надо сделать
        self.char = CharRegystry()
        self.fight_menu = fight_menu
        self.flag = None

    

    def printStep(self):

        print('----------------------------------------------------------------------------------------------------')
        print(f'                                                 Ваш ход ')
        print('----------------------------------------------------------------------------------------------------')
        print('')
        print('------------------------------------******************************----------------------------------')
        print(f'------------------------------------******Ваше здоровье:{self.char.health()}*******------------------------------')
        print(f'------------------------------------******Здоровье врага:{self.mob.health}******-------------------------------')
        print('------------------------------------******************************-------------------------')


    def stepMob(self):
        self.char.healthCorrect(self.mob.atack)
        print('----------------------------------------------------------------------------------------------------')
        print(f'                                                Ход врага')
        print('----------------------------------------------------------------------------------------------------')
        print('')
        print(f'--------------------------------------Враг нанес вам {self.mob.atack} урона -------------------------')
        print('')
        print('------------------------------------******************************----------------------------------')
        print(f'------------------------------------******Ваше здоровье:{self.char.health()}*******------------------------------')
        print(f'------------------------------------******Здоровье врага:{self.mob.health}******-------------------------------')
        print('------------------------------------******************************-------------------------\n\n')
        
        
    def atack(self):

        print('\n----------------------------------------------Вы атакуете-------------------------------------------\n\n')
        self.mob.health -= self.char.atack()
        print('------------------------------------------ Вы нанесли:',self.char.atack(),'урона ------------------\n\n')
        

        if self.mob.health <= 0:
            print('Вы Победили')
            self.fight_menu.forsed_command = True
        elif self.char.health() <= 0: 
            print('Вы проиграли!')
            
            



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