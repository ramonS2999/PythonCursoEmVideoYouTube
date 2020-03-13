def santos():
    cid = str(input('COMO SUA CIDADE SE CHAMA? ')).strip()
    if (cid[:5].upper() == 'SANTOS'):
        print('sim ela tem SANTOS no nome!')
    else:
        print('Ela não tem SANTOS no nome!')

cidade = input('QUAL É SUA CIDADE? ')
san = ['santos']
print(san[0] in cidade.lower())
if (san[0] in cidade.lower()) == True:
    print('VERDADE, SUA CIDADE TEM',cidade)
else:
    print('Ela não tem SANTOS...\n')
santos()