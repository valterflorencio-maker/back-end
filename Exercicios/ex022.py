nome = str(input('Digite seu nome')).strip()
dividido = nome.split()

print('Analisando seu nome...')
print('seu nome em maiúsculas é {}'.format(nome.upper()))
print('seu nome em minúsculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))
