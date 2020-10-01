from menuItem import Menu_item
from simpleMenuIItem import Simple_menu_item
from studentRegistry import StudentRegistry
from editContext import EditContext

class Menu(Menu_item):
    def __init__(self,title = '',flag = True):    
        super().__init__(title)  
        self.__list_menu_item = []
        self.__flag = flag
        startup_command = None 
        before_select_command = None
        tear_down_command = None

    def run(self):
        if startup_command != None:

            startup_command()

        while True:

            if before_select_command != None:
                before_select_command()

            if self.__flag:
                exitt = 'Exit' 
            else:
                exitt = 'Return'

            for i in range(len(self.__list_menu_item)):
                print(i+1,' ',self.__list_menu_item[i].get_title())

            print(len(self.__list_menu_item)+1, '', exitt)

            x = self.proverka()
            
            if x == len(self.__list_menu_item)+1:
                print('Exit')
                break

            self.__list_menu_item[x-1].run()

        if tear_down_command != None:

            tear_down_command()
        

    def addItems(self,title,foo):
        item = Simple_menu_item(title,foo)
        self.__list_menu_item.append(item)
        return item

    def addSubMenu(self,title):
        submenu = Menu(title,False)
        self.__list_menu_item.append(submenu)
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
