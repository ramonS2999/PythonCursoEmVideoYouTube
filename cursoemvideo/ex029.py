import ansi

velocidade = float(input('\033[1;34;0mINFORME A VELOCIDADE EM Km/h:'))
mul = velocidade - 80
if velocidade > 80:
    print('\033[1;31;0mVOCÊ FOI MULTADO! ')
    print('VOCÊ PAGARÁ {:.2f}'.format(7*mul))
else:
    print('DIRIJA COM SEGURANÇA!')