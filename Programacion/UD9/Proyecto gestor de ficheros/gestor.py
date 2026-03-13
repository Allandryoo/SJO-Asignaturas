import os, shutil

def crear_usuario():
    nombre = input("Indique su nombre: ")
    contra = input("Indique una contraseña: ")

    with open("usuarios.csv", "a") as newuser:
        newuser.write(f"{nombre},{contra}\n")
    print("¡Usuario creado!")

def validar_usuario():
    nombre = input("Nombre: ")
    contraseña = input("Contraseña: ")

    with open("usuarios.csv", "r") as user:
        for linea in user:
            datos = linea.strip().split(",")

            if nombre == datos[0] and contraseña == datos[1]:
                print(f"¡Bienvenido {datos[0]}!\n")
                return True

    print("Usuario y contraseña erróneos.")
    return False

def organizar_archivos(archivo, extension):
    
    if extension == "xls":
        carpeta = "Facturas"
    elif extension == "docx":
        carpeta = "Contratos"
    elif extension == "pdf":
        carpeta = "Informes"
    elif extension == "txt":
        carpeta = "Backup"

    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
    shutil.move(archivo, carpeta)
    if not os.path.exists("log.txt"):
        with open("log.txt", "w") as log:
            log.write(f"Movido {archivo} a {carpeta}\n")
    else:
        with open("log.txt", "a") as log:
            log.write(f"Movido {archivo} a {carpeta}\n")

def menu_usuario():
    opciones_usuario = [
        "Iniciar Sesion",
        "Crear Usuario",
        "Cerrar Programa"
    ]
    for i,o in enumerate(opciones_usuario):
        print(f"{i}: {o}")

def menu_sistema():
    opciones_sistema = [
        "Ordenar archivos",
        "Ver historial de movimientos"
    ]
    for i,o in enumerate(opciones_sistema):
        print(f"Presiona {i} para: {o}")

salir=False
validado=False

while not salir:

    menu_usuario()
    while True:
        opcion_usuario=int(input("Bienvenido que desea hacer?\n"))
    
        match opcion_usuario:
            case 0:
                validado = validar_usuario()
                break
            case 1:
                crear_usuario()
                break
            case 2:
                break

    while validado:

        menu_sistema()
        opcion_sistema = input("Indique una opcion:\n")
        lista_archivos = os.listdir(".")
        for i in lista_archivos:
            ip = i.split(".")
            if len(ip) > 1:
                if ip[0] != "log" and ip[-1] != "py":
                    organizar_archivos(i,ip[-1])