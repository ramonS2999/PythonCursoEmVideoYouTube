saque = int(input('Qual valor quer sacar? '))
reais_50 = reais_20 = reais_10 = reais_1 = 0

while saque > 0:

    print('='*40)

    if saque >= 50:
        reais_50 = saque // 50
        saque = saque % 50
        print(f'{reais_50} cédulas de R$50')

    if saque >= 20:
        reais_20 = saque // 20
        saque = saque % 20
        print(f'{reais_20} cédulas de R$20')

    if saque >= 10:
        reais_10 = saque // 10
        saque = saque % 10
        print(f'{reais_10} cédulas de R$10')

    if saque < 10:
        reais_1 = saque
        print(f'{reais_1} cédulas de R$1')
        break

print('='*40)
print('FIM')