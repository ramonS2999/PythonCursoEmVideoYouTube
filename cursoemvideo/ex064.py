n = int(input('Digite um número [999 para rarar]: '))
soma = cont = 0
while n != 999:
    soma += n
    n = int(input('Digite um número [999 para rarar]: '))
    cont += 1
print('A quantidade de números digitados forão {}, e a soma entre eles é {}.'.format(cont, soma))
