login =str(input("Digite seu login"))
senha =str(input("Digite seua senha"))
match(login,senha):
    case("admin", "admin_pass"):
        print(f"{login} logado com sucesso")
    case ("user", "user_pass"):
        print(f"{login} logado com sucesso")
    case ("guest", _):
        print(f"{login} logado com sucesso")
    case _:
        print(("ERRO- login ou senha incorreto"))