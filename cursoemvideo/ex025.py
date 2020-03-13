nome = input('DIGITE SEU NOME COMPLETO: ').strip()
#print(nome.upper().find('SILVA'))
if nome.upper().find('SILVA') < 0:
    print('NÃO EXISTE SILVA NO NOME!')
else:
    print('SIM EXISTE NA POSIÇÃO',nome.upper().find('SILVA'))

print('TEM SILVA NO NOME? {}'.format('SILVA' in nome.upper()))