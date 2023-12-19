class Empregado:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario = salario

class Gerente(Empregado):
    def __init__(self,nome,salario, setor):

        super().__init__(nome,salario)
        self.setor = setor

g1 = Gerente('Giovanna', 1500, "gerente")
print(g1.nome,g1.salario)