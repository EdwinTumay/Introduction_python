"""En este ejemplo, la clase "Animal" es la clase padre y la clase "Perro" 
es la clase hija que hereda de "Animal". El perro hereda el atributo "nombre" 
y el método "saludar" de la clase padre, y además tiene su propio método "ladrar"."""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("¡Hola! Soy un animal.")
class Perro(Animal):
    def ladrar(self):
        print("¡Guau!")
perro = Perro("Fido") 
print(perro.nombre) # Imprime "Fido" perro.saludar() # Imprime "¡Hola! Soy un animal."
perro.ladrar() # Imprime "¡Guau!"