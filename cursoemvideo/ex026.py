frase = str(input('DIGITE UMA FRASE: ')).upper().strip()
print('CONTEM',frase.upper().count('A'),'LETRAS "A" !')
print('A PRIMEIRA LETRA "A" APARECE NA POSIÇÃO',frase.find('A')+1)
print('A UTIMA LETRA "A" APARECE NA POSIÇÃO {}!'.format(frase.rfind('A')+1))