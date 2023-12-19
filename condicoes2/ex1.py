um = int(input("Digite os gols do primeiro: "))
dois = int(input("Digite os gols do segundo: "))

if um == dois:
    print("Empate")
elif um < dois:
    print("O segundo time ganhou")
else:
    print("O primeiro time ganhou")