# Crie uma variável chamada informacao. Ela deverá receber, nesta ordem:

# o texto "42";
# o número inteiro 42;
# o número decimal 42.0;
# o valor booleano False.
# Após cada atribuição, mostre o valor e o resultado de type(informacao).

# Escreva um comentário explicando a diferença entre "42" e 42. Ao final, explique se a variável guarda os quatro valores ao mesmo tempo ou apenas o último valor atribuído.  


informacao = "42"
print(informacao, type(informacao))  # Mostra o valor e o tipo
informacao = 42
print(informacao, type(informacao))  # Mostra o valor e o tipo
informacao = 42.0
print(informacao, type(informacao))  # Mostra o valor e o tipo
informacao = False
print(informacao, type(informacao))  # Mostra o valor e o tipo

# A diferença entre "42" e 42 é que "42" é uma string (texto) e 42 é um número inteiro.
# A variável guarda apenas o último valor atribuído.    
