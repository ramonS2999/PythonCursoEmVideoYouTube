def mul(n):
    i = 1
    print('---------------')
    while i <= 9:
        print(n,'x', i,' = ',n*i)
        i += 1
    print(n,'x', 10,'= ',n*10)
    print('---------------')

def soma(n):
    i = 1
    print('---------------')
    while i <= 9:
        print(n,'+',i,' = ',n+i)
        i += 1
    print(n,'+',10,'= ',n*10)
    print('---------------')

def sub(n):
    i = 1
    print('---------------')
    while i <= 9:
        print(n,'-',i,' = ',n-(i))
        i += 1
    print(n,'-',10,'= ',n*10)
    print('---------------')

def div(n):
    i = 1
    print('---------------')
    while i <= 9:
        print(n,'/',i,' = ',n/i)
        i += 1
    print(n,'/',10,'=',n*10)
    print('---------------')

def reset(n,si):
    if si == 1:
        mul(n)
    elif si == 2:
        soma(n)
    elif si == 3:
        sub(n)
    elif si == 4:
        div(n)
    else:
        print('Valor invalido!')

n = int(input('Digite um valor para tabuada: '))
si = int(input('Digite:\n1 para multiplicar\n2 para soma\n3 para subtrair\n4 para dividir\n'))
reset(n,si)