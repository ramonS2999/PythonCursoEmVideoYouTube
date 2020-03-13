nome = input('Digite seu nome completo: ')

def nome_completo(nome):
    print('O nome',nome,'em maisculo é',nome.upper())
    print('O nome',nome,'em minusculo é',nome.lower())
    print('Separado em uma lista é',nome.split())
    x = nome.split()
    print('O tamanho da lista é',len(x[0:][::]))
    print('O primeiro nome tem',len(x[0]),'letras')
    print('A quantidade de letras ao todo são',len(''.join(x)))

nome_completo(nome)