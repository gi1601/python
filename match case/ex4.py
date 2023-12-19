animal = str(input("Digite um animal da fazendinha"))

match animal:
    case("vaca"|"galinha"|"ovelha"):
        print(f"O animal é {animal}")
    case _:
        print("Animal desconhecido")