#25 учеников есть мальчики есть еовчки, мальчики отимаются левочки приседают, 
# чтобы сдать жкзамен 20 раз надо сделать, создать 25 экземпляров классов со случайным полом, 
# опредлить у каждого сделать упражение, мальчики сделали 25 отжиманий, девочки 20 приседаний и сделать вывод,
#  посчитать сколько сделали больше 20 и вывести кто сдал
from abc import ABCMeta, abstractmethod
from random import random
sudent_mass = []

class Student(metaclass=ABCMeta):
    @abstractmethod
    def zcht(self):
        pass

class Man(Student):
    def zcht(self):
        x = random.randint(0,100)
        #print(f'Я отжался {x} раз')
        return x
        
class Woman(Student):
    def zcht(self):
        x = random.randint(0,100)
        #print(f'Я присела {x} раз')
        return x
def manORwoman():
    boy = Man()
    student_mass = []
    girl = Woman()
    for i in range(0,21):
        x = random.randint(0,1)
        if x == 1:
            student_mass.append(boy)
        else:
            student_mass.append(girl)
    return student_mass

def zcht_fx(student_mass):
    for i in range(0,21):
        if student_mass[i].zcht() > 20:
            print('Экзамен сдан')
        else:
            print('Эзкамен не сдан')

manORwoman()

    
