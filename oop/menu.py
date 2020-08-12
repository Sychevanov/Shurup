from abc import ABCMeta, abstractmethod

class InvalidTimeException(Exception):
    pass

class Menu_item(metaclass=ABCMeta):
    def __init__(self,title):
        self.__title = title

    @abstractmethod
    def run(self):
        pass

    
    def get_title(self):
        return self.__title

class Menu(Menu_item):
    def __init__(self,title = '',flag = False):    
        super().__init__(title)  
        self.__list_menu_item = []
        self.__flag = flag

    def run(self):
        while True:

            if self.__flag == True:
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
        
    #def add(self, item):
    #    self.__list_menu_item.append(item)

    def addItems(self,title,foo):
        item = Simple_menu_item(title,foo)
        self.__list_menu_item.append(item)
        return item

    def addSubMenu(self,title):
        submenu = Menu(title)
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

class Simple_menu_item(Menu_item):

    def __init__(self,title,foo):       
        super().__init__(title)
        self.__foo = foo

    def run(self):
        self.__foo()

def foo():
    print('Hello')

#main_menu = Menu('Main_menu',True)
#student_menu = Menu('Students')
#main_menu.add(Menu('Main_menu_item_1'))
#main_menu.add(student_menu)
#simple = Simple_menu_item('Print',foo)
#main_menu.add(simple)
#student_menu.add(Menu('Students'))
#student_menu.add(Menu('Students2'))
#main_menu.run()
main_menu = Menu('',True)

file_menu = main_menu.addSubMenu('File')
file_menu.addItems('Create', foo)
file_menu.addItems('Open',foo)

edit_menu = main_menu.addSubMenu('Edit')
edit_menu.addItems('Return',foo)

main_menu.run()