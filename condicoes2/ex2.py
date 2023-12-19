valor = float(input("Digite o valor: "))
numero = float(input("Digite a quantidade de prestações: "))

prestacao = valor/numero

if prestacao > 500:
    print("Usuário não consegue pagar")
else:
    print("Usuário consegue pagar")