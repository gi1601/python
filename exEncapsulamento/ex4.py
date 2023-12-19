class livros:
    def __init__(self, titulo, autor,ano, preco):
        self.titulo= titulo
        self.autor= autor
        self.ano = ano
        self.__preco = preco
    def atualizarAno(self,atual):
        self.ano=atual

p1 = livros("Textos para tocar cicatrizes","Igor Pires",2020, 50.00)
p1.atualizarAno(2022)
print(p1.ano)