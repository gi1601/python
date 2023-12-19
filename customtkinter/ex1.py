import customtkinter as tk



tk.set_appearance_mode("Dark")

janela = tk.CTk()
janela.title("Janela 1")
janela.geometry("400x350")

janela.configure(fg_color="blue")
janela.resizable(width=False, height=False)
colunas = list(range(13))
linhas =  list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas, weight=1)


texto1 = tk.CTkLabel(janela, text="Digite..")
texto1.grid(row= 6, column= 6)


caixa1= tk.CTkEntry(janela, placeholder_text="Digite o primero número", width=200, height=30)
caixa1.grid(row= 7, column=6)
caixa2= tk.CTkEntry(janela, placeholder_text="Digite o segundo número", width=200, height=30)
caixa2.grid(row= 8, column=6)

def num():
    num1 = int(caixa1.get())
    num2 = int(caixa2.get())

    if num1>num2:
        texto1.configure(text="O primeiro número é maior")
    elif num1<num2:
        texto1.configure(text="Segundo número é maior +")
    else:
        texto1.configure(text="Os dois são iguais")

btn1= tk.CTkButton(janela, text="Clique aqui", command= num, width=100, height=30)
btn1.grid(row= 10, column=6)

janela.mainloop()

