from math import hypot
def catetos_hipotenusa(co,ca):
    hi = (co**2 + ca**2) ** (1/2)
    print('A hipotenusa é {:.2f}'.format(hi))

def hipcat_math(co,ca):
    hi = hypot(co,ca)
    print('A hipotenusa é {:.2f}'.format(hi))

co = float(input('Digite cateto oposto: '))
ca = float(input('Digite cateto adjacente: '))
catetos_hipotenusa(co, ca)
print(' ')
hipcat_math(co, ca)