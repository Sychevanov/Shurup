from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, beginLocation1, textLocation1,infoChar_menu
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from charRegystry import CharRegystry
from Mob import Mobs
from ArcanumMainMenu import ArcanumMainMenu
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
        print(f'------------------------------------******Ваше здоровье:{self.char.health()}*******---------------------------------',end='')
        if self.char.health() // 10 < 0:
            print('-',end = '')
        if self.char.health() //10 <10:
            print('-')
        else:
            print('-')
        print(f'------------------------------------******Здоровье врага:{self.mob.health}******----------------------------------')
        print('------------------------------------******************************----------------------------------')


    def stepMob(self):
        self.char.healthCorrect(self.mob.atack)
        print('----------------------------------------------------------------------------------------------------')
        print(f'                                                 Ваш ход ')
        print('----------------------------------------------------------------------------------------------------')
        print('')
        print('------------------------------------******************************----------------------------------')
<<<<<<< HEAD
        print(f'------------------------------------******Ваше здоровье:{self.char.health()}*******---------------------------------',end='')
        if self.char.health() // 10 == 0:
            print('-',end = '')
        if self.char.health() //10 <10:
            print('--')
        else:
            print('--')
        print(f'------------------------------------******Здоровье врага:{self.mob.health}******----------------------------------')
        print('------------------------------------******************************----------------------------------\n\n')
=======
        print(f'------------------------------------******Ваше здоровье:{self.char.health()}*******------------------------------')
        print(f'------------------------------------******Здоровье врага:{self.mob.health}******-------------------------------')
        print('------------------------------------******************************-------------------------\n\n')
        if self.char.health() <= 0: 
            print('Вы проиграли!')
            input('Нажмите любую клавишу и Enter для продолжения:')
            os.system('cls' if os.name == 'nt' else 'clear')
            ArcanumMainMenu().listMenu[0].run()
            
>>>>>>> 7817fb67030d7ed7801cb35755371c1435f884df
        
        
    def atack(self):

        print('\n----------------------------------------------Вы атакуете-------------------------------------------\n\n')
        self.mob.health -= self.char.atack()
        print('------------------------------------------ Вы нанесли:',self.char.atack(),'урона ------------------\n\n')
        

        if self.mob.health <= 0:
            print('Вы Победили')
            self.fight_menu.forsed_command = True
            os.system('cls' if os.name == 'nt' else 'clear')
        
            
            



def fight():
    
    fight_menu = Menu(noBack=False)
    fight = Fight(fight_menu)
    fight_menu.setStartupCommand(fight.printStep)
    fight_menu.setTearDownCommand(fight.stepMob)
    fight_menu.addItems('Атаковать',fight.atack)

    fight_menu.addItems('Попытаться договориться(В разработке)',foo)
    fight_menu.addItems('Сбежать(В разработке)',foo)
    fight_menu.add_existing_submenu(infoChar_menu())


    fight_menu.run()