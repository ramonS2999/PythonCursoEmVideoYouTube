def dolar(n):
    dol = n / (3.27)
    print('Com {} Reais, você pode comprar {:.2f} Dólares!'.format(n, dol))

n = float(input('Informe a quantidade de Reais que tem na carteira: '))
dolar(n)