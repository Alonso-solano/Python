CANTIDAD_FRUTAS = ['mango', 'melon', 'sandia', 'pera', 'uva']
ENCONTRADO = False

fruta_ingresada = input("diga una fruta ")

for frutas in CANTIDAD_FRUTAS:

    if fruta_ingresada == CANTIDAD_FRUTAS:

        print("La fruta si esta en la lista")
    else:
        print("la fruta no esta en la lista ")
