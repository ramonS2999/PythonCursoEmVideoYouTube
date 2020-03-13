
# meu, Ramon!

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
limite = razao * 9 + termo
i = 0
while termo <= limite:
    print(termo, end=' -> ')
    termo += razao
print('Fim')

#  curso em video
primeiro = int(input('\nPrimeiro termo: '))
raz = int(input('Razão: '))
ter = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(ter), end='')
    ter += raz
    cont += 1
print('FIM')