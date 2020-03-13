n = input('Digite seu nome: ').strip().title()
sexo = 'H'
while sexo not in 'MF':
    sexo = input('Informe o sexo: ').strip().upper()[0]
if sexo == 'M':
    sexo = 'masculino'
elif sexo == 'F':
    sexo = 'Feminino'
#print('Seu nome é {}, e seu sexo é {}!'.format(n, sexo))
print(f'Seu nome é {n}, e seu sexo é {sexo}!')

