op = 0
while op != '5':
    n1 = int(input('Digiyte um valor: '))
    n2 = int(input('Digite outro valor: '))
    op = input('''aperte o número referente a opção:    
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
    if op == '1':
        resultado = n1+n2
        print('A soma de {} + {} = {}\n'.format(n1, n2, resultado))
    elif op == '2':
        resultado = n1*n2
        print('A multiplicação de {} por {} = {}\n'.format(n1, n2, resultado))
    elif op == '3':
        if n1 > n2:
            resultado = n1
            print('O maior número é {}\n'.format(resultado))
        elif n2 > n1:
            resultado = n2
            print('O maior número é {}\n'.format(resultado))
        else:
            print('Os numeros são iguais!\n')
    elif op == '4':
        print('Carregando!\n')
    elif op == '5':
        print('Finalizando...')
    else:
        print('Opçâo invalida!')
print('Fim')
