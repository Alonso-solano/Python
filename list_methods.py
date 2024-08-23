lista_frutas = ["manzana", "pera", "Mandarina"]

print("Estado actual de la lista", lista_frutas)

nueva_fruta = input("Ingrese una fruta: ")

lista_frutas.append(nueva_fruta)

print("Nuevo estado de la lista", lista_frutas)


# append() => Agrega datos
# insert() => Inserta un item en un indice en especifico
#Ejemplo:
print("Nuevo estado de la lista", lista_frutas)
# remove() => Remueve datos
# pop() => Remueve el ultimo item de la lista
# clear() => Limpia la lista
# sort() => Ordena la lista 
# count() => Cuenta los item de la lista

lista_frutas.clear()
print("Lista", lista_frutas)


menu = input("""Que deseas hacer? \n
             1. Sumar\n
             2. Restar\n 
             3. Multiplicar\n
             4. Dividir""")