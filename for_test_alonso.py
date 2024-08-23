# Crea un app que haga lo siguiente

# 1. Pida al usuario un número del 1 al 10.
# 2. Utilice un ciclo for para buscar el número ingresado en LISTA_NUMEROS.
# 3. Imprima en la pantalla si el número fue encontrado.

LISTA_NUMEROS = [2, 4,  6,  8, 10]


n1 = int(input("Digite un numero del 1 al 10: "))

for numero in LISTA_NUMEROS:
    if n1 == numero:
        print("El numero si esta en la lista")
    else: 
        print("El numero no esta en la lista")