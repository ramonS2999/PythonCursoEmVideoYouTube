soma = 0
for i in range(501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print('A soma de todos os números é',soma)

cont = 0
for j in range(1, 501, 2):
    if j % 3 == 0:
        cont += j
print('A soma de todos os números é',cont)
