class Usuario:

    # 1. Clases: Receta para crear un objecto
    # 2. Objecto: Representación de algo en la vida real con sus atributos: un carro, una persona, etc
    # 3. Attributos: Las caracteristicas de un objeto
    # 4. Constructor: La función que crea o inicializa los atributos de la case
    # 5. Instancia: La creación de un objeto con base a una clase

    def __init__(self, correo, contraseña, nombre):
        self.correo = correo
        self.constraseña = contraseña
        self.nombre = nombre

    def login(self, correo, contraseña):

        if self.correo == correo and self.constraseña == contraseña:
            print('Inicio de sesión con éxito')
        else:
            print('Contraseña incorrecta')
    
    def imprimir_nombre(self):
        print('El nombre del usuario es: ', self.nombre)

usuario1 = Usuario('alonso.solano@gmail.com', '1234', 'Alonso')
usuario2 = Usuario('didier.irias@gmail.com', '0000', 'Didier')

usuario1.login('alonso.solano@gmail.com', '1234')
usuario2.login('didier.irias@gmail.com', '1234')

usuario1.imprimir_nombre()
usuario2.imprimir_nombre()
