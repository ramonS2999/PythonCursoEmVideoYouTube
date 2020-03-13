r1 = float(input('DIGITE O TAMANHO DE LADO: '))
r2 = float(input('DIGITE OUTRO LADO: '))
r3 = float(input('DIGITE MAIS UM LADO: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('SIM DÁ PARA FORMAR UM TRIANGULO!')
else:
    print('NÃO, NÃO DÁ PARA FORMAR UM TRIANGULO!')