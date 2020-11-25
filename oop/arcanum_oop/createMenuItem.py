from menuItem import Menu_item
class Simple_menu_item(Menu_item):

    def __init__(self,title,foo):       
        super().__init__(title)
        self.__foo = foo

    def run(self):
        self.__foo()