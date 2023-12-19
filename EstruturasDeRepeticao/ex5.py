homem = ""
idadeH= 0
mulheres= 0

for pessoa in range(1, 8):
    print(f" Pessoa {pessoa} ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")

    if sexo.upper() == "M" and idade > idadeH:
        homem= nome
        idadeH= idade

    if sexo.upper() == "F" and idade < 20:
        mulheres+= 1

print(f"\nO homem mais velho é: {homem}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres}")