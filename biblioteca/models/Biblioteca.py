import csv
from models.Libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, filtro, valor):
        resultados = [libro for libro in self.libros if getattr(libro, filtro) == valor]
        return resultados

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

    def guardar_libros(self, archivo):
        with open(archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Titulo', 'Autor', 'Año'])
            for libro in self.libros:
                writer.writerow([libro.titulo, libro.autor, libro.ano])

    def cargar_libros(self, archivo):
        try:
            with open(archivo, 'r') as file: # Context Manager
                reader = csv.DictReader(file)
                for row in reader:
                    self.agregar_libro(Libro(row['Titulo'], row['Autor'], row['Año']))
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")