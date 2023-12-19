from conversorDeUnidades import conversor
tem = int(input("1-Converter de celsius para fahrenheit\n2-Converter de fahrenheit para celsius\nR:"))
num = int(input("Grau que será convertido:"))

if tem == 1:
    cf = conversor.celsius_para_fahrenheit(num)
    print(f"{cf}°F")
elif tem == 1:
    fc = conversor.fahrenheit_para_celsius(num)
    print(f"{fc}°C")
else:
    print("ERRO")