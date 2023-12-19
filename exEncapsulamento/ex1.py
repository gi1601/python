class Cliente:
    def __init__(self, codigo):
        self.__codigo = codigo
    def MostrarCodigo(self):
            print(self.__codigo)
pessoa = Cliente(263.453)
pessoa.MostrarCodigo()