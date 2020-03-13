dia = int(input('Informe o dia de nascimento: '))
mes = int(input('Informe o mês de nascimento: '))
ano = int(input('Informe o ano de nascimento: '))
if (dia < 32 and dia > 0) and (mes < 13 and mes > 0) and (ano > 1975 and ano < 2018):
    print('Você nasceo na data {}/{}/{}.'.format(dia,mes,ano))
else:
    print('Valor invalido!')