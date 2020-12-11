from abc import ABCMeta, abstractmethod
from copy import copy
 
class MenuItem(metaclass=ABCMeta):
    def __init__(self, title, parent):
        self.title = title
        self.parent = parent
    
    @abstractmethod
    def copy(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
 
class SimpleMenuItem(MenuItem):
    def __init__(self, title, parent, action):
        super().__init__(title, parent)
        self.action = action
 
    def copy(self):
        return SimpleMenuItem(self.title, self.parent, self.action)
    
    def run(self):
        self.action(self.parent)
 
class Menu(MenuItem):
    def __init__(self, title="", parent=None, is_main=True):
        super().__init__(title, parent)
        self.items = []
        self.is_main = is_main
        self.startup_commands = []
        self.before_select_commands = []
        self.tear_down_commands = []
        self.is_running = False
 
    def copy(self):
        menu_copy = Menu(self.title, self.parent, self.is_main)
        for item in self.items:
            menu_copy.items.append(item.copy())
        menu_copy.startup_commands = copy(self.startup_commands)
        menu_copy.before_select_commands = copy(self.before_select_commands)
        menu_copy.tear_down_commands = copy(self.tear_down_commands)
        return menu_copy
    
    def add_menu_item(self, title, action):
        item = SimpleMenuItem(title, self, action)
        self.items.append(item)
        return item
 
    def add_submenu(self, title):
        submenu = Menu(title, self, False)
        self.items.append(submenu)
        return submenu
 
    def add_existing_submenu(self, submenu):
        submenu = submenu.copy()
        submenu.parent = self
        self.items.append(submenu)
        return submenu
 
    def stop(self):
        self.is_running = False
 
    def run(self):
        self.is_running = True
 
        for command in self.startup_commands:
            result = command(self)  # menu = self, для отмены перехода menu.stop()
            if not result:  # для прекращения выполнения остальных startup_command, return False
                return
 
        while self.is_running:
            for command in self.before_select_commands:
                command(self)
            self.__print_items()
            self.__handle_user_input()
        
        for command in self.tear_down_commands:
            command(self)
 
    def __print_items(self):
        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item.title}")
        
        exit_name = "Выход" if self.is_main else "Назад"
        print(f"{len(self.items) + 1}. {exit_name}")
    
    def __handle_user_input(self):
        try:
            num = int(input("> ")) - 1
        except ValueError:
            print("Некорретное значение ввода")
            return
        
        if num == len(self.items):
            self.stop()
            return
        
        if num < 0 or num > len(self.items):
            print("Такого пункта не существует")
            return
        
        self.items[num].run()
 
def test_action(menu):
    x = input("Выйти? [y/n]: ")
    if x.lower() == "y":
        menu.stop()
    else:
        print("Привет, мир!")
 
def main():
    shared_menu = Menu("Информация о персонаже", is_main=False)
    shared_menu.add_menu_item("Инвентарь", test_action)
    shared_menu.add_menu_item("Характеристики", test_action)
 
    game_menu = Menu()
    game_menu.add_menu_item("Первое действие", test_action)
    submenu = game_menu.add_submenu("Второе действие")
    submenu.add_menu_item("Вариант второго действия", test_action)
    submenu.add_existing_submenu(shared_menu)
    game_menu.add_existing_submenu(shared_menu)
 
    game_menu.run()
 
if __name__ == "__main__":
    main()