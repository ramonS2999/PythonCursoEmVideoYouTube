def largu_altu(la, al):
    area = la * al
    area_pintada = area / 2
    print('A quantidade de lata para pintar {} metros quadrados será, {:.1f} lata'.format(area,area_pintada))

la = float(input('Digite a largura em metros:'))
al = float(input('Digite a altura em metros:'))
largu_altu(la, al)