class Produto:
    def __init__(self, preco, quantidade, custo):
        self.__preco = preco
        self.quantidade = quantidade
        self.custo = custo

p1 = Produto(2,10,1)
print(p1.quantidade)