nota_examen = int(input("Ingrese una nota: "))

if nota_examen >= 70:
    # se mando
    # se escribe un archivo excel
    print("Aprobado")
elif nota_examen >= 60 and nota_examen <= 70: 
    print("Ampliación")
else:
    print("Reprobado")


