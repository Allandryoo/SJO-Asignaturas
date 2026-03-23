import os, shutil
from datetime import datetime

def escribir_log(mensaje):
    with open("log.txt", "a") as log:
        log.write(f"{mensaje} | Hora: {datetime.now()}\n")

def menu_usuario():
    opciones_usuario = [
        "Iniciar Sesion",
        "Crear Usuario",
        "Cerrar Programa"
    ]
    for i, o in enumerate(opciones_usuario):
        print(f"{i}: {o}")

def menu_sistema():
    opciones_sistema = [
        "Ordenar archivos",
        "Ver historial de movimientos",
        "Buscar archivos",
        "Eliminar archivos",
        "Restaurar backup"
    ]
    for i, o in enumerate(opciones_sistema):
        print(f"Presiona {i} para: {o}")

def crear_usuario():
    new_nombre = input("Indique su nombre: ")
    new_contra = input("Indique una contraseña: ")

    with open("usuarios.csv", "a") as newuser:
        newuser.write(f"{new_nombre},{new_contra}\n")
    print("¡Usuario creado!")
    escribir_log(f"Usuario {new_nombre} creado")

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
        carpeta = "Documentos"
    else:
        carpeta = "Otros"

    if not os.path.exists("Backup"):
        os.mkdir("Backup")
    shutil.copy(archivo, "Backup")

    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
    shutil.move(archivo, carpeta)
    escribir_log(f"Movido {archivo} a {carpeta}")

def historial_movimientos():
    with open("log.txt", "r") as movimientos:
        for accion in movimientos:
            print(accion)

def buscar_archivo():
    nombre = input("Nombre del archivo a buscar (sin extensión): ")
    encontrado = False

    for archivo in os.listdir("."):
        if archivo.split(".")[0] == nombre:
            print(f"Archivo encontrado: {archivo}")
            encontrado = True

    for carpeta in ["Facturas", "Contratos", "Informes", "Documentos", "Otros"]:
        if os.path.exists(carpeta):
            for archivo in os.listdir(carpeta):
                if archivo.split(".")[0] == nombre:
                    print(f"Archivo encontrado: {carpeta}/{archivo}")
                    encontrado = True

    if not encontrado:
        print("Archivo no encontrado.")

def eliminar_archivo(*archivos):
    for nombre in archivos:
        eliminado = False
        for carpeta in [".", "Facturas", "Contratos", "Informes", "Documentos", "Otros"]:
            ruta = f"{carpeta}/{nombre}"
            if os.path.exists(ruta):
                if not os.path.exists("Backup"):
                    os.mkdir("Backup")
                shutil.copy(ruta, "Backup")
                os.remove(ruta)
                print(f"Eliminado: {ruta}")
                escribir_log(f"Eliminado {nombre} de {carpeta}")
                eliminado = True
        if not eliminado:
            print(f"No encontrado: {nombre}")

def restaurar_backup():
    if not os.path.exists("Backup"):
        print("No existe carpeta de Backup.")
        return

    archivos = os.listdir("Backup")
    if not archivos:
        print("El Backup está vacío.")
        return

    print("Archivos disponibles en Backup:")
    for archivo in archivos:
        print(f"  - {archivo}")

    nombre = input("Nombre del archivo a restaurar (con extensión): ")
    ruta_backup = f"Backup/{nombre}"

    if not os.path.exists(ruta_backup):
        print("Archivo no encontrado en Backup.")
        return

    extension = nombre.split(".")[-1]
    if extension == "xlsx":
        destino = "Facturas"
    elif extension == "docx":
        destino = "Contratos"
    elif extension == "pdf":
        destino = "Informes"
    elif extension == "txt":
        destino = "Documentos"
    else:
        destino = "."

    if not os.path.exists(destino):
        os.mkdir(destino)

    shutil.copy(ruta_backup, destino)
    print(f"Restaurado {nombre} en {destino}")
    escribir_log(f"Restaurado {nombre} en {destino} desde Backup")


salir = False
validado = True

while not salir:

    # menu_usuario()
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
        opcion_sistema = int(input("Indique una opcion:\n"))
        match opcion_sistema:
            case 0:
                for i in os.listdir("."):
                    ip = i.split(".")
                    if len(ip) > 1:
                        if ip[0] != "log" and ip[-1] != "py" and ip[-1] != "csv":
                            organizar_archivos(i, ip[-1])
            case 1:
                historial_movimientos()
            case 2:
                buscar_archivo()
            case 3:
                archivos_eliminar = input("Nombres de los archivos a eliminar (separados por coma): ").split(",")
                eliminar_archivo(*[a.strip() for a in archivos_eliminar])
            case 4:
                restaurar_backup()