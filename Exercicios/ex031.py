n = int(input('Digite os KM: '))

if n <= 200:
    f = 0.50
    print('A viagem de {}KM custou um total de {}'.format(n, (f * n)))
elif n > 200:
    f = 0.45
print('A viagem de {}KM custou um total de {}'.format(n, (f * n)))
