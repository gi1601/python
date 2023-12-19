class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print('som')

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def fazer_som(self):
        print("Auau")

Meg = Cachorro("Liz")
Meg.fazer_som()
