import customtkinter as tk
from modulo import*

janela= CriarJanelaP("Principal", "400x400", 1)

switch = CriarSwitch(janela, "lala", 6, 7)

janela.mainloop()