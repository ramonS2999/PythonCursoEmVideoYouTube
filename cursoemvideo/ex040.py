nota1 = int(input('informe a primeira nota do aluno: '))
nota2 = int(input('informe a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if 10 >= media >= 0:
    if media < 5:
        print('O aluno está reprovado!\nmedia {:.1f}'.format(media))
    elif media < 7:
        print('O aluno está de recuperação!\nmedia {:.1f}'.format(media))
    else:
        print('O aluno está aprovado!\nmedia {:.1f}'.format(media))
else:
    print('Valor invaido!')
