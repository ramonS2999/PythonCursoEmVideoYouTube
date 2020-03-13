def km_pagamento(kmp, qdias):
    prco = 60 * qdias
    kmr = 0.15 * kmp
    valor_t = prco + kmr
    print(valor_t)

kmp = float(input('Informe a quantidade de km percorrido:'))
qdias = int(input('Informe a quantidade de dias de alugueo: '))
km_pagamento(kmp, qdias)