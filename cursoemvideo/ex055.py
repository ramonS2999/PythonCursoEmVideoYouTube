maior = 0
menor = 999
for i in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if menor > peso:
        menor = peso
print('O maior peso é {}Km'.format(maior))
print('e o menor peso é {}Km'.format( menor))



maior = 0     # Guanabara
menor = 0
for i in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso
print('O maior peso é {}Km'.format(maior))
print('e o menor peso é {}Km'.format( menor))
