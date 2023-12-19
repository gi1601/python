class Carro:
    def __init__(self,nome,cor,marca):
     self.nome=nome
     self.cor=cor
     self.marca=marca
def Ligar(self):
        print("ligando o ", self.nome)

class Carro2:
    def __init__(self,ano):
        self.ano=ano
    def Farol(self):
        print("Acendendo as luzes")
    def Acelerar(self):
        print("Acelerando...")

class CarroCitroen(Carro):
    def __init__(self,nome,cor,portas):
        super().__init__(nome,cor,"Citroen")
        self.portas=portas

class CarroCitroen(Carro, Carro2):
    def __init__(self, nome,cor,portas,ano):
        Carro.__init__(self,nome,cor,"Citroen")
        Carro2.__init__(self,ano)
        self.portas=portas

Car=CarroCitroen("Cactus", "Azul", 2, 2022)
print(Car.ano)