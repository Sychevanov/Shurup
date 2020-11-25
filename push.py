appLead = int(input('Введите цену подтвержденного лида: '))
approve = 0.3
leads = int(input('Введите колличество лидов: '))
cpl = float(input('Введите CPL: '))
costs = float(input('Введите costs: '))

cplCalc = (costs + (appLead*approve))/leads

if cplCalc<=cpl or cplCalc >=appLead* approve :
    print('вырубай тиз нахрен')
else:
    print('Жди пока cpl будет', cplCalc )