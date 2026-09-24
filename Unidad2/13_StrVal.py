while True:
    nombre = input("Nombre: ").strip()
    nombre= " ".join(nombre.split())
    if nombre and nombre.replace(" ","").isalpha():
        break
    print("Usa letras y no dejes el nombre vacio.")
nombre_normalizado = nombre.title() #Title sirve para poner la primera letra en mayuscula
print(f"Hola, {nombre_normalizado}")