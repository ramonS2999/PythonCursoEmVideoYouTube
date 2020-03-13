pessoas = homens = mulher =0
while True:
    idade = int(input('Informe a idade: '))
    while True:
        sexo = str(input('Informe sexo: [M/F]: ')).strip()[0]
        if sexo in 'MFmf':
            break
    if idade > 18:
        pessoas += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    while True:
        op = str(input('Quer continuar ou não? [S/N]: ')).strip()[0]
        if op in 'SsNn':
            break
    if op in 'Nn':
        break
print(f'Foram cadastrados {pessoas} pessoas com mais de 18 anos, {homens} homens, e {mulher} melher com menos de 20 anos!')
