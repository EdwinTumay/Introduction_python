"""En este ejemplo, hemos creado una clase "Producto" con atributos "nombre" y "precio". 
El método "mostrar_informacion" muestra la información del producto en la pantalla. Luego, 
hemos creado dos objetos "producto1" y "producto2" basados en la clase "Producto" y hemos 
asignado valores a los atributos correspondientes. Finalmente, hemos invocado el método
"mostrar_informacion" en cada objeto para mostrar la información del producto en la pantalla."""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")

producto1 = Producto("Camiseta", 25.99)
producto2 = Producto("Pantalón", 39.99)
producto1.mostrar_informacion()
producto2.mostrar_informacion()

