class pessoa:
    def __init__(self,nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


mostrar_detalhes = pessoa('Agatha' ,17, 'Feminino')
print("O nome da pessoa é: ",mostrar_detalhes.nome)
print("A idade é: ", mostrar_detalhes.idade)
print("O sexo é: ", mostrar_detalhes.sexo)