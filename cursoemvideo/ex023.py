def ramon():
    num = int(input('Dgite um número: '))
    n = str(num)
    print('unidade: {}\ndesena:  {}\ncentena: {}\nmilhar:  {}'.format(n[0], n[1], n[2], n[3]))

def fatiar_num(n):
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10
    print('unidade: {}\ndesena:  {}\ncentena: {}\nmilhar:  {}'.format(u, d, c, m))

n = int(input('Digite um numero com 4 algaismos: '))
fatiar_num(n)
#ramon()