class AnimalAquatico:
    def nadando(self):
        pass

class Peixe (AnimalAquatico):
    def nadando(self):
        print("O peixe está nadando")

class Tartaruga (AnimalAquatico):
    def nadando(self):
        print("A tartaruga está nadando")

Animal1 = Peixe()
Animal1.nadando()

Animal2 = Tartaruga()
Animal2.nadando()