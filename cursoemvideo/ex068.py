from random import randint
cont = 0
while True:
    computador = randint(0, 10)
    n = int(input('Escolha um número: '))
    soma = computador + n
    op = ' '
    while op not in 'IP':
        op = str(input('Você quer PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'O valor digitado pelo computador foi {computador}, e o seu foi {n}, a soma deles é {computador+n}!')
    print('PAR'if soma % 2 == 0 else 'IMPAR')
    if soma % 2 == 0:
        if op in 'Pp':
            cont += 1
            print(f'Parabens você venceu {cont} vez!')
        else:
            print('Você perdeu!')
            break
    if soma % 2 != 0:
        if op in 'Ii':
            cont += 1
            print(f'Parabens você venceu {cont} vez!')
        else:
            print('Você perdeu!')
            break
