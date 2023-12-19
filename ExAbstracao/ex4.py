class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

ret = Retangulo(5,9)

area = ret.calcular_area()

print(area)