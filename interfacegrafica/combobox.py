import customtkinter as tk
from modulo import*

janela = CriarJanelaP("JanelaPrincipal","400x400", 1)

Lista = ["Item 1", "Item 2", "Item 3", "Item 4"]
combo =CriarComboBox(janela, Lista, 200, 30, 6,7)

janela.mainloop()