
# Comentarios!
print("Hola mundo")

# pdf 1
# variables
nombre = "Edwin"
edad = 28

# imprimiendo variables
print(f'Hola mi nombres es {nombre} y tengo {edad} años')

# operadores aritmeticos
a = 25
b = 5
resultado = a + b
print(resultado)

# División entera: //   
c = 10
d = 3
resultado = c//d
print(resultado)

# Módulo: % módulo devuelve el resto de la división entre dos números.
resultado = c%d
print(resultado)


# contador
contador = 0
contador += 1
print(contador)

# Igualdad: se utiliza el operador "==". 
a = 5
b = 5
resultado = a == b
print(resultado) # Imprime True

# Desigualdad: se utiliza el operador "!=".
a = 5
b = 3
resultado = a != b
print(resultado) # Imprime True

# Mayor que: se utiliza el operador ">".
a = 5
b = 3
resultado = a > b
print(resultado) # Imprime True

# Menor que: se utiliza el operador "<".
a = 5
b = 3
resultado = a < b
print(resultado) # Imprime False

# Mayor o igual que y menor o igual que: se utilizan los operadores ">=" y "<=".
a = 5
b = 5
resultado = a >= b
print(resultado) # Imprime True

c = 3
d = 5
resultado = c <= d
print(resultado) # Imprime True

# pdf2

# if condicion:

numero = 10
if numero > 0:
    print("El número es positivo")

# else
numero = -5
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo o cero")

#else if
numero = 0
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# while condicion:

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# for variable in secuencia:

frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

for i in range(1, 6):
    print(i)


# pdf3

""" Ejercicio 1 
1. Leer la base del triángulo desde el usuario.
2. Leer la altura del triángulo desde el usuario.
3. Calcular el área del triángulo utilizando la fórmula: área = (base * altura) / 2.
4. Mostrar el resultado del cálculo del área en la pantalla. """

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)

""" Ejercicio 2
Problema:
Dado un número entero positivo, determinar si es primo o no.
Algoritmo:
Leer el número desde el usuario.
Inicializar una variable booleana es_primo como verdadera.
Verificar si el número es menor o igual a 1. En ese caso, asignar es_primo como falso.
Iterar desde 2 hasta la mitad del número (redondeando hacia arriba).
Si el número es divisible entre cualquier valor en ese rango, asignar es_primo como falso y salir del bucle.
Si es_primo es verdadera, imprimir "El número es primo".
De lo contrario, imprimir "El número no es primo".
"""
numero = int(input("Ingrese un número entero positivo: "))
es_primo = True
if numero <= 1:
    es_primo = False
else:
    for i in range(2, (numero // 2) + 1):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")



# probando 2 

def procedimiento ():
    print("esto es un procedimiento")

valor = procedimiento() #valor sera none