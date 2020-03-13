print('{:=^60}'.format(' LOJAS RAMON SILVA '))
pagamento = float(input('Preço das compras R$: '))
opcao = int(input('''
1 - À vista dinheiro/cheque: 10% de desconto!
2 - À vista cartão: 5% de desconto!
3 - Em até 2X no cartão: preço normal!
4 - 3x ou mais no cartão: 20% de juros!'''))

if opcao == 1:
    novo_pagamento = pagamento - (pagamento*10/100)
elif opcao == 2:
    novo_pagamento = pagamento - (pagamento*5/100)
elif opcao == 3:
    novo_pagamento = pagamento
    parcela = pagamento/2
    print('Sua compra será parcelada em 2x de {:.2f}R$ sem juros'.format(parcela))
elif opcao == 4:
    novo_pagamento = pagamento + (pagamento*20/100)
    total_parcela = int(input('Quantas parcelas? '))
    parcela = novo_pagamento / total_parcela
    print('Sua compra será parceladas em {}x de R${:.2f} com juros'.format(total_parcela, parcela))
else:
    novo_pagamento = pagamento
    print('opção invalida')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(pagamento, novo_pagamento))
