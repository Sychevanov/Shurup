from menuItem import Menu_item
from simpleMenuIItem import Simple_menu_item
from simpleMenuItem_char import Simple_menu_item_char
from simpleMenuItem_fight import Simple_menu_item_fight
# from fx import infoChar
#from studentRegistry import StudentRegistry
#from editContext import EditContext

class Menu(Menu_item):
    def __init__(self,title = '',flag = True, noBack = True,forsedExit = True, info = False):    
        super().__init__(title)  
        self.__list_menu_item = []
        self.__flag = flag
        self.__noBack = noBack
        self.forsedExit = forsedExit
        self.__info = info
        self.startup_command = [] 
        self.forsed_command = None
        self.tear_down_command = None
        
       
    def run(self):
        if self.startup_command != None:

            for command in self.startup_command:
                command()
            
        while True:

            if self.forsed_command != None:
                # print('Должно вырубить')
                break

            if self.__flag:
                exitt = ' Выход\n' 
            else:
                exitt = 'Назад\n'
            
            # if self.__info == True: #доделать
            #     # self.addSubMenu('О персонаже')
            #     self.infoChar()

            for i in range(len(self.__list_menu_item)):
                print(i+1,' ',self.__list_menu_item[i].get_title())

            if self.__noBack:
                print(len(self.__list_menu_item)+1, '', exitt)

            x = self.proverka()

            if x == len(self.__list_menu_item)+1 :
                break
            
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

    # def infoChar(self):``

    #     info = self.addSubMenu('О персонаже')
    #     info.addItems('Харакатерисики',1)
    #     info.addItems('Журнал',1)
    #     info.addItems('Сумка',1)
    #     info.addItems('Инвертарь',1)

    # def setForsedCommand(self,programmCommand):
    #     self.forsed_command = programmCommand

    def addItems(self,title,foo):
        item = Simple_menu_item(title,foo)
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



#editContext = EditConext()
#main_menu = Menu('Main_menu',True)
#student_menu = Menu('Students')
#main_menu.add(Menu('Main_menu_item_1'))
#main_menu.add(student_menu)
#simple = Simple_menu_item('Print',foo)
#main_menu.add(simple)
#student_menu.add(Menu('Students'))
#student_menu.add(Menu('Students2'))
#main_menu.run()
