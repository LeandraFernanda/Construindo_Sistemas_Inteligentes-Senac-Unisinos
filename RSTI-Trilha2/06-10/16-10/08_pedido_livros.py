'''
A biblioteca tem 8 exemplares disponíveis . Leia a quantidade que 
o usuário deseja retirar e informe se a retirada é possível ou não.
Se a quantidade for menos ou igual a zero
Se for maior que o estoque , informe que não há exemplares suficientes
Caso contrário , confirme o pedido , aualize o estoque e mostre a quantidade
restante.
O estoque só deve diminuir quando o pedido for confirmado.
'''

estoque = 8
quantidade = int(input("Quantos exemplares deseja retirar? "))

if quantidade <= 0:
    print("Quantidade inválida.")
elif quantidade > estoque:
    print("Não há exemplares suficientes.")
else:
    estoque -= quantidade
    print(f"Pedido confirmado. Quantidade restante: {estoque}")

print("Fim do programa.") 

