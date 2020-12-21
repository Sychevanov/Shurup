from menuItem import Menu_item
from simpleMenuIItem import Simple_menu_item
from simpleMenuItem_char import Simple_menu_item_char
from simpleMenuItem_fight import Simple_menu_item_fight
import os


class Menu(Menu_item):
    def __init__(self,title = '',flag = True, noBack = True,forsedExit = True, info = False, start = True):    
        super().__init__(title)  
        self.__list_menu_item = []
        self.__flag = flag
        self.__noBack = noBack
        self.forsedExit = forsedExit
        self.__info = info
        self.start = start
        self.startup_command = [] 
        self.forsed_command = None
        self.tear_down_command = None
        
       
    def run(self):
        if self.startup_command != None:

            for command in self.startup_command:
                command()
            
        while self.start != None:

            if self.forsed_command != None:

                break

            if self.__flag:
                exitt = 'Выход\n' 
            else:
                exitt = 'Назад\n'

            for i in range(len(self.__list_menu_item)):
                print(i+1,'',self.__list_menu_item[i].get_title())

            if self.__noBack:
                print(len(self.__list_menu_item)+1, '', exitt)

            x = self.proverka()

            if x == len(self.__list_menu_item)+1 :
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
            os.system('cls' if os.name == 'nt' else 'clear')

            self.__list_menu_item[x-1].run()

            if self.tear_down_command != None:

                self.tear_down_command()

            if self.forsedExit == False :
                    break

        
            

    def setTearDownCommand(self,programmCommand):
        self.tear_down_command = programmCommand
        
    def setStartupCommand(self,programmCommand):
        self.startup_command.append(programmCommand)

    def setNoExitCommand(self):
        self.noExit_command = True

    def startCommand(self):
        self.start = None

    def addItems(self,title,foo, flag = True,printText=''):
        item = Simple_menu_item(title,foo,flag,printText)
        self.__list_menu_item.append(item)
        return item

    def addFightItem(self,title,mob):
        item = Simple_menu_item_fight(title,mob)
        self.__list_menu_item.append(item)
        return item

    def addItemsChar(self,title,menu):
        item = Simple_menu_item_char(title,menu)
        self.__list_menu_item.append(item)
        return item

    def addSubMenu(self,title,noBack = True):
        submenu = Menu(title,False,noBack)
        self.__list_menu_item.append(submenu)
        return submenu

    def add_existing_submenu(self, submenu):

        self.__list_menu_item .append(submenu)
        return submenu



    def proverka(self):
        while True:
            x = input('Enter number: ')
            try:
                x = int(x)
                if x >= 1 and x <= len(self.__list_menu_item)+1:
                    break
                else: 
                    print(f'Введите число от {1} до {len(self.__list_menu_item)+1}')
            except:
                print('Введите цифру, а не букву')    
        return x

