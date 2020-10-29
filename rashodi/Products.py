class Products():
    def __init__(self):
        self.__products = []


    def products(self):
        return self.__products

    def add(self, product):
        self.__products.append(product)

    def summ(self, products):
        summ = 0
        for product in products:
            summ = summ + product.price
        return summ