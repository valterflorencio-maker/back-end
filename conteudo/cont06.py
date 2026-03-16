# OPERADORES – Exemplo de alinhamento de saída com format()

# Podemos escrever um resultado em uma quantidade específica de caracteres
# ao colocar o valor dentro da "máscara" {:20} após escrever a string
# Aqui usamos input para pedir o nome do usuário

# Solicita ao usuário que digite o nome
nome = input('Qual é o seu nome? ')  # Ex: Gustavo

# Imprime a mensagem com o nome do usuário, alinhando em 20 caracteres
# {:20} garante que o espaço reservado para o nome tenha 20 caracteres
print('Prazer em conhece-lo {:20}!'.format(nome))

# Exemplo de saída se o usuário digitar "Gustavo":
# Qual é o seu nome? Gustavo
# Prazer em conhece-lo Gustavo       !
# O espaço adicional após "Gustavo" completa os 20 caracteres reservados
