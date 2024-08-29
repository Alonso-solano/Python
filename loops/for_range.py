def ciclo_for(numero1):
    for numero in range(0, 10000, 5):
        if (numero == numero1):
            print("Numero", numero, "encontrado")

numero_ingresado = int(input("Ingrese un número: "))

ciclo_for(numero_ingresado)

# Palabras reservadas

# Funciones

# 1. Las funciones tienes 2 estados, cuando se crean y cuando se llaman / invocan.
# 2. Si la funciones fue creada pero no invocada, nunca se va a ejecutar