try:
    # Pedir la masa en kilogramos
    masa = float(input("Ingrese la masa en kilogramos: "))
    # Verificar que la masa no sea negativa
    if masa < 0:
        print("La masa no puede ser negativa. Por favor, ingrese un valor válido.")
    else:
        # Calcular la ecuación E=mc^2
        c = 3000000  # Velocidad de la luz en m/s
        energia = masa * c ** 2
        print("La energía es igual a:", energia, "joules")
except ValueError:
    print("Error: Por favor, ingrese un valor numérico válido para la masa.")
