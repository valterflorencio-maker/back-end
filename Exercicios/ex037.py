number1 = int(input('escolha um numero: '))
choice = str(input('escolha entre bin oct e hex: '))
if choice == 'bin':
    print(bin(number1))
elif choice == 'oct':
    print(oct(number1))
elif choice == 'hex':
    print(hex(number1))
else:
    print('Padrao nao reconhecido digite exatamento como foi mostrado')
