
w=input("Vedite shirinu: ")
h=input("Vedite visotu: ")
x=input ('vvedite koordinatu X: ')
y=input("vvedite koordinatu Y: ")
w=int(w)
h=int(h)
x=int(x)
y=int(y)
if x>0 and x<w and y>0 and y<h:
    print ('V pryamougolnike')
elif ((x==0 or x==w) and y>=0 and y<h) or ((y==0 or y==h) and x>=0 and x<w) :
    print ('na perimetre')
else:
    print ('ne tam')
