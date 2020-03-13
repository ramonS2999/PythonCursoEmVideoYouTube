from random import randint
print('Digite um numero entri 0 e 10!')
chave = randint(0, 10)
palpite = False
cont = 0
while not palpite:
    tentativas = int(input('Digite a {}ª tentativa: '.format(cont+1)))
    if tentativas > chave:
        print('É menor!\n')
    elif tentativas < chave:
        print('É maior!\n')
    else:
        palpite = True
    cont += 1
print('Parabens você acertou o numero correto {} em {} tentativas!'.format(chave, cont))
