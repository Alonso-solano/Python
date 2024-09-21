frutas = ['manzana', 'pera', 'limon']

def lista_frutas():
    for fruta in frutas:
        print(fruta.upper())

# list comprenhension

# TODO: ponga el codigo en una funcion y que retorne la lista nueva
def lista():
    nueva_lista = [fruta.upper() 
               for fruta in frutas 
               if fruta != 'pera']
    return nueva_lista


algo = lista()
print(algo)

# dictionary comprenhensions


# upper(), lower()
# uppercase - Mayusculas
# lowercase - minusculas