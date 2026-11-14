""" Utilize uma classe Produtoe uma lista com três instâncias. Percorra a lista para mostrar nome, estoque e valor em estoque de cada uma.

Mostre também:

o valor total em estoque;
a quantidade de produtos cujo estoque é zero.
Teste com Produto("Caderno", 10.0, 2), Produto("Caneta", 3.0, 0)e Produto("Borracha", 2.0, 5).

Resultado esperado: total 30.0e um produto sem estoque. Repita com uma lista vazia: o total e a contagem devem ser zero. 
"""
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def valor_em_estoque(self):
        return self.preco * self.estoque
print("Relatório de Produtos:")
print("---------------------")
produtos = [    
    Produto("Caderno", 10.0, 2),
    Produto("Caneta", 3.0, 0), 
    Produto("Borracha", 2.0, 5)
]
   