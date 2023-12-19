# Aluna: Giovanna Rodrigues Silva - Questão: "Conversão de tempo"

segundos = float(input("Informe o tempo em segundos: "))

#cada minuto tem 60 segundos e cada hora tem 60 minutos, portanto para descobrir os segundo de uma hora multiplicar 60*60= 3600 segundos em 1 hora
horas= segundos / 3600
resto= segundos % 3600
#o que sobrar da divisão das horas eu divido por 60 , para descobrir os minutos
minutos = resto / 60
#para os segundos eu pego os restos do minuto/60
seg = resto % 60

print(f"{horas:.0f}:{minutos:.0f}:{seg:.0f}")
#quando o numero da por exemplo, 38.9, ele arredonda para 39 ao inves de deixar só 38