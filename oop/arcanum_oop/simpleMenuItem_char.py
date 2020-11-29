from menuItem import Menu_item
from Char import Char
from charRegystry import CharRegystry
from fx import raceName, human
from Weapon import Weapon

class Simple_menu_item_char(Menu_item):

    def __init__(self,title,menu):       
        super().__init__(title)
        self.menu = menu



    def run(self):
        race = self.get_title()
        raceName[race][0]()
        print('Хотите продолжить этой расой?\n')
        print('1. Да')
        print('2. Нет')
        x = int(input('Введите число: '))
        if x == 1:
            self.menu.forsed_command = True
            name = input('Введите имя персонажа: ')
        
            char = Char(name,race)
            
            print('\nВыбеерите начальное снаряжение: ')
            print('1. Меч(1-4)')
            print('2. Кремневый пистолет(2-3)')
            print('3. Лук(0-6)\n') 
            x = int(input('Введите число: '))
            if x == 1:
                Sword = Weapon('Меч',10,[1,4],70)
                char.addWeapon(Sword)
            if x == 2:
                FlintlockPistol = Weapon('Кремневый пистолет',10,[2,3],70)
                char.addWeapon(FlintlockPistol)
            if x == 3:
                Bow = Weapon('Лук',10,[0,6],70)
                char.addWeapon(Bow)
            CharRegystry().addChar(char)
            CharRegystry().raceCorrect(race)
            CharRegystry().printChar()