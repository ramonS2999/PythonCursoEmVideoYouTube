from datetime import date

atual = date.today().year
ano = int(input('informe o ano de nascimento: '))
idade = atual - ano

if idade < 18:
    tempo = 18 - idade
    print('ainda não está no tempo de se alistar!\nvalta {} ano(s)!'.format(tempo))
    saldo = atual + tempo
    print('Seu alistamento será em {}'.format(saldo))
elif idade > 18:
    tempo = idade - 18
    print('ja passol do tempo!\n{} ano(s) se passol'.format(tempo))
    saldo = atual - tempo
    print('Seu alistamento foi em {}'.format(saldo))
else:
    print('está na hora!!!')
