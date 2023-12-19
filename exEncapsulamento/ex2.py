class Conta:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular
    def depositar(self, deposito):
        self.__saldo+= deposito
    def sacar (self, sacar):
        self.__saldo-=sacar
    def exibir(self):
        print(self.__saldo)

pessoa= Conta(100, "Giovanna")
pessoa.sacar(20)
pessoa.exibir()