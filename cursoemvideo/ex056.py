media = 0
divisor = 0
maior = 0
cont = 0
n1 = 0
nome1 = ', não tem homem no grupo'
for i in range(1, 5):
    print('\n',':'*8, '{}º PESSOA'.format(i), ':'*8)
    nome = str(input('Digite o nome: '.format(i)))
    idade = int(input('Imforme a idade: '))
    sexo = str(input('Informe o sexo (m/f): ')).strip()
    media += idade
    divisor += 1
    if maior < idade and sexo in 'Mm':
        maior = idade
        nome1 = nome
        n1 = idade
    if sexo in 'Ff' and idade < 20:
        cont += 1
print('\nA media da idade do grupo é {} anos'.format(media/divisor))
print('O humem mais velho é {} e tem {} anos'.format(nome1, n1))
print('Ao todo são {} mulhere(s) com menos de 20 anos!'.format(cont))
