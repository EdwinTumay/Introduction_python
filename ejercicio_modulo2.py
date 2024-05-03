#ejercicio 1 Saludo
def saludar (nombre):
    return f"¡Hola, {nombre}!"

# Ejemplo de uso:
saludo_personalizado = saludar('Alice')
print(saludo_personalizado)
    
#ejercicio 2 carculadora de area de circulo
import math 

def area_circulo(radio):
    return math.pi * radio**2

#ejemplo
radio = 6
print(f"El area del cirulo con radio {radio} es: {area_circulo(radio)}")


# ejercicio 3 conversor de temperatura
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplo de uso:
temp_celsius = 30
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius} grados Celsius son equivalentes a {temp_fahrenheit} grados Fahrenheit.")

temp_fahrenheit = 86
temp_celsius = fahrenheit_a_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit} grados Fahrenheit son equivalentes a {temp_celsius} grados Celsius.")

# Ejercicio 4 Factorial

def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Ejemplo de uso:
numero = 5
print(f"El factorial de {numero} es {factorial(numero)}.")

# Ejercicio 6
def saludo(nombre):
    print(f"Hola, {nombre}!")

saludo("Alice")
