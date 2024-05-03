"""1. Crea un módulo `calculadora.py` con funciones para las operaciones básicas: 
suma, resta, multiplicación y división.
2. Crea un módulo `principal.py` que importe tu módulo `calculadora.py` y 
utilice sus funciones para realizar algunas operaciones."""

import operaciones_basicas

print(operaciones_basicas.suma(1000,250))
print(operaciones_basicas.resta(1000,250))
print(operaciones_basicas.multiplicar(1000,250))
print(operaciones_basicas.division(1000,250))


class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

p1 = Persona("Juan", 30)
p1.saludo() # Imprime: "Hola, mi nombre es Juan y tengo 30 años."