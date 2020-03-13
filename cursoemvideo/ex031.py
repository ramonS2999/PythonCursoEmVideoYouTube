distan = float(input('INFORME A DISTÂNCIA EM Km: '))
if distan <= 200:
    pre = distan * 0.50
else:
    pre = distan * 0.45
print('VOCÊ PAGARÁ {:.2f} REAIS!'.format(pre))