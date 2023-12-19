class Bebida:
    def __init__(self, nome, tipo):
        self.nome=nome
        self.tipo = tipo

class Refrigerante(Bebida):
    def __init__(self,nome, tipo, preco):

        super().__init__(nome, tipo)
        self.preco = preco

class Cafe(Bebida):
    def __init__(self,nome, tipo,marca):
        super().__init__(nome, tipo)
        self.marca = marca

Bebida1 = Refrigerante('Coca-Cola', "Zero", 7.99)
Bebida2 = Cafe('Café', 'Expresso', 'Café Brasil')
print(Bebida1.tipo)