while True:
    edad = input("Edad: ")
    if type(edad)==str:
         print("Escribe un numero entero")
    elif edad<0 or edad>120:
         print("La edad debe estar entre 0 y 120")
    elif  0 <= int(edad) <= 120:
         break
print(f"Edad registrada: {edad}")