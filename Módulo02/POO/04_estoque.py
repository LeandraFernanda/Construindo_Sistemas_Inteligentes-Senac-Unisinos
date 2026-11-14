"""  Implemente uma classe Produtocom os métodos repore venderapresentada valor_em_estoquena aula.

Crie um produto de preço 5.0e estoque 4. Execute, nesta ordem:

Venda de 2unidades.
Tentativa de venda de 3unidades.
Reposição de 5unidades.
Tentativa de reposição de 0unidades.
Registre o retorno e o estoque após cada chamada. Ao final, mostre o valor em estoque.

Conferência: os estoques devem ser 2, 2, 7e 7. O valor final deve ser 35.0. 
"""
class Produto:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= 0:
            return "Quantidade inválida para venda."
        if quantidade > self.estoque:
            return "Estoque insuficiente para a venda."
        self.estoque -= quantidade
        return f"Venda de {quantidade} unidades realizada com sucesso."

    def repor(self, quantidade):
        if quantidade <= 0:
            return "Quantidade inválida para reposição."
        self.estoque += quantidade
        return f"Reposição de {quantidade} unidades realizada com sucesso."

    def valor_em_estoque(self):
        return self.preco * self.estoque    

    