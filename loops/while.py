# Es un ciclo, que permite ejecutar un proque de código mientras la condición inicial sea verdadera

usuario_activo = True


while usuario_activo:
    option = int(input("""
          Menú
            1. Imprimir 'Hola'
            2. Imprimir 'Como estás?'
            3. Cerrar sistema
          : """))
    
    if option == 1:
        print('Hola')
    elif option == 2:
        print('Como estás?')
    elif option == 3:
        usuario_activo = False
        print('Cerrando sistema ...')
    else:
        print('Opción no valida')

