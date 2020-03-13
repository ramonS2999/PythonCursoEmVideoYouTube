peso = float(input('informe o peso da pessoa: '))
altura = float(input('informe a altura da pessoa: '))
imc = peso / (altura*altura)

if imc < 18.50:
    print('{:.2f} IMC, Abaixo do peso.'.format(imc))
elif imc <= 25:
    print('{:.2f} IMC, Peso ideal.'.format(imc))
elif imc < 30:
    print('{:.2f} IMC, Sobrepeso.'.format(imc))
elif imc < 40:
    print('{:.2f} IMC, Obesidade.'.format(imc))
else:
    print('{:.2f} IMC, Obisidade mórbida.'.format(imc))
