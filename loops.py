# Ciclo for

fruitas_listas = ['manzana', 'pera', 'sandia', 'naranja']
lista_alumnos = ['Didier', 'Alonso', 'Juan']
fruitas_tuplas= ('manzana', 'pera', 'sandia')

# diccionarios,
# strings

# inmutabilidad

for fruta in fruitas_tuplas:
    print(f'Hola: {fruta}')

# diccionarios

alumnos = {
    'nombre': "Alonso", 
    "apellido": "Solano",
    "telefono": "8592-2222",
    "edad": 24
    } # llave y valor, key-value pair

# TODO: Aprender
# dict.keys() = muestra las llaves
# dict.values() = muestra los valores
# dict.items() = muestra los items

for alumno in alumnos.items():
    print('\nInicio del ciclo')
    print(f'{alumno}')
    print('Fin del ciclo\n')

# lista de dictionarios

alumnos = [
    {
    'nombre': "Alonso", 
    "apellido": "Solano",
    "telefono": "8592-2222",
    "edad": 24,
    "nota": 80
    },
    {
    'nombre': "Didier", 
    "apellido": "Irias",
    "telefono": "8592-2222",
    "edad": 26,
    "nota": 65
    }
    ] # llave y valor, key-value pair

for alumno in alumnos:
    print('\nInicio del ciclo')

    if alumno.get("nota") < 70:
        print(alumno.get('nombre'), ' está reprobrado')
    else:
        print(alumno.get('nombre'), ' está aprobado')

    print('Fin del ciclo\n')