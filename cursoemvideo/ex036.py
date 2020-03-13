valor_casa = float(input('informe o valor da casa: '))
salario_comprador = float(input('informe a quantidade do salario do comprador: '))
quantidade_ano = int(input('informe a quantidade de ano que irá ser pago: '))

parcela = valor_casa/(quantidade_ano*12)

if parcela <= ((salario_comprador * 30)/100):
    print('O vaor da prestação será {:.2f}.'.format(parcela))
else:
    print('O valor {:.2f} é maior que 30% do salario {:.2f}! Infeismente não poderá fazer o imprestimo!'.format(parcela, salario_comprador))
