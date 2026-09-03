for numero in range(0,7,3):  #Trabajando con rangos de for
    cuadrado = numero ** 2
    print(numero, cuadrado)

materias = ["Python", "Linux", "Interfaces"]
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}. {materia}")

for materia in materias:
    print(materia)

cadena="0123456789ABCDEF"
for letra in cadena:
    print(letra)

for i in range(len(cadena)):
    print(cadena[i])