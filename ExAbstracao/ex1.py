class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


pessoa1 = pessoa("Giovanna", 16)
pessoa2 = pessoa("Bianca", 16)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)