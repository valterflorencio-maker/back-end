n1 = float(input('digite a altura em metros: '))
n2 = float(input('digite a largura em metros: '))
area = n1 * n2
print('A altura {:.2f} A largura {:.2f} e a area {:.2f}'.format(n1, n2, area))
print('voce precisa de {:.2f} litros de tinta para pintar a parede'.format(area / 2))
