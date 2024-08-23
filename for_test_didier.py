# Crea un app que haga lo siguiente

# 1. Pida al usuario un número del 1 al 10.
# 2. Utilice un ciclo for para buscar el número ingresado en LISTA_NUMEROS.
# 3. Imprima en la pantalla si el número fue encontrado.

LISTA_NUMEROS = [2, 4,  6,  8, 10]
ENCONTRADO = False

n1 = int(input("Digite un numero del 1 al 10: "))

if n1 > 10:
    print("El numero no esta en lista")
else:
    for numero in LISTA_NUMEROS:
        print(numero)
        if n1 == numero:
            ENCONTRADO = True
            break

    if ENCONTRADO:
        print("El numero si esta en la lista")
    else: 
        print("El numero no esta en la lista")