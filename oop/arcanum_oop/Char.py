from MobileObject import MobileObject

class Char(MobileObject):
    def __init__(self,name,health,atack,head, body, boots, hands):
        super.__init__(self,head, body, boots, hands)
        self.__head = head
        self.__body = body
        self.__boots = boots
        self.__hands = hands

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self,head):
        self.__head = head 

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self,body):
        self.__body = body 

    @property
    def boots(self):
        return self.__boots

    @boots.setter
    def boots(self,boots):
        self.__boots = boots 
    
    @property
    def hands(self):
        return self.__name

    @hands.setter
    def hands(self,hands):
        self.__hands = hands 