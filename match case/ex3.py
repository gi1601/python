dia = str(input("Digite o dia"))

match dia:
    case("Segunda"|"Terça"|"Quarta"|"Quinta"|"Sexta"):
        print(f"{dia} é dia ùtil")
    case _:
        print(f"{dia} é fim de semana")