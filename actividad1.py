"""
Actividad Práctica
1. Escriba un algoritmo para calcular la factorial de un número. 
    Recuerda que la factorial de un número n es el producto de todos 
    los números enteros positivos desde 1 hasta n.
2. Escriba un algoritmo para determinar si una palabra es un palíndromo. 
    Un palíndromo es una palabra que se lee igual al revés que al derecho.
3. Implementa un algoritmo que ordene una lista de números de menor a mayor. 
    Puedes usar cualquier algoritmo de ordenación que prefieras."""


# numero 1

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Ejemplo de uso:
numero_str = input("Ingrese un numero positivo: ")
numero = int(numero_str)
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

# numero 2

def es_palindromo(palabra):
    palabra = palabra.lower()    
    # Eliminar espacios en blanco de la palabra
    palabra = palabra.replace(" ", "")
    
    # Comparar la palabra original con su versión invertida
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# Ejemplo de uso:
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")


# numero 3

def ordenar_lista(lista):
    n = len(lista)
    
    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            # Intercambiamos si el elemento encontrado es mayor que el siguiente elemento
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ejemplo de uso:
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)
ordenar_lista(numeros)
print("Lista ordenada:", numeros)
