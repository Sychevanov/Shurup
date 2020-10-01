eat = 0
alcohol = 0
allProducts = [{'Продукты': eat}, {'Алкоголь': alcohol},]
print(len(allProducts))
print(list(allProducts[0].keys())[0])
print(allProducts)

for i in range(0,len(allProducts)): 
    if 'Продукты '!= list(allProducts[i].keys())[0]:
        print('все норм')
    else:
        print('Выберите каттегорию: ')

print(allProducts[1])