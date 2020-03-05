def bread(func):
    def wrapper():
        print ("</------\>")
        func()
        print ("<\______/>")
    return wrapper
 
def ingredients(func):
    def wrapper():
        print ("#помидоры#")
        func()
        print ("~салат~")
    return wrapper
    
#@bread
#@ingredients
def sandwich(food="--ветчина--"):
    print (food)
 
a = bread(ingredients(sandwich))
#a()

def bulka1(func):
    def wrapper():
        print('Булка1')
        func()
    return wrapper
def bulka2(func):
    def wrapper():
        
        func()
        print('Булка2')
    return wrapper

def buter(food2 = 'Колбаса'):
    print(food2)

#buter = bulka1(bulka2(buter))
#buter()
bulka1(buter)()