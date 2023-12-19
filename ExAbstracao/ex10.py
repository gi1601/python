class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        self.estoque -= quantidade

    def mostrar(self):
        print(self.estoque)

produto = Produto('notebook', 1000, 10)

produto.vender(2)

print(produto.mostrar())
