tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
         'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:

    while True:

        num = int(input('\nDigite um número entre 0 e 20 >>> '))

        if (0 <= num <= 20):
            break

        print('\nNúmero invalido, digite novamente: ')


    print(f'\n\tO número digitado foi >>> {tupla[num]} <<<')

    op = str(input('\nAPERTE ZERO "0" PARA PARAR O PROGRAMA >>> '))

    if (op == '0'):
        break

print('\n\n\t\t\t\tFIM')