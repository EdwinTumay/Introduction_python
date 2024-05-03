# Programa principal
from geometria import calcular_area_rectangulo, calcular_area_circulo
base_rectangulo = 5
altura_rectangulo = 3
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_rectangulo)

radio_circulo = 2
area_circulo = calcular_area_circulo(radio_circulo)
print("El área del círculo es:", area_circulo)