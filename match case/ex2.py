cor = str(input("Digite uma cor"))

match cor:
    case("vermelho"):
        print("É vermelho")
    case("azul"):
        print("azul")
    case("verde"):
        print("É verde")
    case _:
        print("Cor desconhecida")
