import math
def cos_sen_tan(angulo):
    seno = math.sin(math.radians(angulo))
    print('O seno de {} é {:.2f}'.format(angulo, seno))
    cosseno = math.cos(math.radians(angulo))
    print('O cosseno {} é {:.2f}'.format(angulo, cosseno))
    tangente = math.tan(math.radians(angulo))
    print('A tangente {} é {:.2f}'.format(angulo, tangente))

angulo = float(input('Informe o ângulo: '))
cos_sen_tan(angulo)