n = int(input('Digite um número: '))
soma = n
i = 0
print('O fatorial de {} é.'.format(n))
print('{}! = '.format(n), end='')
while n > i:
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
    if n != 0:
        soma = soma * n
print(soma)