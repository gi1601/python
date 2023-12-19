class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def exibir(self):
        print(self.modelo, self.marca)

    def alterar_modelo(self):
        mudar = input()
        self.modelo = mudar
        print(self.modelo)


car = Carro("Chevrolet", "carro")
car.alterar_modelo()