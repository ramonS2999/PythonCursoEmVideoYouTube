from math import trunc
def porcao_int(n):
    print('A porção inteira de',n,'é',(trunc(n)))

def inteiro(n):
    print('A porção inteira de {} é {}!'.format(n, int(n)))

n = float(input('Digite um número: '))
porcao_int(n)
print(' ')
inteiro(n)