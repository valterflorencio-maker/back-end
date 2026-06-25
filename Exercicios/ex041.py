produto = float(input('Digite o valor do produto: '))
opcao = int(input('Formas de pagamento, 1.dinheiro/cheque, 2.avista, 3.credito 2x, 4.credito 3x: '))
desconto = produto
juros = produto
if opcao == 1:
    produto = produto - (desconto * 0.10)
elif opcao == 2:
   produto = produto - (desconto * 0.05)
elif opcao == 3:
    produto = 0 
elif opcao == 4:
    produto = produto + (juros * 0.20)
else:
    print('opcao incorreta')

print(f'valor final {produto}')
