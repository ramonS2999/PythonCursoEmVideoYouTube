n1 = int(input('DIGITE UMNÚMERO: '))
n2 = int(input('DIGITE OUTRO NÚMERO: '))
n3 = int(input('DIGITE MAIS UM NÚMERO: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O MAIOR NÚMERO É {}, E O MENOR É {}!'.format(maior, menor))