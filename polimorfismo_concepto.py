""" En este ejemplo, tanto la clase "Perro" como la clase "Gato" sobrescriben el método 
"saludar" de la clase padre "Animal". Cada clase hija proporciona su propia implementación 
del método, lo que permite que los objetos de ambas clases se comporten de manera polimórfica."""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("¡Hola! Soy un animal.")

class Perro(Animal):
    def saludar(self):
        print("¡Guau! Soy un perro.")

class Gato(Animal):
    def saludar(self):
        print("¡Miau! Soy un gato.")
animal1 = Perro("Fido")
animal2 = Gato("Tom")
animal1.saludar() # Imprime "¡Guau! Soy un perro."
animal2.saludar() # Imprime "¡Miau! Soy un gato."