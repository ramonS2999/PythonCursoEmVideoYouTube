def cent_milin(n):
    c = 100 * n
    m = 1000 * n
    print(' ')
    print('%d metros é %d centimetros e %d milimetros!'%(n,c,m))

n = int(input('Iforme o metro: '))
cent_milin(n)