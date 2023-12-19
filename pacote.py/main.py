from pacotes import OpMat
raiz=OpMat.raiz_quadrada(3249)
print(raiz)

#ou#

from pacotes.OpMat import *
raiz = raiz_quadrada(3249)
print(raiz)

#testes#

from pacotes.texto import *
from pacotes.data import *
from pacotes.desenho import *
from pacotes.emoji import *


capitalizar = capitalizar_palavras("Oi, tudo bem")
print(capitalizar)



cavalo = desenhar_cavalo()
print(cavalo)

riso = emoji_riso()
print(riso)