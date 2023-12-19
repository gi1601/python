import customtkinter as tk
from modulo import*

janela= CriarJanelaP("JanelaPrincipal","400x400", 1)
check= CriarCheckBox(janela, "lala", 6, 8)
btn= CriarBotao(janela, "Clique", clique, 100, 300, 8, 7)

tk.set_appearance_mode("Light")

def clique():
    if check.get() ==1:
        label1.configure(text="Marcado")
    else:
        label1.configure(text="Desmarcado")








janela.mainloop()