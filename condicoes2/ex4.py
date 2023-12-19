valor1 = float(input("Digite o valor: "))
valor2 = float(input("Digite o valor: "))

escolha = str(input("Escolha a operação: soma, subtração, multiplicação ou divisão: "))
adicao = valor1+valor2
subtracao = valor1-valor2
multiplicacao = valor1*valor2
divisao = valor1/valor2

if escolha == "soma" or escolha =="SOMA":
    print(f"{adicao}")
elif escolha == "subtração" or escolha == "SUBTRAÇÃO":
    print(f"{subtracao}")
elif escolha == "multiplicação" or escolha == "MULTIPLICAÇÃO":
    print(f"{multiplicacao:.2f}")
elif escolha == "divisão" or escolha == "DIVISÃO":
    print(f"{divisao:.2f}")