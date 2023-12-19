class Carro:
    def __init__(self, marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano= ano
tesla = Carro('Tesla', 'esportiva', 2008)
print("O nome do Carro é:", tesla.marca)
print("O modelo é:",tesla.modelo)
print("O ano é: ", tesla.ano)