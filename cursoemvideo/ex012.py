n = float(input('Informe o valor do produto: '))
desconto = (5/100) * n
novo_preco = n - desconto
print(' ')
print('O desconto foi de {:.2f} Reais'.format(desconto))
print('O novo preço será {:.2f} Reais'.format(novo_preco))