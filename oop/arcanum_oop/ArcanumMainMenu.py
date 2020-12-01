from singletone import Singleton
class ArcanumMainMenu(metaclass=Singleton):
    def __init__(self):
        self.__listMenu = []
        # self.__listLocMenu = []

    def addMainMenu(self,menu):
        self.__listMenu.append(menu)

    # def addLocMenu(self,menu):
    #     self.__listLocMenu.append(menu)
    
    def mainRun(self):
        for menu in self.__listMenu:
            menu.run()

    # def locRun(self):
    #     for menu in self.__listLocMenu:
    #         menu.run()