import os, shutil
from datetime import datetime

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

def crear_usuario():
    new_nombre = input("Indique su nombre: ")
    new_contra = input("Indique una contraseña: ")

    with open("usuarios.csv", "a") as newuser:
        newuser.write(f"{new_nombre},{new_contra}\n")
    print("¡Usuario creado!")

    if not os.path.exists("log.txt"):
        with open("log.txt", "w") as log:
            log.write(f"Usuario {new_nombre} creado | Hora: {datetime.now()}\n")
    else:
        with open("log.txt", "a") as log:
            log.write(f"Usuario {new_nombre} creado | Hora: {datetime.now()}\n")

def validar_usuario():
    nombre_user = input("Nombre: ")
    contra_user = input("Contraseña: ")

    with open("usuarios.csv", "r") as user:
        for linea in user:
            datos = linea.strip().split(",")

            if nombre_user == datos[0] and contra_user == datos[1]:
                print(f"¡Bienvenido {datos[0]}!\n")
                return True

    print("Usuario y contraseña erróneos.")
    return False

def organizar_archivos(archivo, extension):
    
    if extension == "xlsx":
        carpeta = "Facturas"
    elif extension == "docx":
        carpeta = "Contratos"
    elif extension == "pdf":
        carpeta = "Informes"
    elif extension == "txt":
        carpeta = "Documento"
    
    if not os.path.exists("Backup"):
        os.mkdir("Backup")
    shutil.move(archivo, "Backup")

    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
    shutil.move(archivo, carpeta)

    if not os.path.exists("log.txt"):
        with open("log.txt", "w") as log:
            log.write(f"Movido {archivo} a {carpeta} | Hora: {datetime.now()}\n")
    else:
        with open("log.txt", "a") as log:
            log.write(f"Movido {archivo} a {carpeta} | Hora: {datetime.now()}\n")



salir=False
validado=True

while not salir:

    #menu_usuario()
    # while True:
    #     opcion_usuario=int(input("Bienvenido que desea hacer?\n"))
    
    #     match opcion_usuario:
    #         case 0:
    #             validado = validar_usuario()
    #         case 1:
    #             crear_usuario()
    #             break
    #         case 2:
    #             salir=True
    #             break

    while validado:

        menu_sistema()
        opcion_sistema = input("Indique una opcion:\n")
        lista_archivos = os.listdir(".")
        for i in lista_archivos:
            ip = i.split(".")
            if len(ip) > 1:
                if ip[0] != "log" and ip[-1] != "py" and ip[-1] != "csv":
                    organizar_archivos(i,ip[-1])