def almento_salario(n):
    almento = (15/100) * n
    novo_salario = n + almento
    print('O almento foi de {:.2f} Reais, e o novo salario é {:.2f} Reais'.format(almento,novo_salario))

n = float(input('Informe o salario: '))
almento_salario(n)