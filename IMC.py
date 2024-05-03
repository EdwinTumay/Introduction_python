peso = float(input("Por favor, introduzca su peso en Kilogramos: "))
altura = float(input("Por favor, introduzca su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    resultado = "Bajo De peso"
elif imc < 25:
    resultado = "Normal"
else:
    resultado = "Sobrepeso"

print(f"Su IMC es {imc:.1f}. Usted tiene {resultado}.")