total = mais_1000 = mais_barato = 0
nome_barato = 'Todos iguais'

while True:

    print('_'*40)

    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Informe o preço do produto: '))

    print('_'*40)

    total += preco

    if preco > 1000:
        mais_1000 += 1
    
    if mais_barato == 0:
        mais_barato = preco
        nome_barato = nome
    
    if preco < mais_barato:
        mais_barato = preco
        nome_barato = nome
    
    while True:
        op = str(input('Quer continuar? [S/N]: ')).strip()[0]
        if op in 'SsNn':
            break
   
    if op in 'Nn':
        break

print(f'''
    +-----------------------------------------------------------------------------------------+
    | O total da compra é de {total} reais, {mais_1000} produtos cunstam                      
    | mais de 1000 reais, "{nome_barato}" é o produto mais barato e custa {mais_barato} reias!
    |                                                                                         
    +-----------------------------------------------------------------------------------------+''')