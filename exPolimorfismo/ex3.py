class Calculo:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calcular_valor(self):
        pass

class soma(Calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)

    def calcular_valor(self):
        print(self.num1 + self.num2)

class subtração(Calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)

    def calcular_valor(self):
        print(self.num1 - self.num2)

class multiplicação(Calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)

    def calcular_valor(self):
        print(self.num1 * self.num2)

class divisão(Calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)

    def calcular_valor(self):
       print(self.num1 / self.num2)

num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo número: "))
somas = [soma(num1,num2), subtração(num1,num2), multiplicação(num1,num2), divisão(num1,num2)]
for i in range(len(somas)):
    somas[i].calcular_valor()