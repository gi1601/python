class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        mediaNota = (self.nota1 + self.nota2) / 2
        print(f'{self.nome} teve a média de {mediaNota}')

resp = aluno('Anaju', 10, 10)
resp.media()