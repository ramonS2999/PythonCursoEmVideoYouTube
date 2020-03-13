salario = float(input('INFORME O SALARIO ATUAL: '))
if salario <= 1250.00:
    por = (15/100)*salario
    novo_salario = ((15/100)*salario) + salario
else:
    por = (10/100)*salario
    novo_salario = ((10/100)*salario) + salario
print('O NOVO SALARIO SERÁ {} REAIS!'.format(novo_salario))
print('O ALMENTO FOI DE {:.2f} REAIS!'.format(por))