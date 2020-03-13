import random
def escolha01():
    n1 = input('Informe aluno:')
    n2 = input('Informe aluno:')
    n3 = input('Informe aluno:')
    n4 = input('Informe aluno:')
    lista = [n1, n2, n3, n4]
    random.shuffle(lista)
    print('A orden escolhida é\n',lista)

def escolha02():
    lista = ['Rayanne', 'Ramon', 'Lorena', 'Ermeson']
    random.shuffle(lista)
    print(' ')
    print('A ordem escolhida é\n',lista)

escolha01()
escolha02()