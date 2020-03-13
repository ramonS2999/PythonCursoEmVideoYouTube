tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
          'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense','Ceará SC',
          'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')

for i in range(0, 20):
    print(f'{i+1}º {tabela[i]}')

print('\n\t\t\tOS 5 PRIMEIROS COLOCADOS\n')
for i in range(0, 5):
    print(f'|{1+i}º colocado {tabela[i]}')

print('\n\t\t\tOS 4 ULTIMOS COLOCADOS\n')
for c in range(16, 20):
    print(f'|{1+c}ª colocado {tabela[c]}')

print('\n\t\t\tORDEM ALFHABETICA\n')
for j in sorted(tabela):
    print('\t\t\t',j)

print('\n\t\t\tChapecoence está\n')
for g in range(0, 20):
    if ('Chapecoense' == tabela[g]):
        print(f'{tabela[g]} {g+1}ª colocação!')