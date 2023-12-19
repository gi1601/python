clientes = int(input("Quantos clientes: "))
soma = 0
for n in range (1,clientes+1):
    temperatura = float(input('Digite a temperatura'))
    soma+= temperatura
    if temperatura <=37.2:
        print('Temperatura está normal')
    elif temperatura>=37.3 and temperatura<38:
        print("Estado febril")
    elif temperatura>=38 and temperatura <=39:
        print("Com febre")
    elif temperatura >39:
        print("Febre alta")
media = soma/clientes
print(" A media das temperaturas é: ", media, "e a quantidade de clientes é", clientes)