class Product():
    def __init__(self,name,price):
        #self.products = []
        self.name = name
        self.price = price 


class Products():
    def __init__(self):
        self.products = []


    def add(self, product):
        self.products.append(product)



Products().add(Product('ff',5))