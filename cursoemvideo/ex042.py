lado1 = float(input('informe o primeiro lado do triânguo: '))
lado2 = float(input('informe o segundo lado do triângulo:'))
lado3 = float(input('informe o terceiro lado do triângulo; '))

if (lado1+lado2) > lado3 and (lado2+lado3) > lado1 and (lado1+lado3) > lado2:
    if lado1 == lado2 == lado3:
        print('O triangulo é EQUILÁTERO!')
    elif lado1 != lado2 != lado3 != lado1:
        print('O triângulo é ESCALENO')
    else:
        print('O triângulo é ISÓSCELIS')
else:
    print('Não dá para formar um triângulo!')
