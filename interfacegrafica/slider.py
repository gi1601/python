import customtkinter as tk
from modulo import*

janela= CriarJanelaP("JanelaPrincipal","400x400", 1)

slider = tk.CTkSlider(janela, width=200, height=10)
slider.grid(row= 12, column= 6)
slider.get()

janela.mainloop()