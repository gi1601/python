class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self,valor):
        self.saldo+=valor

    def sacar(self, valor):
        self.saldo-=valor

    def exSaldo(self):
        print(self.saldo)

Bianca = ContaBancaria("Bianca", 1000, 2032)
Bianca.depositar(200)
Bianca.sacar(100)
Bianca.exSaldo()

