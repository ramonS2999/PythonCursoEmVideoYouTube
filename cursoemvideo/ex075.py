tupla = (int(input('1º valor: ')),
         int(input('2º valor: ')),
         int(input('3º valor: ')),
         int(input('4º valor: ')))

print(f'\nOs valores digitados foram {tupla}\n')

print(f'É um número par >>>', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end= ' ')

if 3 in tupla:
    print(f'\nO número 3 está na {1+tupla.index(3)}ª posição.')
else:
    print('\nValor 3 não foi digitado em nenhuma posição.')

print(f'9 aparecel {tupla.count(9)} veses.')
