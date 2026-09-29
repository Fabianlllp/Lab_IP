USUARIO = "alumno"
CLAVE = "python123"
usuario = input("Usuario: ").strip().lower()
clave = input("Contraseña:").strip().lower()
if usuario == USUARIO and clave == CLAVE:
    print("Bienvenido")
else:
    print("Credenciales incorrectas")