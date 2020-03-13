from datetime import date
atual = date.today().year
ano = int(input('informe o ano de nascimento do atleta: '))
idade = atual - ano

if idade <= 9:
    print('{} anos, atleta mirim!'.format(idade))
elif idade <= 14:
    print('{} anos, atleta infantil!'.format(idade))
elif idade <= 19:
    print('{} anos, atleta junior!'.format(idade))
elif idade <= 25:
    print('{} anos, atleta sénhor!'.format(idade))
else:
    print('{} anos, atleta master!'.format(idade))
