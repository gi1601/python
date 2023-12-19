class Lampada:
    def __init__(self, nome, on):
        self.nome = nome
        self.estado = on

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def exibir(self):
        if self.estado:
            print('A lâmpada está acesa!')
        else:
            print('A lâmpada está apagada!')