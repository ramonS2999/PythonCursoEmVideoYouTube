from random import randint
from time import sleep

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = lista[randint(0, 2)]

escolha = lista[int(input('''
VVamos jogar Jokenpô, escolha um número referente a opção:

0 - PEDRA
1 - PAPEL
2 - TESOURA  '''))]

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 'PEDRA':
    if escolha == 'PEDRA':
        print('EMPATE!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
    elif escolha == 'PAPEL':
        print('PARABÉNS VOCÊ VENCEU!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
    else:
        print('QUE PENA VOCÊ PERDEU!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
elif computador == 'PAPEL':
    if escolha == 'PAPEL':
        print('EMPATE!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
    elif escolha == 'PEDRA':
        print('QUE PENA VOCÊ PERDEU!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
    else:
        print('PARABÉNS VOCÊ VENCEU!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
else:
    if escolha == 'TESOURA':
        print('EMPATE!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
    elif escolha == 'PAPEL':
        print('QUE PENA VOCÊ PERDEU!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))
    else:
        print('PARABÉNS VOCÊ VENCEU!\nVOCÊ {}\nCOMPUTADOR {}'.format(escolha, computador))