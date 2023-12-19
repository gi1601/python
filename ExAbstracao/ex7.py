class Produto:
    def __init__(self,preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
    def calcular_total(self):
        return self.preco * self.quantidade

tot = Produto(20,5)

total = tot.calcular_total()

print(f'O valor total é R${total}')