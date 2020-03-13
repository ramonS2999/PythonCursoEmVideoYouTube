# meu, Ramon!
termo = restarte = int(input('Primeiro temor: '))
razao = int(input('Razão: '))
limite = razao * 9 + termo
adicao = 1
while adicao > 0:
    while termo <= limite:
        print(termo, end=' -> ')
        termo += razao
    print('Fim')
    adicao = int(input('\nQuantos termos quer a mais? '))
    if termo > 0:
        limite = (razao * (adicao-1)) + termo
        termo = restarte
print('FIM')


#  curso em video
primeiro = int(input('\nPrimeiro termo: '))
raz = int(input('Razão: '))
ter = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(ter), end='')
        ter += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais desejas? '))
print('Progressão ultilizado com {} termos.'.format(total))