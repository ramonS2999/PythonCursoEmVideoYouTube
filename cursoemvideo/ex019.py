import random
def sorteio_aluno():
    x = ['Rayanne','Ramon','Lorena','Ermeson']
    aluno = random.randint(0,len(x)-1)
    print('Os alunos para serem sorteados são...\n',x)
    print(' ')
    print('O aluno escolhido é', x[aluno])

def choice():
    n1 = input('Digite um nome:')
    n2 = input('Digite um nome:')
    n3 = input('Digite um nome:')
    n4 = input('Digite um nome:')
    lista = [n1, n2, n3, n4]
    escolha = random.choice(lista)
    print('O aluno escolhido foi',escolha)

sorteio_aluno()
choice()