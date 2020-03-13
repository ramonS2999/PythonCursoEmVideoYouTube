termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = termo + (10-1) * razao
for i in range(termo, dec + razao, razao):
    print(i, end=' -> ')
print('Acabou')