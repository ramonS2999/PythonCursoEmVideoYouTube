listagem = ('Lápis', 1.75,
            'Borracha', 2.0,
            'Caderno', 15.9,
            'Estojo', 25.0,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
print('='*40)
print('\t\t  LISTAGEM DE PREÇOS')
print('='*40)

for i in range(0, 18):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')

print('='*40)