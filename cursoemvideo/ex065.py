op = 'S'
i = soma = maior = menor = divisor = 0
while op in 'Ss':
    n = int(input('Digite um número: '))
    if maior == menor == 0:
        maior = menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    soma += n
    divisor += 1
    op = input('Quer continuar? [S] para sim: ').strip().upper()
    if op == 'S':
        print('CARREGANDO...')
resutado = soma / divisor
print('O maior nº é {}!\nO menor nº é {}!\nA quantidade de números digitados é {}!\nE a media desses números é {}!'.format(maior, menor, divisor, resutado))
