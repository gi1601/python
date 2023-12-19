# Aluna: Giovanna Rodrigues Silva - Questão: "Bazinga!"
sheldon = str(input("Informe a escolha de Sheldon: "))
raj = str(input("Informe a escolha de Raj: "))

#todas as possibilidades de sheldon ganhar
if sheldon == "papel" and raj == "pedra":
    print("Bazinga!")
elif sheldon == "pedra" and raj == "lagarto":
    print("Bazinga!")
elif sheldon == "lagarto" and raj == "spock":
    print("Bazinga!")
elif sheldon == "spock" and raj == "tesoura":
    print("Bazinga!")
elif sheldon == "tesoura" and raj == "lagarto":
    print("Bazinga!")
elif sheldon == "lagarto" and raj == "papel":
    print("Bazinga!")
elif sheldon == "papel" and raj == "spock":
    print("Bazinga!")
elif sheldon == "spock" and raj == "pedra":
    print("Bazinga! ")
elif sheldon == "pedra" and raj == "tesoura":
    print("Bazinga!")

#todas as possibilidades de raj ganhar
elif sheldon == "papel" and raj == "tesoura":
    print("Raj trapaceou!")
elif sheldon == "pedra" and raj == "papel":
    print("Raj trapaceou!")
elif sheldon == "lagarto" and raj == "pedra":
    print("Raj trapaceou!")
elif sheldon == "spock" and raj == "lagarto":
    print("Raj trapaceou!")
elif sheldon == "tesoura" and raj == "spock":
    print("Raj trapaceou!")
elif sheldon == "lagarto" and raj == "tesoura":
    print("Raj trapaceou!")
elif sheldon == "papel" and raj == "lagarto":
    print("Raj trapaceou!")
elif sheldon == "spock" and raj == "papel":
    print("Raj trapaceou!")
elif sheldon == "pedra" and raj == "spock":
    print("Raj trapaceou!")
elif sheldon == "tesoura" and raj == "pedra":
    print("Raj trapaceou!")

#todas as possibilidades de dar empate
elif sheldon == "papel" and raj == "papel":
    print("De novo!")
elif sheldon == "pedra" and raj == "pedra":
    print("De novo!")
elif sheldon == "tesoura" and raj == "tesoura":
    print("De novo!")
elif sheldon == "lagarto" and raj == "lagarto":
    print(" De novo!")
elif sheldon == "spock" and raj == "spock":
    print("De novo!")