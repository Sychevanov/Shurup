n1 = {'car': 'bmw','rt':'fd'}
n2 = {'car2': 'bmw2','rt':'fd'}
n = [n1,n2]

#car = [x['car'] for x in n]
#print(car)

#car2 = []
#for y in n:
#    car2.append(y['rt'])
#print(car2)

car = [x.get('car','нет кар') for x in n]
print(car)