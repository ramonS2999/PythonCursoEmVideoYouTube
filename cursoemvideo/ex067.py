while True:
    n = int(input('Quer ver a tabuada de qua valor? '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
print('Fim do programa!')
