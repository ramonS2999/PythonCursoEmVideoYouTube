n = int(input('Quantidade de termos da sequência de FIBONACCI: '))
a = 0
b = i = 1
while i <= n:
    print(a, end=' -> ')
    a, b = b, a+b
    i += 1
print('Fim')
