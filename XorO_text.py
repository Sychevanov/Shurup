a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]    
xORo = ''
p1 = input('Игрок Х, введите имя: ')
p2 = input('Игрок О, введите имя: ')
tr = False
def win2(a):
    for k in range(3):
        if a[0][k] == a[1][k] == a[2][k] != ' ' :            
            return True
        if a[k][0]==a[k][1] == a[k][2] != ' ' :
            return True
    if a[0][0]==a[1][1]==a[2][2]!= ' ':
        return True
    if a[0][2]==a[1][1]==a[2][0]!= ' ':
        return True
        
    return False
for o in range(9):     
    if o%2==0:
        xORo = 'x'
    else:
        xORo = '0'
    x = int(input(f'игрок {xORo} Введите коокрдинату х: '))
    y = int(input(f'игрок {xORo} Введите коокрдинату y: '))
    while not(x>=0 and x<3 and y>=0 and y<3 and a[x][y]==' '):
        print('введите корректно!')
        x = int(input(f'игрок {xORo} Введите коокрдинату х: '))
        y = int(input(f'игрок {xORo} Введите коокрдинату y: '))
        o=o-1
    a[x][y]=xORo
    for i in range(3):
        for j in range(3):       
            print('+ - ', end = '')
        print('+')
        for j in range(3):      
            print(f'| {a[i][j]} ', end = '')                
        print('|')
    for j in range(3):       
        print('+ - ', end = '') 
    print('+')
    
    if win2(a):
        print(f'win player {xORo}')
        break
        
if o==8 and not win2(a):
    print('ничья')

if  xORo=='x':
    p=p1
else:
    p=p2

found = False
full = []
i = 0

with open ('xORo.txt','r') as y:
    while True:
        s = y.readline()
        if not s:
            break
        full.append(s)        
        a = s.split(' ')        
        if a[0]==p:  
            a[-1]=str(int(a[-1])+1)
            a = ' '.join(a) 
            a = a + '\n'
            full[i] = a
            found = True  
        i = i + 1    
        a = ['']
    #print(full)  
    #print(a)
    #print(a[0])
if not found:
    s = p + ' - 1\n'
    full.append(s)
    #with open('xORo.txt','a') as f:
        #f.write(f'{p} - 1\n')
with open ('xORo.txt','w') as f:
    for i in range(len(full)):
        f.write(f'{full[i]}') 