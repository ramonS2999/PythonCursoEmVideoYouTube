numero = int(input('Digite um numero: '))
escolha = int(input('''aperte o numero para transforma a base:
1 para binario:
2 para octal:
3 para hexadecimal
opção:'''))

resultado = []
if escolha == 1:
    while 0 < numero:
        cont = numero % 2
        resultado.append(cont)
        numero = numero // 2
    print('{} convertido pra binario é igual a {}'.format(numero,resultado[::-1]))
elif escolha == 2:
    while 0 < numero:
        cont = numero % 8
        resultado.append(cont)
        numero = numero // 8
    print('{} convertido pra octal é igual a {}'.format(numero,resultado[::-1]))
elif escolha == 3:
    #while 0 < numero:
        #cont = numero % 16
        #resultado.append(cont)
        #numero = numero // 16
    print('{} convertido pra hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Não há essa alternativa!')
