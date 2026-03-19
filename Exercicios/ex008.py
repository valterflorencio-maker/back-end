n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
if n1 > 10 or n2 > 10:
    print('erro numero invalido')
else:
    print('A 1\u00ba nota: {} 2\u00ba nota {} e a Media {}'.format(n1, n2, (n1 + n2)/ 2))
