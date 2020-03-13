from random import randint

tupla = (randint(0, 10),
         randint(0, 10),
         randint(0, 10),
         randint(0, 10),
         randint(0, 10))

print(f'\n\t\t\tValores sorteados {tupla}')

print (f'\t\t\tMaior valor é {max(tupla)}')
print (f'\t\t\tMenor valor é {min(tupla)}')