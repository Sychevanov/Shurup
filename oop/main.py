from cat_class import Cat

cat = Cat('Кошка',12,'Синий')
print(cat.name)
cat.mew()
print(cat.get_age())
cat.set_age(13)
print(cat.get_age())
cat.set_age(50)
print(cat.get_age())
print(cat.get_color())
