#import models.Biblioteca as Biblioteca
from models.Libro import Libro
from models.Biblioteca import Biblioteca

def menu():
    biblioteca = Biblioteca()
    biblioteca.cargar_libros("libros.csv")

    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Mostrar todos los libros")
        print("4. Guardar y salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Año de publicación: ")
            biblioteca.agregar_libro(Libro(titulo, autor, ano))

        elif opcion == "2":
            filtro = input("¿Buscar por (titulo, autor, ano)? ")
            valor = input(f"Introduce el valor de {filtro}: ")
            resultados = biblioteca.buscar_libro(filtro, valor)
            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontró ningún libro.")

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            biblioteca.guardar_libros("libros.csv")
            print("Libros guardados. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

menu()