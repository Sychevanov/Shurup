from arcanum_fx.picture_draw import * 
from arcanum_fx.proverka import proverka
def dialog_virgil(s):
    s[0] = ('Не может быть, Ваше появление — «Знак свыше», вы Избранный ')
    virdgil(s)
    print('1. Конечно! я же выжил после такого крушения, называй меня Мой Господин!')
    print('2. Наверное, мне просто повезло.')
    print('3. Отвали')
    x = proverka('Выберите ответ: ',1,3)
    os.system('cls' if os.name == 'nt' else 'clear')
    if x == 1:
        s[0] = 'Да... Скромности не занимать. Но в любом случае, предания говоярят,'
        s[1]= ' о том что выживет один - "Живущий", я пойду с вами'
        virdgil(s)
        print('1. Отлично, после такого, мне потребуется личный раб')
        print('2. Пойдем')
        print('3. Отвали')
        x = proverka('Выберите ответ: ',1,3)
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == 1:
            s[0] = '*Мыслит про себя* "Мда... Почему предания не говорили, '
            s[1] = 'что "Живущий" будет таким козлом." Идем Мой Господин.'
            s[2] = 'Нам нужно идти в деревню - Туманные холмы'
            s[3] = 'и встретиться со старейшиной Иоахимом'
            virdgil(s)
        if x == 2:
            s[0] = 'Тогда нам нужно идти в деревню - Туманные холмы '
            s[1] = 'и встретиться со старейшиной Иоахимом'
            virdgil(s)
        if x == 3:
            s[0] = 'Хотите Вы этого или нет, но я все равно пойду с вами' 
            virdgil(s)   
    elif x == 2:
        s[0] = 'Я монах - Вирджил, предания говоярят,'
        s[1]= ' о том что выживет один - "Живущий", я пойду с вами. '
        virdgil(s)
        print('1. Отлично, спутник мне не помешает')
        print('2. Отвали')
        x = proverka('Выберите ответ: ',1,2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == 1:
            s[0] = 'Тогда нам нужно идти в деревню - Туманные холмы '
            s[1] = 'и встретиться со старейшиной Иоахимом'
            virdgil(s)
        if x == 2:
            s[0] = 'Хотите Вы этого или нет, но я все равно пойду с вами'
            s[1] = 'Нам нужно идти в деревню - Туманные холмы '
            s[2] = 'и встретиться со старейшиной Иоахимом'
            virdgil(s)  
    elif x == 3:
        s[0] = 'Хотите Вы этого или нет, но я все равно пойду с вами'
        s[1] = 'Нам нужно идти в деревню - Туманные холмы '
        s[2] = 'и встретиться со старейшиной Иоахимом'
        virdgil(s) 
    input('Нажмите любую клавишу для продолжения: ')  
    os.system('cls' if os.name == 'nt' else 'clear')
    