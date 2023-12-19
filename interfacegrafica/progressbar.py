import customtkinter as tk
from modulo import*

janela= CriarJanelaP("JanelaPrincipal","400x400", 1)

progress= tk.CTkProgressBar(janela, width=200, height=10)
progress.grid(row=7, column=6)
progress.set(0)
progress.set(1)
progress.set(0.2)

janela.mainloop()