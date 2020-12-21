from equip import Equip
import random

class Item(Equip):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.noWeapon = True


    def printName(self):
        print('',self.name)
    


    
