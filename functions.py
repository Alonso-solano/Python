# Funciones

#print()
#input()

def validar_mensaje(mensaje, edad, domicilio): # -> la funcion se define
    """
    Esta funcion valida que el mensaje no sea vacio
    """
    if mensaje == "":
        print("No se pueden imprimer mensajes vacios")
    elif edad <=0:
        print("Esta edad no es valida")
    elif domicilio == "":
        print("Se necesita un domicilio valido")
    else:
        print("Mensaje: ", mensaje)
        print("Edad: ", edad)
        print("Domicilio: ", domicilio)




validar_mensaje("Hola", 24, "Orotina") # La funcion se llama

# Parametros vs argumentos
# Los parametros es lo que se define cuando se crea la funcion, y los argumentos son los que se envian cuando se llama la funcion.
    