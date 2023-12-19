class Restaurante:
    def __init__(self, nome,tipo,gastoMensal):
        self.nome= nome
        self.tipo= tipo
        self.__gastoMensal = gastoMensal

    def atualizarRestaurante(self,tipo2):
        self.tipo=tipo2

p1 = Restaurante("Primus","pizzaria", 1980.00)
p1.atualizarRestaurante("Lanchonete")
print("Antigo: ",p1.nome,"Novo:", p1.tipo)