try:
    numero = int(input('Digite un numero: '))

    if numero > 1:
        print('Número mayor a 1')

    print(numero/0)
    
except TypeError:
    print('El número ingresado no es un int')
except ZeroDivisionError:
    print('No se puede dividir el número por 0')
except:
    print('Hubo un error')

# Las exepciones
#logs