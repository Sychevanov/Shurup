#25 учеников есть мальчики есть еовчки, мальчики отимаются левочки приседают, 
# чтобы сдать жкзамен 20 раз надо сделать, создать 25 экземпляров классов со случайным полом, 
# опредлить у каждого сделать упражение, мальчики сделали 25 отжиманий, девочки 20 приседаний и сделать вывод,
#  посчитать сколько сделали больше 20 и вывести кто сдал
from abc import ABCMeta, abstractmethod
import random


class Student(metaclass=ABCMeta):
    @abstractmethod
    def zcht(self):
        pass

class Man(Student):
    def zcht(self):
        x = random.randint(0,50)
        print(f'Я отжался {x} раз')
        return x
        
class Woman(Student):
    def zcht(self):
        x = random.randint(0,50)
        print(f'Я присела {x} раз')
        return x

def manORwoman():
    boy = Man()
    girl = Woman()
    student_mass = []    
    for i in range(0,21):
        x = random.randint(0,1)
        if x == 1:
            student_mass.append(boy)
        else:
            student_mass.append(girl)
        
    return student_mass

#a = [x = random.randint(0,1) for i in range(0,21) if x == 1 a.append(boy) else a.append(girl) ] думал может можно как-то так сделать
#a = [random.randint(0,1) for i in range(0,21)]
#b = [boy if a[i]==1 else girl for i in a]

def zcht_fx(student_mass):
    x = 0
    for i in range(0,21):
        if student_mass[i].zcht() > 20:
            x = x + 1
            print(f'Ученик номер {i}, Экзамен сдан\n')
        else:
            print(f'Ученик номер {i}, Эзкамен не сдан \n')
    return x






def generator():    
    boy = Man()
    girl = Woman()
    c = [boy if random.randint(0,1) == 1 else girl for i in range(0,21)]
    x = 0
    for i in range(0,21): #можно ли пробежаться по массиву без цтикла?
        if c[i].zcht() > 20:
            x = x + 1
            print(f'Ученик номер {i}, Экзамен сдан\n')
        else:
            print(f'Ученик номер {i}, Эзкамен не сдан \n')
    return x


    

print(zcht_fx(manORwoman()))
#print(a)
#print(b)
#print(c)
print(generator())

    
