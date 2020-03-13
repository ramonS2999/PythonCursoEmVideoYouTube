from random import randint
from time import sleep
sorte = randint(0,5)
#print(sorte)
n = int(input('TENTE ACERTAR UM NÚMERO ENTRE 0 E 5:'))
print('PROCESSANDO...')
sleep(2)
if sorte == n:
    print('PARABENS VOCE ACERTOL! {}'.format(sorte))
else:
    print('QUE PENA O NÚMERO CERTO É {}'.format(sorte))
